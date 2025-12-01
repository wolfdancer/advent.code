def main():
    dial = 50
    password = 0

    with open('day1.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Track if dial is 0 at the beginning of the loop
            was_on_0 = (dial == 0)

            direction = line[0]
            clicks = int(line[1:])

            # Add integer division of clicks by 100 to password
            password += clicks // 100

            clicks = clicks % 100

            if direction == 'L':
                dial -= clicks
            elif direction == 'R':
                dial += clicks
            else:
                print(f"Error: Invalid direction in line: {line}")
                return

            # If dial is less than 0, increase password by 1 but only if was_on_0 is false
            if dial < 0:
                if not was_on_0:
                    password += 1
                dial += 100

            # If dial is bigger than or equals 100, increase password by 1 but only if dial is not 100
            if dial >= 100:
                if dial != 100:
                    password += 1
                dial -= 100

            if dial == 0:
                password += 1

    print(password)

if __name__ == '__main__':
    main()
