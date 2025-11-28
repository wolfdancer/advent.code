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

    def is_safe_with_dampener(self):
        """
        Check if this report is safe with the Problem Dampener.
        The dampener allows removing a single level to make an unsafe report safe.

        Returns:
            bool: True if the report is safe or can be made safe by removing one level
        """
        # First check if already safe without dampener
        if self.is_safe():
            return True

        # Try removing each level one at a time
        for i in range(len(self.levels)):
            # Create new levels list without the element at index i
            dampened_levels = self.levels[:i] + self.levels[i+1:]
            # Create new report and check if it's safe
            dampened_report = Report(dampened_levels)
            if dampened_report.is_safe():
                return True

        return False


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
