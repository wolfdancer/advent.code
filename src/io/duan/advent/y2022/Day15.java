package io.duan.advent.y2022;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Objects;

public class Day15 {
    public static void main(String... args) throws IOException {
        var sensors = new ArrayList<Sensor>();
        var beaconPositions = new HashSet<Position>();
        try(var stream = Files.lines(Path.of("day15.txt"))) {
            stream.forEach(line -> {
                Sensor sensor = parse(line);
                beaconPositions.add(sensor.getBeacon());
                sensors.add(sensor);
            });
        }
        final var y = 3289729;
        final var coverage = new Coverage(y, sensors);
        System.out.println(coverage);
        var beaconsInCoverage = beaconPositions.stream()
                .filter(coverage::doesCover)
                        .count();
        System.out.printf("positions %d%n", coverage.getCoveredPositions() - beaconsInCoverage);
    }

    public static Sensor parse(String line) {
        final var sensorStart = line.indexOf("x");
        final var sensorEnd = line.indexOf(":");
        final var beaconStart = line.lastIndexOf("x");
        final var sensorPosition = Position.parse(line.substring(sensorStart, sensorEnd));
        final var beaconPosition = Position.parse(line.substring(beaconStart));
        return new Sensor(sensorPosition, beaconPosition);
    }

    static class Coverage {
        private final int y;
        private final List<Range> ranges;

        public Coverage(int y, List<Sensor> sensors) {
            this.y = y;
            this.ranges = new ArrayList<>();
            sensors.stream()
                    .map(sensor -> sensor.coveredRange(y))
                    .filter(Objects::nonNull)
                    .sorted()
                    .forEach(this::add);
        }

        private void add(Range range) {
            if (ranges.isEmpty()) {
                ranges.add(range);
            } else {
                var lastOne = ranges.get(ranges.size() - 1);
                if (lastOne.overlap(range)) {
                    ranges.set(ranges.size() - 1, lastOne.merge(range));
                } else {
                    ranges.add(range);
                }
            }
        }

        public String toString() {
            return this.ranges.toString();
        }

        public int getCoveredPositions() {
            return this.ranges.stream()
                    .mapToInt(Range::length)
                    .sum();
        }

        public boolean doesCover(Position position) {
            if (position.y != y) {
                return false;
            }
            return ranges.stream()
                    .anyMatch(range -> range.cover(position.x));
        }

        public Position findUncovered(int min, int max) {
            var find = this.ranges.stream()
                    .filter(range -> range.max >= min && range.min <= max)
                    .map(range -> {
                        if (range.min > min) return new Position(range.min - 1, y);
                        else if (range.max < max) return new Position(range.max + 1, y);
                        else return null;
                    })
                    .filter(Objects::nonNull)
                    .findFirst();
            return find.orElse(null);
        }
    }

    static class Sensor {
        private final Position position;
        private final Position beacon;

        public Sensor(Position position, Position beacon) {
            this.position = position;
            this.beacon = beacon;
        }

        public String toString() {
            return "%s locked on %s".formatted(position, beacon);
        }

        public Range coveredRange(int y) {
            final var distance = position.distanceFrom(beacon);
            final var deltaY = Math.abs(position.y() - y);
            final var deltaX = distance - deltaY;
            if (deltaX < 0) {
                return null;
            }
            return new Range(this.position.x() - deltaX, this.position.x() + deltaX);
        }

        public Position getBeacon() {
            return this.beacon;
        }
    }

    record Position(int x, int y){
        public static Position parse(String coordinate) {
            final var xStart = coordinate.indexOf("x=");
            final var xEnd = coordinate.indexOf(",");
            final var yStart = coordinate.indexOf("y=");
            return new Position(Integer.parseInt(coordinate.substring(xStart+2, xEnd)),
                    Integer.parseInt(coordinate.substring(yStart+2)));
        }

        public int distanceFrom(Position that) {
            return Math.abs(this.x - that.x) + Math.abs(this.y - that.y);
        }
    }

    record Range(int min, int max) implements Comparable<Range> {
        @Override
        public int compareTo(Range that) {
            final var minCompare = Integer.compare(this.min, that.min);
            return minCompare != 0 ? minCompare : Integer.compare(this.max, that.max);
        }

        public boolean overlap(Range that) {
            return this.max >= that.min && this.min <= that.max;
        }

        public Range merge(Range that) {
            return new Range(
                    Math.min(this.min, that.min),
                    Math.max(this.max, that.max)
            );
        }

        public int length() {
            return this.max - this.min + 1;
        }

        public boolean cover(int x) {
            return this.min <= x && this.max >= x;
        }
    }
}
