from year2024.day2 import parse

if __name__ == "__main__":
    reports = parse("day2_safety_reports.txt")
    safe_reports_with_dampener = [report for report in reports if report.is_safe_with_dampener()]
    result = len(safe_reports_with_dampener)
    print(f"Total safe reports with dampener: {result}")
