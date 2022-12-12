package io.duan.advent.y2022;

import java.util.*;
import java.util.stream.Collectors;

import static java.util.stream.Collectors.groupingBy;

public class Experiment {
    public static void main(String... args) {
        var strings = List.of("one", "two", "three", "four");
        var map = strings.stream().collect(Collectors.groupingBy(String::length, Collectors.counting()));
        map.forEach((key, value) -> System.out.println(key + "::" + value));
    }
}
