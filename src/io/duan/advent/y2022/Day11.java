package io.duan.advent.y2022;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Day11 {
    public static void main(String... args) throws IOException {
        var monkeys = new ArrayList<Monkey>();
        var items = new ArrayList<Item>();
        try (var reader = Files.newBufferedReader(Path.of("day11.txt"))) {
            String line;
            do {
                var monkeyLine = reader.readLine();
                var startItems = reader.readLine();
                var operationLine = reader.readLine();
                var testLine = reader.readLine();
                var trueLine = reader.readLine();
                var falseLine = reader.readLine();
                var monkey = Monkey.parse(monkeyLine, startItems, operationLine, testLine, trueLine, falseLine);
                if (monkey.getNumber() != monkeys.size()) {
                    throw new IllegalStateException("expected monkey " + monkeys.size() + " but got " + monkey.getNumber());
                }
                monkeys.add(monkey);
                items.addAll(monkey.getItems());
                line = reader.readLine();
            } while (line != null);
        }
        items.forEach(item -> monkeys.forEach(item::registerMonkey));
        IntStream.range(0, 10000).forEach(round -> {
            monkeys.forEach(monkey -> {
                monkey.takeTurn(monkeys);
            });
            System.out.println(round + ":" + monkeys);
        });
        monkeys.sort(Collections.reverseOrder(Comparator.comparingLong(Monkey::getInspectionsCount)));
        System.out.println("monkey business " + monkeys.get(0).getInspectionsCount() * monkeys.get(1).getInspectionsCount());
    }

    static class Monkey {
        private long inspectionsCount;
        private int number;
        private List<Item> items;
        private Operation operation;
        private int divisor;
        private int trueTarget, falseTarget;

        public static Monkey parse(String monkeyLine, String startItems, String operationLine, String testLine, String trueLine, String falseLine) {
            var monkey = new Monkey();
            monkey.number = parseMonkeyLine(monkeyLine);
            monkey.items = parseStartItems(startItems);
            monkey.operation = parseOperation(operationLine);
            monkey.divisor = parseTest(testLine);
            monkey.trueTarget = parseIfLine(true, trueLine);
            monkey.falseTarget = parseIfLine(false, falseLine);
            return monkey;
        }

        private static int parseMonkeyLine(String monkeyLine) {
            var space = monkeyLine.indexOf(" ");
            var colon = monkeyLine.indexOf(":");
            return Integer.parseInt(monkeyLine.substring(space+1, colon));
        }

        private static List<Item> parseStartItems(String startItems) {
            var start = startItems.indexOf(":") + 1;
            return Arrays.stream(startItems.substring(start).split(","))
                    .map(String::strip)
                    .map(Integer::parseInt)
                    .map(Item::new)
                    .collect(Collectors.toList());
        }

        private static Operation parseOperation(String operationLine) {
            var start = operationLine.indexOf("=") + 2;
            var tokens = operationLine.substring(start).split(" ");
            Integer left = parseOperand(tokens[0]);
            Integer right = parseOperand(tokens[2]);
            return new Operation(tokens[1], left, right);
        }

        private static Integer parseOperand(String string) {
            return "old".equals(string) ? null : Integer.valueOf(string);
        }

        private static int parseTest(String testLine) {
            var token = "divisible by ";
            var index = testLine.indexOf(token) + token.length();
            return Integer.parseInt(testLine.substring(index));
        }

        private static int parseIfLine(boolean expected, String line) {
            var indexIf = line.indexOf("If ");
            var indexColon = line.indexOf(":");
            var indexMonkey = line.indexOf("monkey ");
            var condition = Boolean.parseBoolean(line.substring(indexIf + 3, indexColon));
            if (condition != expected) {
                throw new IllegalArgumentException("expected condition to be " + expected);
            }
            return Integer.parseInt(line.substring(indexMonkey + 7));
        }

        public long getInspectionsCount() {
            return inspectionsCount;
        }

        public void takeTurn(ArrayList<Monkey> monkeys) {
            this.items.forEach(item -> {
/* part one solution for low worry levels
                var value = this.operation.calculate(item.getWorryLevel());
                value = value / 3;
                var target = value % divisionTestBy == 0 ? trueTarget : falseTarget;
                monkeys.get(target).items.add(new Item(value));
*/
                item.calculateWorryLevel(this.operation);
                var target = item.isDivisibleBy(divisor) ? trueTarget : falseTarget;
                monkeys.get(target).items.add(item);
            });
            this.inspectionsCount += this.items.size();
            this.items.clear();
        }

        public int getNumber() {
            return number;
        }

        public String toString() {
            return String.valueOf(inspectionsCount);
        }

        public List<Item> getItems() {
            return items;
        }

        public int getDivisor() {
            return this.divisor;
        }
    }

    record Operation (String operand, Integer left, Integer right) {

        public int calculate(int value) {
            int leftValue = this.left == null ? value : this.left;
            int rightValue = this.right == null ? value : right;
            return calculate(leftValue, rightValue);
        }

        private int calculate(int left, int right) {
            return switch(operand) {
                case "+" -> left + right;
                case "*" -> left * right;
                default -> throw new IllegalStateException("unexpected " + operand);
            };
        }

    }

    static class Item {
        private final int initialWorryLevel;
        private final Map<Integer, Integer> worryLevelResidue = new HashMap<>();

        public Item(int worryLevel) {
            this.initialWorryLevel = worryLevel;
        }

        public int getInitialWorryLevel() {
            return initialWorryLevel;
        }

        public void registerMonkey(Monkey monkey) {
            var divisor = monkey.getDivisor();
            worryLevelResidue.put(divisor, initialWorryLevel % divisor);
        }

        public void calculateWorryLevel(Operation operation) {
            worryLevelResidue.forEach((key, value) -> {
                var newValue = operation.calculate(value) % key;
                worryLevelResidue.put(key, newValue);
            });
        }

        public boolean isDivisibleBy(int divisor) {
            return worryLevelResidue.get(divisor) == 0;
        }
    }
}
