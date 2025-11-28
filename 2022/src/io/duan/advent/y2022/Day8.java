package io.duan.advent.y2022;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.IntStream;

public class Day8 {
    public static void main(String... args) throws IOException {
        try(var stream = Files.lines(Path.of("day8.txt"))) {
            var forest = stream.toList();
            var height = forest.size();
            var width = forest.get(0).length();
            var heightMap = new int[height][width];
            IntStream.range(0, height).forEach(row -> {
                IntStream.range(0, width).forEach(column -> {
                    heightMap[row][column] = forest.get(row).charAt(column) - '0';
                    System.out.print(heightMap[row][column]);
                });
                System.out.println();
            });
            //survey(height, width, heightMap);
            var evaluator = new Evaluator(heightMap);
            IntStream.range(0, height).forEach(row -> IntStream.range(0, width).forEach(column -> evaluator.evaluate(row, column)));
            System.out.println("best property: " + evaluator.getMaxValue());
        }
    }

    private static void survey(int height, int width, int[][] heightMap) {
        var surveyer = new Surveyer(heightMap);
        IntStream.range(0, height).forEach(row -> {
            surveyer.reset();
            IntStream.range(0, width)
                    .forEach(column -> surveyer.check(row, column));
            surveyer.reset();
            IntStream.range(0, width)
                    .map(column -> width - 1 - column)
                    .forEach(column -> surveyer.check(row, column));
        });
        IntStream.range(0, width).forEach(column -> {
            surveyer.reset();
            IntStream.range(0, height).forEach(row -> surveyer.check(row, column));
            surveyer.reset();
            IntStream.range(0, height)
                    .map(row -> height - 1 - row)
                    .forEach(row -> surveyer.check(row, column));
        });
        System.out.println(surveyer.getPositions().size());
    }
}

class Evaluator {

    private final int[][] heightMap;
    private int max = -1;

    public Evaluator(int[][] heightMap) {
        this.heightMap = heightMap;
    }

    public int getMaxValue() {
        return max;
    }

    public void evaluate(int row, int column) {
        var height = heightMap.length;
        var width = heightMap[0].length;
        var value = 1;
        if (row == 0 || column == 0 || row == height - 1 || column == width - 1) {
            value = 0;
        } else {
            value = up(row, column) * down(row, column) * left(row, column) * right(row, column);
        }
        if (max < value) {
            max = value;
        }
    }

    private int up(int row, int column) {
        var height = this.heightMap[row][column];
        var count = 0;
        for (int r = row - 1; r >= 0; r--) {
            count ++;
            if (this.heightMap[r][column] >= height) {
                break;
            }
        }
        return count;
    }

    private int down(int row, int column) {
        var height = this.heightMap[row][column];
        var count = 0;
        for (int r = row + 1; r < this.heightMap.length; r++) {
            count++;
            if (this.heightMap[r][column] >= height) {
                break;
            }
        }
        return count;
    }

    private int left(int row, int column) {
        var height = this.heightMap[row][column];
        var count = 0;
        for (int c = column - 1; c >= 0; c--) {
            count++;
            if (this.heightMap[row][c] >= height) {
                break;
            }
        }
        return count;
    }

    private int right(int row, int column) {
        var height = this.heightMap[row][column];
        var count = 0;
        var maxWidth = this.heightMap[0].length;
        for (int c = column + 1; c < maxWidth; c++) {
            count++;
            if (this.heightMap[row][c] >= height) {
                break;
            }
        }
        return count;
    }
}

class Surveyer {

    private int maxHeight;
    private final int[][] heightMap;
    private final Set<Position> positions = new HashSet<>();

    public Surveyer(int[][] heightMap) {
        this.heightMap = heightMap;
    }

    public void reset() {
        this.maxHeight = -1;
    }

    public void check(int row, int column) {
        var current = heightMap[row][column];
        if (current > maxHeight) {
            positions.add(new Position(row, column));
            maxHeight = current;
        }
    }

    public Set<Position> getPositions() {
        return this.positions;
    }
    record Position(int row, int column){}
}

