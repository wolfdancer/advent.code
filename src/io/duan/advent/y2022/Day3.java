package io.duan.advent.y2022;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.stream.Collectors;

public class Day3 {
    public static void main(String... args) throws IOException {
        try(var stream = Files.lines(Path.of("day3.1.txt"))) {
            final var result = stream
                    .map(Day3::sharedItem)
                    .map(Day3::priority)
                    .reduce(0, Integer::sum);
            System.out.println("answer: " + result);
        }
    }

    public static int priority(Character letter) {
        if (Character.isUpperCase(letter)) {
            return letter.compareTo('A') + 27;
        } else {
            return letter.compareTo('a') + 1;
        }
    }

    private static Character sharedItem(String line) {
        final var midPoint = line.length() / 2;
        final var first = line.substring(0, midPoint).chars()
                .mapToObj(e -> (char) e)
                .collect(Collectors.toSet());
        final var second = line.substring(midPoint).chars()
                .mapToObj(e -> (char) e)
                .collect(Collectors.toSet());
        first.retainAll(second);
        if (first.size() != 1) {
            throw new IllegalStateException("expected only one but found " + first);
        }
        return first.iterator().next();
    }
}
