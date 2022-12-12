package io.duan.advent.y2022;

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;
import java.util.function.Predicate;
import java.util.stream.Collectors;

public class Day7 {
    public static void main(String... args) throws IOException {
        var root = new Dir("/", null);
        var current = root;
        try(var reader = Files.newBufferedReader(Path.of("day7.txt"))) {
            var commandLine = reader.readLine();
            while(commandLine != null) {
                switch(commandLine.substring(2, 4)) {
                    case "cd" -> {
                        current = current.cd(commandLine.substring(5));
                        commandLine = reader.readLine();
                    }
                    case "ls" -> {
                        commandLine = buildList(reader, current);
                    }
                    default -> throw new IllegalArgumentException("unexpected command " + commandLine);
                }
            }
        }
        var total = root.getDirs(dir -> dir.getSize() < 100000).stream().map(Dir::getSize).reduce(0, Integer::sum);
        System.out.println("result " + total);
        final var neededSpace = root.getSize() - 40000000;
        var selection = root.getDirs(dir -> dir.getSize() >= neededSpace).stream().min(Comparator.comparingInt(Dir::getSize)).get();
        System.out.println("dircetory to delete " + selection.getSize());
    }

    private static String buildList(BufferedReader reader, Dir current) throws IOException {
        var nextLine = reader.readLine();
        while (nextLine != null && !nextLine.startsWith("$")) {
            if (nextLine.startsWith("dir")) {
                current.addDir(nextLine.substring(4));
            } else {
                var fileInfo = nextLine.split(" ");
                current.addFile(fileInfo[1], Integer.parseInt(fileInfo[0]));
            }
            nextLine = reader.readLine();
        }
        return nextLine;
    }
}

class Dir {
    private final String name;
    private final Dir parent;
    private final Map<String, Dir> subdirs;
    private final Map<String, Integer> files;
    private int size = -1;

    public Dir(String name, Dir parent) {
        this.name = name;
        this.parent = parent;
        this.subdirs = new HashMap<>();
        this.files = new HashMap<>();
    }

    public Dir cd(String directory) {
        return switch (directory) {
            case "/" -> root();
            case ".." -> parent;
            default -> subdirs.get(directory);
        };
    }

    private Dir root() {
        if (parent == null) return this;
        return parent.root();
    }

    public void addDir(String name) {
        subdirs.put(name, new Dir(name, this));
        this.size = -1;
    }

    public void addFile(String name, int size) {
        files.put(name, size);
        this.size = -1;
    }

    public int getSize() {
        if (this.size == -1) {
            var fileTotalSize = files.values().stream().reduce(0, Integer::sum);
            var dirTotalSize = subdirs.values().stream().map(Dir::getSize).reduce(0, Integer::sum);
            this.size = fileTotalSize + dirTotalSize;
        }
        return size;
    }

    public List<Dir> getDirs(Predicate<Dir> predicate) {
        var result = new ArrayList<Dir>();
        subdirs.values().forEach(dir -> {
            if (predicate.test(dir)) {
                result.add(dir);
            }
            result.addAll(dir.getDirs(predicate));
        });
        return result;
    }
}
