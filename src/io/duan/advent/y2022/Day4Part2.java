package io.duan.advent.y2022;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Day4Part2 {
    public static void main(String... args) throws IOException {
        try(var stream = Files.lines(Path.of("day4.txt"))) {
            var result2 = stream.mapToInt((Day4::overlaps)).reduce(0, Integer::sum);
            System.out.println("answer 2: " + result2);
        }
    }
}
