package io.duan.advent.y2022;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Day10 {
    public static void main(String... args) throws IOException {
        var cpu = new Cpu();
        var signal = new Signal();
        try (var stream = Files.lines(Path.of("day10.txt"))) {
            stream.forEach(line -> {
                var from = cpu.getCurrentCycle();
                var x = cpu.process(line);
                System.out.println(from + ":" + line + " -> " + x);
                signal.check(from, cpu.getCurrentCycle(), x);
            });
        }
        System.out.println("Total " + signal.getTotal());
    }

    static class Cpu {
        private int cycle = 1;
        private int register = 1;

        public int process(String instruction) {
            var value = this.register;
            var elements = instruction.split(" ");
            switch (elements[0]) {
                case "addx" -> {
                    this.register += Integer.parseInt(elements[1]);
                    cycle += 2;
                }
                case "noop" -> cycle += 1;
                default -> throw new IllegalArgumentException("cannot process " + instruction);
            }
            return value;
        }

        public int getCurrentCycle() {
            return this.cycle;
        }

    }

    static class Signal {
        private final int[] cycles = {20, 60, 100, 140, 180, 220};
        private int sum = 0;
        public void check(int from, int toExclusive, int register) {
            var cycle = checkRange(from, toExclusive);
            if (cycle != -1) {
                sum += cycle * register;
            }
        }

        private int checkRange(int from, int toExclusive) {
            for (int cycle : cycles) {
                if (from <= cycle) {
                    if (toExclusive > cycle) {
                        return cycle;
                    } else {
                        return -1;
                    }
                }
            }
            return -1;
        }

        public int getTotal() {
            return this.sum;
        }
    }
}
