package io.duan.advent.y2022;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;
import java.util.function.Predicate;

public class Day14 {
    public static void main(String... args) throws IOException {
        final var map = new CaveMap();
        try (final var stream = Files.lines(Path.of("day14.txt"))) {
            stream.forEach(map::process);
        }
        var units = 0;
//        while (map.dropSand(500, 0)) {
        while (map.dropSandWithFloor(500, 0)) {
            units++;
        }
        System.out.printf("Units of sand needed %d%n", units);
    }

    static class CaveMap {
        final Map<Integer, List<Line>> horizonals;
        final Map<Integer, List<Line>> verticals;
        final Set<Position> sand;
        int bottomRow;

        public CaveMap() {
            horizonals = new HashMap<>();
            verticals = new HashMap<>();
            sand = new HashSet<>();
            bottomRow = Integer.MIN_VALUE;
        }

        public void process(String line) {
            final var points = Arrays.stream(line.split("->"))
                    .map(Position::parse)
                    .toList();
            for (int i = 1; i < points.size(); i++) {
                register(points.get(i - 1), points.get(i));
            }
        }

        private void register(Position from, Position to) {
            updateBottomRow(from);
            updateBottomRow(to);
            if (from.sameRowAs(to)) {
                registerLine(this.horizonals, from.y, from.x, to.x);
            } else if (from.sameColumnAs(to)) {
                registerLine(this.verticals, from.x, from.y, to.y);
            } else {
                throw new IllegalStateException("Not on horizontal or vertical line %s --> %s".formatted(from, to));
            }
        }

        private void updateBottomRow(Position p) {
            if (this.bottomRow < p.y) {
                this.bottomRow = p.y;
            }
        }

        private void registerLine(Map<Integer, List<Line>> map, int primary, int secondaryStart, int secondaryStop) {
            if (secondaryStart > secondaryStop) {
                final var swap = secondaryStart;
                secondaryStart = secondaryStop;
                secondaryStop = swap;
            }
            var list = map.computeIfAbsent(primary, k -> new ArrayList<>());
            list.add(new Line(primary, secondaryStart, secondaryStop));
        }

        public boolean dropSand(int x, int y) {
            return dropSand(new Position(x, y));
        }

        private boolean dropSand(Position position) {
            if (position.y > bottomRow) {
                return false;
            }
            var landing = position.options().stream()
                    .filter(Predicate.not(this::isOccupied))
                    .findFirst();
            if (landing.isPresent()) {
                return dropSand(landing.get());
            } else {
                sand.add(position);
                return true;
            }
        }

        public boolean dropSandWithFloor(int x, int y) {
            Position position = new Position(x, y);
            if (this.sand.contains(position)) {
                return false;
            }
            return dropSandWithFloor(position);
        }

        private boolean dropSandWithFloor(Position position) {
            if (position.y < bottomRow + 1) {
                var landing = position.options().stream()
                        .filter(Predicate.not(this::isOccupied))
                        .findFirst();
                if (landing.isPresent()) {
                    return dropSandWithFloor(landing.get());
                }
            }
            sand.add(position);
            return true;
        }

        private boolean isOccupied(Position position) {
            return sand.contains(position) || checkRow(position) || checkColumn(position);
        }

        private boolean checkRow(Position position) {
            return horizonals.computeIfAbsent(position.y, k -> Collections.emptyList()).stream()
                    .anyMatch(line -> position.x >= line.start && position.x <= line.end);
        }

        private boolean checkColumn(Position position) {
            return verticals.computeIfAbsent(position.x, k -> Collections.emptyList()).stream()
                    .anyMatch(line -> position.y >= line.start && position.y <= line.end);
        }
    }

    record Line(int primary, int start, int end) {
    }

    record Position(int x, int y) {
        public static Position parse(String pair) {
            final var values = Arrays.stream(pair.strip().split(","))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            return new Position(values[0], values[1]);
        }

        public boolean sameRowAs(Position that) {
            return this.y == that.y;
        }

        public boolean sameColumnAs(Position that) {
            return this.x == that.x;
        }

        public List<Position> options() {
            return List.of(down(), downLeft(), downRight());
        }

        public Position down() {
            return new Position(x, y + 1);
        }

        public Position downLeft() {
            return new Position(x - 1, y + 1);
        }

        public Position downRight() {
            return new Position(x + 1, y + 1);
        }
    }
}
