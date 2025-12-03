# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Python Environment

**CRITICAL**: Always use the virtual environment in `.venv` when running Python scripts:

```bash
source .venv/bin/activate && python dayX.Y.py
```

## Project Overview

This is an Advent of Code 2025 solutions repository. Each day's challenge has two parts, and solutions are self-contained Python scripts that read input files and print answers to stdout.

## File Naming Convention

- `dayX.Y.py` - Solution scripts (X = day number, Y = part number)
- `dayX.txt` - Actual puzzle input data
- `dayX.example.txt` - Example/test input from problem description
- `test_dayX.py` - Optional test scripts for validation

## Code Architecture

## Running Solutions

Execute a specific day's solution:
```bash
source .venv/bin/activate && python day3.1.py
```

Test with example input (modify script to use `.example.txt` file):
```bash
source .venv/bin/activate && python test_day3.py
```
