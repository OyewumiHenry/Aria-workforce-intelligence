#!/usr/bin/env python3
"""ARIA pre-deployment validation for local and Streamlit Cloud readiness."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
APP_DIR = SCRIPT_DIR
DATA_DIR = PROJECT_ROOT / "01_Data"


def project_path(relative_path: str) -> Path:
    return PROJECT_ROOT / relative_path


def app_path(relative_path: str) -> Path:
    return APP_DIR / relative_path


def print_header(text: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"  {text}")
    print(f"{'=' * 60}\n")


def print_check(status: bool, text: str) -> None:
    symbol = "PASS" if status else "FAIL"
    print(f"{symbol}: {text}")


def check_python_version() -> bool:
    print_header("Python Version Check")
    version = sys.version_info
    required = (3, 10)

    if version >= required:
        print_check(True, f"Python {version.major}.{version.minor}.{version.micro} (3.10+ required)")
        return True

    print_check(False, f"Python {version.major}.{version.minor}.{version.micro} (upgrade to 3.10+ needed)")
    return False


def check_files() -> bool:
    print_header("Required Files Check")

    required_files = [
        ("deployment/aria_app.py", project_path("deployment/aria_app.py")),
        ("deployment/aria_config.py", project_path("deployment/aria_config.py")),
        ("deployment/requirements.txt", project_path("deployment/requirements.txt")),
        ("packages.txt", project_path("packages.txt")),
        (".gitignore", project_path(".gitignore")),
        (".streamlit/config.toml", project_path(".streamlit/config.toml")),
        ("01_Data/aria_dataset_manifest.json", DATA_DIR / "aria_dataset_manifest.json"),
        ("01_Data/final_aria_dataset.csv", DATA_DIR / "final_aria_dataset.csv"),
        ("01_Data/aria_executive_review_dataset.csv", DATA_DIR / "aria_executive_review_dataset.csv"),
        ("01_Data/aria_executive_overrides.csv", DATA_DIR / "aria_executive_overrides.csv"),
    ]

    all_exist = True
    for label, file_path in required_files:
        exists = file_path.exists()
        print_check(exists, label)
        if not exists:
            all_exist = False

    return all_exist


def check_requirements() -> bool:
    print_header("Dependencies Check")

    required = [
        "setuptools",
        "wheel",
        "streamlit",
        "pandas",
        "numpy",
        "plotly",
        "vaderSentiment",
    ]

    req_file = project_path("deployment/requirements.txt")
    if not req_file.exists():
        print_check(False, "deployment/requirements.txt not found")
        return False

    content = req_file.read_text(encoding="utf-8").lower()
    all_found = True

    for package in required:
        found = package.lower() in content
        print_check(found, f"{package} in deployment/requirements.txt")
        if not found:
            all_found = False

    return all_found


def check_system_packages() -> bool:
    print_header("System Package Configuration Check")

    packages_file = project_path("packages.txt")
    if not packages_file.exists():
        print_check(False, "packages.txt not found")
        return False

    content = packages_file.read_text(encoding="utf-8").lower()
    required = [
        "build-essential",
        "python3-dev",
        "libffi-dev",
        "libssl-dev",
    ]

    all_found = True
    for package in required:
        found = package in content
        print_check(found, f"{package} in packages.txt")
        if not found:
            all_found = False

    return all_found


def check_streamlit_config() -> bool:
    print_header("Streamlit Configuration Check")

    config_file = project_path(".streamlit/config.toml")
    if not config_file.exists():
        print_check(False, ".streamlit/config.toml not found")
        return False

    content = config_file.read_text(encoding="utf-8")
    checks = [
        ('headless = true', "Headless mode enabled"),
        ('fileWatcherType = "none"', "Production mode (file watcher disabled)"),
        ('toolbarMode = "viewer"', "Viewer toolbar mode"),
        ('showErrorDetails = false', "Detailed Streamlit errors hidden"),
        ('enableXsrfProtection = true', "CSRF protection enabled"),
    ]

    all_good = True
    for check_str, description in checks:
        found = check_str in content
        print_check(found, description)
        if not found:
            all_good = False

    return all_good


def check_data_integrity() -> bool:
    print_header("Data Integrity Check")

    manifest_path = DATA_DIR / "aria_dataset_manifest.json"
    if not manifest_path.exists():
        print_check(False, "Manifest file not found")
        return False

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        print_check(True, "Manifest valid JSON")

        hash_pairs = [
            ("raw_dataset_sha256", "final_aria_dataset.csv"),
            ("executive_dataset_sha256", "aria_executive_review_dataset.csv"),
            ("override_table_sha256", "aria_executive_overrides.csv"),
        ]

        for manifest_key, filename in hash_pairs:
            expected_hash = str(manifest.get(manifest_key, "")).strip().lower()
            file_path = DATA_DIR / filename
            if not expected_hash:
                print_check(False, f"Missing manifest key {manifest_key}")
                return False
            if not file_path.exists():
                print_check(False, f"{filename} not found")
                return False

            actual_hash = hashlib.sha256(file_path.read_bytes()).hexdigest()
            matches = actual_hash == expected_hash
            print_check(matches, f"{filename} hash verified ({manifest_key})")
            if not matches:
                return False

        return True
    except Exception as exc:  # pragma: no cover - defensive validation script
        print_check(False, f"Manifest validation failed: {exc}")
        return False


def check_git_ignore() -> bool:
    print_header("Git Ignore Configuration Check")

    gitignore_file = project_path(".gitignore")
    if not gitignore_file.exists():
        print_check(False, ".gitignore not found")
        return False

    content = gitignore_file.read_text(encoding="utf-8")
    should_exclude = [
        ".vscode/",
        "__pycache__/",
        "*.pyc",
        ".ipynb_checkpoints/",
        ".env",
        ".venv/",
        ".streamlit/secrets.toml",
        "streamlit_local.out",
        "streamlit_local.err",
        ".streamlit_local_pid",
    ]

    all_good = True
    for pattern in should_exclude:
        found = pattern in content
        print_check(found, f"Excludes {pattern}")
        if not found:
            all_good = False

    return all_good


def check_app_structure() -> bool:
    print_header("Application Structure Check")

    app_file = app_path("aria_app.py")
    config_file = app_path("aria_config.py")

    if not app_file.exists():
        print_check(False, "aria_app.py not found")
        return False
    if not config_file.exists():
        print_check(False, "aria_config.py not found")
        return False

    app_content = app_file.read_text(encoding="utf-8")
    config_content = config_file.read_text(encoding="utf-8")

    checks = [
        ("import streamlit as st", "Streamlit imported"),
        ("import pandas as pd", "Pandas imported"),
        ("import plotly", "Plotly imported"),
        ("configure_app()", "Shared app configuration applied"),
        ("@st.cache_data", "Caching configured"),
        ("from aria_config import", "Shared app config module used"),
    ]

    all_good = True
    for check_str, description in checks:
        found = check_str in app_content
        print_check(found, description)
        if not found:
            all_good = False

    config_checks = [
        ("st.set_page_config", "Page config defined in aria_config.py"),
        ("APP_CSS", "Shared app styling defined in aria_config.py"),
        ('PROJECT_ROOT = APP_DIR.parent', "Project root resolves from deployment directory"),
        ('DATA_DIR = PROJECT_ROOT / "01_Data"', "Dashboard uses the single root governance bundle"),
    ]

    for check_str, description in config_checks:
        found = check_str in config_content
        print_check(found, description)
        if not found:
            all_good = False

    print_check(len(app_content) > 10000, f"Application size: {len(app_content)} bytes")
    return all_good


def main() -> int:
    print("\n" + "=" * 60)
    print("  ARIA PRE-DEPLOYMENT FINAL VALIDATION")
    print("=" * 60)
    print(f"Project root: {PROJECT_ROOT}")
    print(f"App directory: {APP_DIR}")

    checks = [
        ("Python Version", check_python_version),
        ("Required Files", check_files),
        ("Dependencies", check_requirements),
        ("System Packages", check_system_packages),
        ("Streamlit Config", check_streamlit_config),
        ("Data Integrity", check_data_integrity),
        ("Git Ignore", check_git_ignore),
        ("App Structure", check_app_structure),
    ]

    results = {}
    for name, check_func in checks:
        results[name] = check_func()

    print_header("FINAL VALIDATION REPORT")

    passed = sum(results.values())
    total = len(results)

    for name, result in results.items():
        print_check(result, name)

    print(f"\nPassed: {passed}/{total}")

    if passed == total:
        print("\nVALIDATION COMPLETE: READY FOR DEPLOYMENT\n")
        print("Recommended next steps:")
        print("1. Push the repository to GitHub")
        print("2. In Streamlit Community Cloud, select the repository")
        print("3. Set the main file path to deployment/aria_app.py")
        print("4. Choose Python 3.10 in the app settings")
        print("5. Deploy")
        print()
        return 0

    print("\nVALIDATION FAILED: Fix the items above before publishing.\n")
    return 1


if __name__ == "__main__":
    sys.exit(main())
