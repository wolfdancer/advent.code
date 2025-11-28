from year2024.day2 import parse

if __name__ == "__main__":
    reports = parse("day2_safety_reports.txt")
    safe_reports = [report for report in reports if report.is_safe()]
    result = len(safe_reports)
    print(f"Total safe reports: {result}")
