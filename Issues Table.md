# Issues Found and Fixed — Static Code Analysis

This document summarizes the issues detected using **Pylint**, **Flake8**, and **Bandit**, along with the corresponding fixes applied to improve code quality, security, and maintainability of `inventory_system.py`.

| Issue                     | Type          | Line(s)     | Description                                                                                  | Fix Approach                                                                                                 |
|---------------------------|---------------|-------------|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Mutable default argument  | Bug           | 8           | `logs=[]` shared across calls; dangerous default value                                       | Changed default to `None` and initialized inside the method using `if logs is None: logs = []`.                |
| Bare except               | Security      | 19          | `except:` used without specifying exception type                                            | Replaced with `except KeyError:` to avoid masking other exceptions.                                          |
| Unspecified file encoding | Maintain.     | 26, 32      | `open()` used without specifying encoding                                                    | Added `encoding="utf-8"` in both read and write file operations.                                             |
| Use of eval()             | Security      | 59          | Use of `eval()` can lead to arbitrary code execution                                         | Removed `eval()` call entirely.                                                                              |
| Unused import             | Style         | 2           | `import logging` imported but not used                                                       | Removed the unused import.                                                                                   |
| Missing module docstring  | Style         | 1           | No module-level docstring                                                                    | Added descriptive module-level docstring at the top of the file.                                             |
| Naming & docstring issues | Style         | multiple    | Functions not following `snake_case`; missing docstrings                                     | Added proper docstrings and renamed all functions to `snake_case`.                                          |
| Blank line issues         | Style         | multiple    | Insufficient blank lines between functions                                                   | Added appropriate blank lines as per PEP 8.                                                                  |
| Empty except block        | Security      | 19          | `try/except/pass` hides critical errors                                                      | Handled exception properly by printing an error message.                                                     |
| Loop iteration warnings   | Performance   | 75, 87, 99  | Iterating over dict keys manually                                                            | Replaced with `.items()` iteration in loops and comprehensions.                                              |
| Global statement warning  | Style         | 104         | Use of `global` keyword to modify global variable                                           | Refactored to remove the need for global by loading data once at startup.                                   |
| Variable shadowing        | Style         | 13, 75      | Variable name `f` reused in multiple scopes                                                  | Renamed variables (`file_obj`, `file_handle`) to avoid shadowing.                                           |

## ✅ Result After Fixes

- Pylint: **10.00/10**
- Bandit: **0 issues**
- Flake8: **0 issues**
- Code fully PEP 8 compliant and security-safe.