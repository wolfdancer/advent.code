package io.duan.advent.y2022;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.stream.Collectors;

public class Day3Part2 {
    public static void main(String... args) throws IOException {
        try(var stream = Files.lines(Path.of("day3.1.txt"))) {
            var charsList = stream.map(String::chars).toList();
            var sum = 0;
            for (int i = 0; i < charsList.size(); i += 3) {
                var first = charsList.get(i).mapToObj(e -> (char) e).collect(Collectors.toSet());
                var second = charsList.get(i + 1)
                        .mapToObj(e -> (char) e)
                        .filter(first::contains)
                        .collect(Collectors.toSet());
                var third = charsList.get(i + 2)
                        .mapToObj(e -> (char) e)
                        .filter(second::contains)
                        .collect(Collectors.toSet());
                if (third.size() != 1) {
                    throw new IllegalStateException("expected 1 item only: " + first);
                }
                sum += Day3.priority(third.iterator().next());
            }

            System.out.println("sum = " + sum);
        }
    }
}
