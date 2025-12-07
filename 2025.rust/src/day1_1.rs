use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let file = File::open("../2025/day1.txt").expect("Unable to open file");
    let reader = BufReader::new(file);

    let mut dial = 50;
    let mut password = 0;

    for line in reader.lines() {
        let line = line.expect("Unable to read line");
        let line = line.trim();

        if line.is_empty() {
            continue;
        }

        // Get the first character as direction
        let direction = line.chars().next().expect("Empty line");

        // Get the rest as clicks
        let clicks_str = &line[1..];
        let mut clicks: i32 = clicks_str.parse().expect("Invalid number");

        // Mod clicks by 100
        clicks = clicks % 100;

        // Process based on direction
        match direction {
            'L' => dial -= clicks,
            'R' => dial += clicks,
            _ => {
                eprintln!("Error: Invalid direction in line: {}", line);
                std::process::exit(1);
            }
        }

        // Handle negative dial
        if dial < 0 {
            dial += 100;
        }

        // Handle dial >= 100
        if dial >= 100 {
            dial -= 100;
        }

        // Check if dial is 0
        if dial == 0 {
            password += 1;
        }
    }

    println!("{}", password);
}
