use std::fs::read_to_string;

fn main() {
    let binding = read_to_string("../../input.txt").expect("To have a file");
    let input: Vec<&str> = binding.split("\n\n").collect();

    let mut fresh: Vec<(u64, u64)> = Vec::new();
    let mut available: Vec<u64> = Vec::new();

    for line in input[0].split('\n') {
        if !line.is_empty() {
            let (first_str, second_str) = line.split_once('-').expect("Incorrect format");
            let min_val = first_str.parse().expect("Not a number");
            let max_val = second_str.parse().expect("Not a number");

            fresh.push((min_val, max_val));
        }
    }

    for line in input[1].split('\n') {
        if !line.is_empty() {
            let value = line.parse().expect("Not a number");
            available.push(value);
        }
    }

    let mut fresh_count = 0;

    for ingredient in available {
        for (low, high) in &fresh {
            if *low <= ingredient && *high >= ingredient {
                fresh_count += 1;
                break;
            }
        }
    }

    println!("{fresh_count}");
}
