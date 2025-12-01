def main():
    dial = 50
    password = 0

    with open('day1.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            clicks = int(line[1:])

            clicks = clicks % 100

            if direction == 'L':
                dial -= clicks
            elif direction == 'R':
                dial += clicks
            else:
                print(f"Error: Invalid direction in line: {line}")
                return

            if dial < 0:
                dial += 100

            if dial >= 100:
                dial -= 100

            if dial == 0:
                password += 1

    print(password)

if __name__ == '__main__':
    main()
