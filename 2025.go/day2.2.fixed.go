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

	current := r.first

	for current < r.last {
		numDigits := countDigits(current)

		// Try different numbers of parts (2, 3, 4, ...)
		for numParts := 2; numParts <= numDigits; numParts++ {
			// Each part must have equal length
			if numDigits%numParts != 0 {
				continue
			}

			partLength := numDigits / numParts
			divisor := pow10(partLength)
			nextPower := pow10(numDigits)

			// Reset candidate for each division strategy
			candidate := current

			// Middle candidates loop - iterate through candidates with this division
			for candidate < nextPower && candidate < r.last {
				// Extract all parts
				temp := candidate
				parts := make([]int, numParts)
				for i := numParts - 1; i >= 0; i-- {
					parts[i] = temp % divisor
					temp /= divisor
				}

				leader := parts[0]
				finished := true

				// Inner validation loop - compare leader to other parts
				for i := 1; i < numParts; i++ {
					if leader > parts[i] {
						// Replace all parts with leader
						candidate = 0
						for j := 0; j < numParts; j++ {
							candidate = candidate*divisor + leader
						}
						finished = false
						break
					} else if leader < parts[i] {
						// Increase leader and reconstruct
						candidate = increaseLeader(leader, numParts, divisor)
						finished = false
						break
					}
				}

				if finished {
					// All parts are equal - this is an invalid ID
					invalidIDs[candidate] = true
					candidate = increaseLeader(leader, numParts, divisor)
				}
			}
		}

		// Move to next power of 10
		current = pow10(numDigits)
	}

	return invalidIDs
}

func increaseLeader(leader, numParts, divisor int) int {
	leader++
	// Check if leader overflowed to next power of 10
	if leader >= divisor {
		// Calculate total number of digits: partLength * numParts
		partLength := countDigits(divisor - 1)
		totalDigits := partLength * numParts
		return pow10(totalDigits)
	}

	// Reconstruct number by repeating the leader
	result := 0
	for i := 0; i < numParts; i++ {
		result = result*divisor + leader
	}
	return result
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
