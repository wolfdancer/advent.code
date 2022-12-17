package io.duan.advent.y2022;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.IntStream;

public class Day9 {
    public static void main(String... args) throws IOException {
        var start = new Position(0, 0);
        var visitor = new Visitor(start);
        try(var stream = Files.lines(Path.of("day9.txt"))) {
            stream.forEach(visitor::move);
        }
        System.out.println("visited " + visitor.getVisited().size());
    }

    static class Visitor {
        private final Set<Position> visited = new HashSet<>();
        private Position head;
        private final Position[] tail;

        public Visitor(Position start) {
            this.head = start;
            this.tail = new Position[9];
            IntStream.range(0, 9).forEach(i -> tail[i] = head);
            visited.add(tail[8]);
        }

        public void move(String line) {
            var command = line.split(" ");
            var direction = command[0];
            var count = Integer.parseInt(command[1]);
            IntStream.range(0, count).forEach(step -> {
                head = head.step(direction);
                tail[0] = tail[0].follow(head);
                IntStream.range(1, 9).forEach(i -> tail[i] = tail[i].follow(tail[i-1]));
                visited.add(tail[8]);
            });
        }

        public Set<Position> getVisited() {
            return this.visited;
        }
    }
    record Position(int x, int y){
        public Position step(String direction) {
            var nextX = x;
            var nextY = y;
            switch(direction) {
                case "U" -> nextY++;
                case "D" -> nextY--;
                case "L" -> nextX--;
                case "R" -> nextX++;
                default -> throw new IllegalArgumentException("cannot understand direction:" + direction);
            }
            return new Position(nextX, nextY);
        }

        public Position follow(Position head) {
            var deltaX = head.x - this.x;
            var deltaY = head.y - this.y;
            var nextX = this.x;
            var nextY = this.y;
            if (deltaX > 1) {
                nextX ++;
                nextY += Integer.compare(deltaY, 0);
            } else if (deltaX < -1) {
                nextX --;
                nextY += Integer.compare(deltaY, 0);
            } else if (deltaY > 1) {
                nextY ++;
                nextX += Integer.compare(deltaX, 0);
            } else if (deltaY < -1) {
                nextY --;
                nextX += Integer.compare(deltaX, 0);
            }
            return new Position(nextX, nextY);
        }

    }
}

