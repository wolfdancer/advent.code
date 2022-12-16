package io.duan.advent.y2022;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

public class Day13 {
    public static void main(String... args) throws IOException {
        try(var reader = Files.newBufferedReader(Path.of("day13.txt"))) {
            var index = 1;
            var sum = 0;
            String line;
            do {
                final var first = reader.readLine();
                final var packet1 = Packet.parse(first);
                final var second = reader.readLine();
                final var packet2 = Packet.parse(second);
                switch (packet1.compareTo(packet2)) {
                    case -1 -> sum += index;
                    case 0 -> throw new IllegalStateException("same between '%s' and '%s'".formatted(first, second));
                    case 1 -> {}
                    default -> throw new IllegalStateException();
                }
                index++;
                line = reader.readLine();
            } while(line != null);
            System.out.println("number of pairs with right order " + sum);
        }
    }

    interface Item extends Comparable<Item> {
    }

    final static class Packet implements Item {
        private final List<Item> list;

        public Packet() {
            this.list = new ArrayList<>();
        }
        public static Packet parse(String line) {
            return parse(new Lexer(line));
        }

        public static Packet from(NumberItem item) {
            final var p = new Packet();
            p.list.add(item);
            return p;
        }

        private static Packet parse(Lexer lexer) {
            if (lexer.current() != TokenType.OPEN) {
                throw new IllegalStateException("expected [ but got " + lexer.current());
            }
            var packet = new Packet();
            var next = lexer.next();
            while (next != TokenType.CLOSE) {
                switch (next) {
                    case OPEN -> packet.list.add(parse(lexer));
                    case NUMBER -> packet.list.add(lexer.getNumber());
                    default -> throw new IllegalStateException(lexer.toString());
                }
                next = lexer.next();
                if (next == TokenType.COMMA) {
                    next = lexer.next();
                }
            }
            return packet;
        }

        public int compareToPacket(Packet that) {
            var result = Integer.compare(this.list.size(), that.list.size());
            final var end = Math.min(this.list.size(), that.list.size());
            var compareResult = IntStream.range(0, end)
                    .map(index -> this.list.get(index).compareTo(that.list.get(index)))
                    .filter(value -> value != 0)
                    .findFirst();
            return compareResult.orElse(result);
        }

        public int compareToNumber(NumberItem thatNumber) {
            return compareToPacket(Packet.from(thatNumber));
        }

        @Override
        public int compareTo(Item that) {
            return switch(that) {
                case Packet thatPacket -> this.compareToPacket(thatPacket);
                case NumberItem thatNumber -> this.compareToNumber(thatNumber);
                default -> throw new IllegalStateException("Unexpected value: " + that);
            };
        }
    }

    static class Lexer {
        private final String line;
        private int index;
        private TokenType currentTokenType;
        private NumberItem number;

        public Lexer(String line) {
            this.line = line;
            this.index = 0;
            next();
        }

        public TokenType current() {
            return currentTokenType;
        }

        public TokenType next() {
            this.number = null;
            var c = line.charAt(index);
            var end = index + 1;
            switch (c) {
                case '[' -> this.currentTokenType = TokenType.OPEN;
                case ']' -> this.currentTokenType = TokenType.CLOSE;
                case ',' -> this.currentTokenType = TokenType.COMMA;
                default -> {
                    if (!Character.isDigit(c)) {
                        throw new IllegalArgumentException("cannot process char at index " + index + " in " + line);
                    }
                    end = index;
                    while (Character.isDigit(line.charAt(end))) {
                        end ++;
                    }
                    this.currentTokenType = TokenType.NUMBER;
                    this.number = new NumberItem(Integer.parseInt(line.substring(index, end)));
                }
            }
            this.index = end;
            return current();
        }

        public NumberItem getNumber() {
            return number;
        }

        public String toString() {
            return "index %d at %s with %s".formatted(index, line, currentTokenType);
        }
    }

     record NumberItem(int number) implements Item {
        @Override
        public int compareTo(Item that) {
            return switch(that) {
                case NumberItem thatNumber -> Integer.compare(this.number, thatNumber.number);
                case Packet thatPacket -> - thatPacket.compareTo(this);
                default -> throw new IllegalStateException("Unexpected value: " + that);
            };
        }
     }

    enum TokenType {
        OPEN, CLOSE, COMMA, NUMBER
    }
}
