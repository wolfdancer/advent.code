package io.duan.advent.y2022;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.HashSet;

public class Day6 {
    public static void main(String... args) throws IOException {
        var position = 0;
        var slidingWindow = new ArrayList<Character>(4);
        try (var reader = Files.newBufferedReader(Path.of("day6.txt"))) {
            var readChar = reader.read();
            while (readChar != -1) {
                position++;
                char c = (char) readChar;
                slidingWindow.add(c);
                if (slidingWindow.size() == 14) {
                    if (new HashSet<>(slidingWindow).size() == 14) {
                        break;
                    }
                    slidingWindow.remove(0);
                }
                readChar = reader.read();
            }
        }
        System.out.println("result " + position);
    }
}
