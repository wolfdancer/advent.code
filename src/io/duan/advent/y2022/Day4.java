package io.duan.advent.y2022;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Day4 {
    public static void main(String... args) throws IOException {
//        var re/*sult1 = Files.lines(Path.of("day4.txt")).map(Day4::fullyContains).reduce(Integer::sum).get();
//        System.out.println("answer 1: " + result1*/);
        var result2 = Files.lines(Path.of("day4.txt")).map((Day4::overlaps)).reduce(Integer::sum).get();
        System.out.println("answer 2: " + result2);
    }

    private static int fullyContains(String line) {
        var ranges = line.split(",");
        var first = parse(ranges[0]);
        var second = parse(ranges[1]);
        if (first.contains(second) || second.contains(first)) {
            return 1;
        }
        return 0;
    }

    private static int overlaps(String line) {
        var ranges = line.split(",");
        var first = parse(ranges[0]);
        var second = parse(ranges[1]);
        if (first.overlap(second)) {
            return 1;
        }
        return 0;
    }

    private static Range parse(String rangeFormat) {
        var beginEnd = rangeFormat.split("-");
        return new Range(Integer.parseInt(beginEnd[0]), Integer.parseInt(beginEnd[1]));
    }
}

record Range(int begin, int end) {
    public boolean contains(Range that) {
        return begin <= that.begin && end >= that.end;
    }

    public boolean overlap(Range that) {
        if (end < that.begin) {
            return false;
        }
        if (begin > that.end) {
            return false;
        }
        return true;
    }
}
