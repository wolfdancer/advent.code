package io.duan.advent.y2022;

import java.util.Scanner;
import java.util.regex.MatchResult;

public class ScannerExample {

    public static void main(String... args) {
        String wordsAndNumbers = """
                Longing rusted furnace
                daybreak 17 benign 
                9 homecoming 1 
                freight car
                benign
                """;

        try (Scanner scanner = new Scanner(wordsAndNumbers)) {
            scanner.findAll("benign").map(MatchResult::group).forEach(System.out::println);
        }
    }
}
