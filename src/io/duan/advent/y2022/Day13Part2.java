package io.duan.advent.y2022;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Day13Part2 {
    public static void main(String... args) throws IOException {
        var dividerStream = List.of("[[2]]", "[[6]]").stream();
        var packets = Stream.concat(Files.lines(Path.of("day13.txt")), dividerStream)
                .filter(Predicate.not(String::isBlank))
                .map(Day13.Packet::parse)
                .sorted(Day13.Packet::compareToPacket)
                .toList();
        var answer = IntStream.range(1, packets.size() + 1)
                .filter(index -> packets.get(index - 1).isDivider())
                .reduce(1, Math::multiplyExact);
        System.out.printf("decoder key %s%n", answer);
    }
}
