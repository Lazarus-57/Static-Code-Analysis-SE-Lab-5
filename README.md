# Static Code Analysis — Lab 5

## Project Overview
This lab involves performing static code analysis on a Python program (`inventory_system.py`) using **Pylint**, **Flake8**, and **Bandit**.  
The objective was to detect, document, and fix issues to improve **code quality**, **security**, and **maintainability**.

## Tools Used
- **Pylint** — for style and convention checks  
- **Flake8** — for PEP 8 compliance  
- **Bandit** — for security vulnerability analysis

## Files in this Repository
| File                     | Description                                                                 |
|---------------------------|------------------------------------------------------------------------------|
| `inventory_system.py`     | Final cleaned Python code after fixing all issues                           |
| `pylint_report.txt`       | Final Pylint static analysis report (score: 10/10)                           |
| `flake8_report.txt`       | Final Flake8 report (0 issues)                                              |
| `bandit_report.txt`       | Final Bandit security report (0 vulnerabilities)                            |
| `Issues Table.md`         | Documented list of issues found and fixes applied                            |
| `REFLECTION.md`           | Reflection answers and learnings                                            |
| `README.md`               | Project overview and submission details                                     |

## Final Results
- Pylint Score: **10.00 / 10**
- Flake8: **0 Issues**
- Bandit: **0 Security Vulnerabilities**
- All functions refactored, docstrings added, globals removed, security flaws eliminated.

## Instructions to Run
```bash
# Run Pylint
pylint inventory_system.py

# Run Flake8
flake8 inventory_system.py

# Run Bandit
bandit -r inventory_system.py
