import re
from year2025.day10 import IndicatorLights, Buttons, process


def parse_line(line):
    # Parse indicator lights: [...]
    lights_match = re.search(r'\[([^\]]+)\]', line)
    indicator_lights = IndicatorLights(lights_match.group(1))

    # Parse all button groups: (...)
    buttons = []
    for match in re.finditer(r'\(([^)]+)\)', line):
        values = list(map(int, match.group(1).split(',')))
        buttons.append(Buttons(values))

    return indicator_lights, buttons


def main():
    total = 0
    with open('day10.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                indicator_lights, buttons = parse_line(line)
                total += process(indicator_lights, buttons)
    print(total)


if __name__ == '__main__':
    main()
