//go:build ignore

package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("../2025/day1.txt")
	if err != nil {
		log.Fatalf("Failed to open file: %v", err)
	}
	defer file.Close()

	dial := 50
	password := 0

	scanner := bufio.NewScanner(file)
	lineNum := 0
	for scanner.Scan() {
		lineNum++
		line := scanner.Text()

		if len(line) < 2 {
			log.Fatalf("Line %d is too short: %s", lineNum, line)
		}

		direction := line[0]
		clicksStr := line[1:]

		clicks, err := strconv.Atoi(clicksStr)
		if err != nil {
			log.Fatalf("Failed to parse clicks on line %d: %s", lineNum, line)
		}

		// Track if dial is 0 at the beginning of the loop
		wasOn0 := dial == 0

		// Integer division of clicks by 100, add to password
		password += clicks / 100

		// Mod clicks by 100
		clicks = clicks % 100

		// Update dial based on direction
		switch direction {
		case 'L':
			dial -= clicks
		case 'R':
			dial += clicks
		default:
			log.Fatalf("Invalid direction on line %d: %s", lineNum, line)
		}

		// Handle negative dial
		if dial < 0 {
			if !wasOn0 {
				password++
			}
			dial += 100
		}

		// Handle dial >= 100
		if dial >= 100 {
			if dial != 100 {
				password++
			}
			dial -= 100
		}

		// Check if dial is 0
		if dial == 0 {
			password++
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatalf("Error reading file: %v", err)
	}

	fmt.Println(password)
}
