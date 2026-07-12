# Day 1 Commit Guide

## Recommended commit

```bash
git add .
git commit -m "feat(foundation): initialize Ming Foundation 1.0 repository"
git branch -M main
git remote add origin https://github.com/YuemingHub/Ming-Foundation.git
git push -u origin main
```

When `origin` already exists:

```bash
git remote set-url origin https://github.com/YuemingHub/Ming-Foundation.git
git push -u origin main
```

## Validation before push

```bash
python scripts/validate_repository.py
```

## Codex instruction

```text
Open the local Ming-Foundation repository. Extract the supplied Day 1 package into the repository root without adding an extra nested directory. Run:

python scripts/validate_repository.py

Review git status. Commit all Day 1 files with:

feat(foundation): initialize Ming Foundation 1.0 repository

Push the main branch to:
https://github.com/YuemingHub/Ming-Foundation

Do not modify other repositories. Do not add private keys, .env files, server credentials, personal data, or raw family case data. After pushing, report the commit hash and the validation result.
```
