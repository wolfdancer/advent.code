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
		for id := range invalidIDs {
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

func identifyInvalidIDs(r Range) map[int]bool {
	invalidIDs := make(map[int]bool)

	for numDigits := 1; numDigits <= countDigits(r.last-1); numDigits++ {
		// Try different numbers of parts (2, 3, 4, ...)
		for numParts := 2; numParts <= numDigits; numParts++ {
			// Each part must have equal length
			if numDigits%numParts != 0 {
				continue
			}

			partLength := numDigits / numParts
			divisor := pow10(partLength)

			// Start at the beginning of numbers with this digit count
			start := pow10(numDigits - 1)
			if start < r.first {
				start = r.first
			}

			// End at numbers with this digit count
			end := pow10(numDigits)
			if end > r.last {
				end = r.last
			}

			// Iterate through candidates
			current := start
			for current < end {
				// Extract all parts
				temp := current
				parts := make([]int, numParts)
				allEqual := true

				for i := numParts - 1; i >= 0; i-- {
					parts[i] = temp % divisor
					temp /= divisor
				}

				// Check if all parts are equal
				firstPart := parts[0]
				for i := 1; i < numParts; i++ {
					if parts[i] != firstPart {
						allEqual = false
						break
					}
				}

				if allEqual {
					invalidIDs[current] = true
				}

				// Move to next candidate: increase first part by 1
				firstPart++
				if firstPart >= divisor {
					// Overflow - we're done with this digit count and part count
					break
				}

				// Reconstruct the number with all parts equal to firstPart
				current = 0
				for i := 0; i < numParts; i++ {
					current = current*divisor + firstPart
				}
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
