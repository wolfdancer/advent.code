package io.duan.advent.y2022;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.stream.IntStream;

public class Day10Part2 {
    public static void main(String... args) throws IOException {
        var sprite = new Sprite();
        try (var stream = Files.lines(Path.of("day10.txt"))) {
            stream.forEach(sprite::drawAndExecute);
        }
        sprite.print();
    }

    static class Sprite {
        private int cycle = 0;
        private int sprite = 1;
        final private StringBuilder buffer = new StringBuilder();
        public void drawAndExecute(String line) {
            var elements = line.split(" ");
            switch (elements[0]) {
                case "addx" -> {
                    draw();
                    draw();
                    this.sprite += Integer.parseInt(elements[1]);
                }
                case "noop" -> draw();
                default -> throw new IllegalArgumentException("cannot process " + line);
            }
        }

        private void draw() {
            var index = cycle % 40;
            if (index >= sprite - 1 && index <= sprite + 1) {
                buffer.append("#");
            } else {
                buffer.append(".");
            }
            cycle++;
        }

        public void print() {
            IntStream.range(0, 6).forEach(row -> {
                var start = row * 40;
                System.out.println(buffer.substring(start, start+40));
            });
        }
    }
}
