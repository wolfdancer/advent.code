package io.duan.advent.y2022;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.IntStream;

public class Day12 {
    public static void main(String... args) throws IOException {
        var map = Files.readAllLines(Path.of("day12.txt"));
        Position start = null, end = null;
        for (int i = 0; i < map.size(); i++) {
            var column = map.get(i).indexOf("S");
            if (column != -1) {
                start = new Position(i, column);
            }
            column = map.get(i).indexOf("E");
            if (column != -1) {
                end = new Position(i, column);
            }
        }
        var explorer = new Explorer(map, start, end);
        while(!explorer.explore());
        System.out.println("steps " + explorer.getSteps());
    }

    static class Explorer {
        private final List<String> map;
        private final int[][] steps;
        private final int heigh;
        private final int width;
        private int stepCount;
        private Set<Position> candidates;
        private final Position end;

        public Explorer(List<String> map, Position start, Position end) {
            this.map = map;
            this.heigh = map.size();
            this.width = map.get(0).length();
            this.steps = new int[map.size()][map.get(0).length()];
            IntStream.range(0, steps.length).forEach(row -> {
                IntStream.range(0, steps[row].length).forEach(column -> steps[row][column] = -1);
            });
            this.candidates = new HashSet<>();
            candidates.add(start);
            this.end = end;
            this.stepCount = 0;
            mark(start, 0);
        }

        private void mark(Position p, int number) {
            steps[p.row][p.column] = number;
        }

        public int getSteps() {
            return this.stepCount;
        }

        public boolean explore() {
            stepCount++;
            var nextRound = new HashSet<Position>();
            candidates.forEach(position -> {
                var height = getHeight(position);
                position.neighbors().forEach(neighbor -> {
                    if (valid(neighbor) && canReach(height, getHeight(neighbor))) {
                        mark(neighbor, stepCount);
                        nextRound.add(neighbor);
                    }
                });
            });
            candidates = nextRound;
            if (candidates.isEmpty()) {
                throw new IllegalStateException("running out of options at step " + stepCount);
            }
            return candidates.contains(end);
        }

        private boolean canReach(char from, char to) {
            if (from == 'S') from = 'a';
            if (to == 'E') to = 'z';
            return to - from <= 1;
        }

        private char getHeight(Position position) {
            return map.get(position.row).charAt(position.column);
        }

        private boolean valid(Position p) {
            return p.row >= 0 && p.row < heigh && p.column >= 0 && p.column < width
                    && steps[p.row][p.column] == -1;
        }
    }

    record Position(int row, int column) {
        public List<Position> neighbors() {
            return List.of(up(), down(), left(), right());
        }

        private Position up() {return new Position(row - 1, column);}
        private Position down() {return new Position(row + 1, column);}
        private Position left() {return new Position(row, column - 1);}
        private Position right() {return new Position(row, column + 1);}
    }
}
