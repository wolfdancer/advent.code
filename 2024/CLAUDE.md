# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Advent of Code 2024 solutions repository. The parent directory contains solutions from multiple years (2022, 2024, 2025), with this directory (2024) being the active year.

## Project Structure

- Python solutions are stored as individual files: `dayN.M.py` (e.g., `day1.1.py`, `day1.2.py`)
  - `N` = day number
  - `M` = part number (1 or 2)
- Input data files are named: `dayN.txt` or `dayN_description.txt` (e.g., `day1.txt`, `day2_safety_reports.txt`)
- Python virtual environment is in `.venv/` (Python 3.11)

## Running Solutions

Activate the virtual environment and run solutions directly:
```bash
source .venv/bin/activate
python day1.1.py
python day2.1.py
```

Each solution file is self-contained and reads its corresponding input file.

## Code Patterns

Solutions follow a consistent structure:
1. Helper functions for core logic (e.g., `is_safe_report()`)
2. Use domain specific method names instead of generic names like "solve"
3. `if __name__ == "__main__"` block that:
   - Calls the solve function with the input filename
   - Prints the result with a descriptive label

Input parsing typically:
- Opens the data file in the solve function
- Processes line by line
- Uses `strip().split()` for whitespace-separated values
- Converts to appropriate types (usually `int()`)
