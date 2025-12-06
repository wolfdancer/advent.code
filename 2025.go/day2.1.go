//go:build ignore

package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Range struct {
	first int
	last  int
}

func main() {
	data, err := os.ReadFile("../2025/day2.txt")
	if err != nil {
		log.Fatalf("Failed to read file: %v", err)
	}

	line := strings.TrimSpace(string(data))
	ranges := parseRanges(line)

	total := 0
	for _, r := range ranges {
		invalidIDs := identifyInvalidIDs(r)
		sum := 0
		for _, id := range invalidIDs {
			sum += id
		}
		total += sum
	}

	fmt.Println(total)
}

func parseRanges(line string) []Range {
	var ranges []Range
	pairs := strings.Split(line, ",")

	for _, pair := range pairs {
		parts := strings.Split(pair, "-")
		if len(parts) != 2 {
			log.Fatalf("Invalid range format: %s", pair)
		}

		first, err := strconv.Atoi(parts[0])
		if err != nil {
			log.Fatalf("Failed to parse first value: %s", parts[0])
		}

		last, err := strconv.Atoi(parts[1])
		if err != nil {
			log.Fatalf("Failed to parse last value: %s", parts[1])
		}

		// Add 1 to last to make it inclusive
		ranges = append(ranges, Range{first: first, last: last + 1})
	}

	return ranges
}

func identifyInvalidIDs(r Range) []int {
	var invalidIDs []int
	current := r.first

	for current < r.last {
		numDigits := countDigits(current)

		// If odd number of digits, jump to next power of 10
		if numDigits%2 == 1 {
			current = pow10(numDigits)
			continue
		}

		// Even number of digits - split in half
		halfDigits := numDigits / 2
		divisor := pow10(halfDigits)

		firstHalf := current / divisor
		secondHalf := current % divisor

		if firstHalf > secondHalf {
			// Replace second half with first half
			current = firstHalf*divisor + firstHalf
		} else if firstHalf == secondHalf {
			// Found an invalid ID
			invalidIDs = append(invalidIDs, current)
			// Move to next candidate: increase first half by 1
			firstHalf++
			if firstHalf >= divisor {
				// Overflow - jump to next power of 10
				current = pow10(numDigits)
			} else {
				current = firstHalf*divisor + firstHalf
			}
		} else {
			// firstHalf < secondHalf
			// Increase first half by 1 and replace second half
			firstHalf++
			if firstHalf >= divisor {
				// Overflow - jump to next power of 10
				current = pow10(numDigits)
			} else {
				current = firstHalf*divisor + firstHalf
			}
		}
	}

	return invalidIDs
}

func countDigits(n int) int {
	if n == 0 {
		return 1
	}
	count := 0
	for n > 0 {
		count++
		n /= 10
	}
	return count
}

func pow10(n int) int {
	result := 1
	for i := 0; i < n; i++ {
		result *= 10
	}
	return result
}
