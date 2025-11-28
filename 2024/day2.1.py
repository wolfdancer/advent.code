class Report:
    """
    Represents a safety report containing a list of level numbers.
    """
    def __init__(self, levels):
        """
        Initialize a Report with a list of level numbers.

        Args:
            levels: List of integer levels
        """
        self.levels = levels

    def is_safe(self):
        """
        Check if this report is safe based on the following rules:
        1. Determine trending (increase/decrease) from first 2 outputs
        2. For each subsequent output:
           - Check if it matches the trending direction
           - Check if absolute difference is between 1 and 3 (inclusive)
        """
        if len(self.levels) < 2:
            return False

        # Determine trending from first two outputs
        if self.levels[1] > self.levels[0]:
            trending = "increase"
        elif self.levels[1] < self.levels[0]:
            trending = "decrease"
        else:
            # No change means unsafe
            return False

        # Iterate from second output to the end
        for i in range(1, len(self.levels)):
            current = self.levels[i]
            previous = self.levels[i - 1]

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


def parse(filename):
    """
    Read reports from file and return them.
    """
    reports = []
    with open(filename, 'r') as f:
        for line in f:
            # Parse the report (list of numbers)
            levels = list(map(int, line.strip().split()))
            reports.append(Report(levels))
    return reports


if __name__ == "__main__":
    reports = parse("day2_safety_reports.txt")
    safe_reports = [report for report in reports if report.is_safe()]
    result = len(safe_reports)
    print(f"Total safe reports: {result}")
