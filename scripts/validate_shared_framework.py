#!/usr/bin/env python3
"""Validate the shareable framework using only the Python standard library."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "AGENTS.md",
    "README.md",
    "START_HERE.md",
    "SETUP_INSTRUCTIONS.md",
    "CONTRIBUTING.md",
    "00_My_Workspace/README.md",
    "00_My_Workspace/MY_ASSIGNMENTS.template.md",
    "01_Rules/zendesk-account-to-outreach-rules.md",
    "01_Rules/email-outreach-drafting-standard.md",
    "02_Knowledge/enterprise-bdr-operating-controls.md",
    ".github/CODEOWNERS",
)
TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".yml",
    ".yaml",
    ".json",
    ".csv",
    ".py",
    ".sh",
    ".zsh",
}
EXPECTED_SKILL_COUNT = 48


def repository_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line for line in result.stdout.splitlines() if line]


def main() -> int:
    errors: list[str] = []

    for relative_path in REQUIRED:
        if not (ROOT / relative_path).is_file():
            errors.append(f"Missing required file: {relative_path}")

    tracked = repository_files()
    forbidden_tracked = {
        "00_My_Workspace/MY_ASSIGNMENTS.md",
    }
    for relative_path in tracked:
        if relative_path in forbidden_tracked or relative_path.startswith("08_Working_Accounts/"):
            errors.append(f"Local account work is tracked: {relative_path}")

    files_to_check = set(tracked).union(REQUIRED)
    for relative_path in sorted(files_to_check):
        path = ROOT / relative_path
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "\N{EM DASH}" in text:
            errors.append(f"Em dash found: {relative_path}")
        private_markers = (
            "/" + "Users" + "/",
            "will" + "." + "richardson",
            "@" + "zendesk.com",
        )
        for marker in private_markers:
            if marker in text:
                errors.append(
                    f"Private or machine-specific marker found in "
                    f"{relative_path}: {marker}"
                )

    skills_root = ROOT / "06_Skills"
    skill_directories = (
        sorted(path for path in skills_root.iterdir() if path.is_dir())
        if skills_root.is_dir()
        else []
    )
    if len(skill_directories) != EXPECTED_SKILL_COUNT:
        errors.append(
            f"Expected {EXPECTED_SKILL_COUNT} skill folders, found {len(skill_directories)}"
        )
    for skill_directory in skill_directories:
        skill_file = skill_directory / "SKILL.md"
        agent_file = skill_directory / "agents" / "openai.yaml"
        if not skill_file.is_file():
            errors.append(f"Skill is missing SKILL.md: {skill_directory.name}")
            continue
        if not agent_file.is_file():
            errors.append(f"Skill is missing agents/openai.yaml: {skill_directory.name}")
        skill_text = skill_file.read_text(encoding="utf-8")
        expected_name = f"name: {skill_directory.name}"
        if expected_name not in skill_text.splitlines()[:6]:
            errors.append(f"Skill name does not match folder: {skill_directory.name}")

    skills_readme = skills_root / "README.md"
    if skills_readme.is_file():
        catalog_text = skills_readme.read_text(encoding="utf-8")
        for skill_directory in skill_directories:
            catalog_entry = f"`{skill_directory.name}`"
            if catalog_entry not in catalog_text:
                errors.append(f"Skill is missing from catalog: {skill_directory.name}")

    template = ROOT / "00_My_Workspace/MY_ASSIGNMENTS.template.md"
    if template.is_file():
        required_headers = (
            "Account name",
            "CRM Account ID",
            "Website",
            "Aligned AE",
            "Motion",
            "Priority",
        )
        template_text = template.read_text(encoding="utf-8")
        for header in required_headers:
            if header not in template_text:
                errors.append(f"Assignment template is missing column: {header}")

    if errors:
        print("Framework validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Framework validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
