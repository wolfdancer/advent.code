package io.duan.advent.y2022;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Day5 {
    public static void main(String... args) throws IOException {
        var stacks = new ArrayList<Deque<Character>>();
        try (var reader = Files.newBufferedReader(Path.of("day5.txt"))) {
            var line = reader.readLine();
            while (line.startsWith("[")) {
                checkStackSize(stacks, (line.length() + 1) / 4);
                parseStacks(stacks, line);
                line = reader.readLine();
            }
            printStackStats(stacks);
            reader.readLine();
            line = reader.readLine();
            while (line != null) {
                move(stacks, line);
                line = reader.readLine();
            }
        }
        var result  = stacks.stream().map(Deque::peekFirst)
                .map(Object::toString)
                .collect(Collectors.joining());
        System.out.println(result);
    }

    private static void printStackStats(List<Deque<Character>> stacks) {
        stacks.stream().map(Deque::size).forEach(item -> System.out.print("[" + item + "]"));
        System.out.println();
    }

    private static void checkStackSize(List<Deque<Character>> stacks, int size) {
        if (stacks.size() < size) {
            for (int i = stacks.size(); i < size; i++) {
                stacks.add(new LinkedList<>());
            }
        }
    }

    private static void parseStacks(List<Deque<Character>> stacks, String line) {
        IntStream.range(0, stacks.size())
                .forEach(index -> {
                    char crate = line.charAt(index * 4 + 1);
                    if (!Character.isWhitespace(crate)) {
                        stacks.get(index).addLast(crate);
                    }
                });
    }

    private static void move(List<Deque<Character>> stacks, String line) {
        System.out.println(line);
        var fromIndex = line.indexOf("from");
        var toIndex = line.indexOf("to");
        var numberOfCrates = Integer.parseInt(line.substring(5, fromIndex - 1));
        var fromStackIndex = Integer.parseInt(line.substring(fromIndex + 5, toIndex - 1)) - 1;
        var toStackIndex = Integer.parseInt(line.substring(toIndex + 3)) - 1;
        var fromStack = stacks.get(fromStackIndex);
        var toStack = stacks.get(toStackIndex);
        //IntStream.range(0, numberOfCrates).forEach(index -> toStack.addFirst(fromStack.removeFirst()));
        var list = new LinkedList<Character>();
        IntStream.range(0, numberOfCrates).forEach(index -> list.addFirst(fromStack.removeFirst()));
        list.forEach(item -> toStack.addFirst(item));
        printStackStats(stacks);
    }
}
