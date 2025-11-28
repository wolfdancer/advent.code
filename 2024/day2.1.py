def is_safe_report(report):
    """
    Check if a report is safe based on the following rules:
    1. Determine trending (increase/decrease) from first 2 outputs
    2. For each subsequent output:
       - Check if it matches the trending direction
       - Check if absolute difference is between 1 and 3 (inclusive)
    """
    if len(report) < 2:
        return False

    # Determine trending from first two outputs
    if report[1] > report[0]:
        trending = "increase"
    elif report[1] < report[0]:
        trending = "decrease"
    else:
        # No change means unsafe
        return False

    # Iterate from second output to the end
    for i in range(1, len(report)):
        current = report[i]
        previous = report[i - 1]

        # Check if it matches the trending
        if trending == "increase" and current < previous:
            return False
        if trending == "decrease" and current > previous:
            return False

        # Check if absolute difference is between 1 and 3
        diff = abs(current - previous)
        if diff < 1 or diff > 3:
            return False

    return True


def parse_and_count_safe_reports(filename):
    """
    Read reports from file and count how many are safe.
    """
    safe_count = 0

    with open(filename, 'r') as f:
        for line in f:
            # Parse the report (list of numbers)
            report = list(map(int, line.strip().split()))

            if is_safe_report(report):
                safe_count += 1

    return safe_count


if __name__ == "__main__":
    result = parse_and_count_safe_reports("day2_safety_reports.txt")
    print(f"Total safe reports: {result}")
