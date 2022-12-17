package io.duan.advent.y2022;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Objects;
import java.util.stream.IntStream;

public class Day15Part2 {
    public static void main(String... args) throws IOException {
        try (var stream = Files.lines(Path.of("day15.txt"))) {
            var sensors = stream
                    .map(Day15::parse)
                    .toList();
            var maxY = 4000000;
            var optionalPosition = IntStream.range(0, maxY + 1)
                    .mapToObj(y -> new Day15.Coverage(y, sensors))
                    .map(coverage -> coverage.findUncovered(0, maxY))
                    .filter(Objects::nonNull)
                    .findFirst();
            if (optionalPosition.isPresent()) {
                Day15.Position position = optionalPosition.get();
                System.out.printf("located %s%n", position);
                System.out.printf("tuning frequency %s%n", position.x() * (long) 4000000 + position.y());
            } else {
                throw new IllegalStateException("cannot find answer");
            }
        }
    }
}
