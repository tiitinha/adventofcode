use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;


fn main() {

    let file = File::open("input.txt").expect("File not found");
    let reader = BufReader::new(file);

    let mut lines = Vec::new();
    for line in reader.lines() {
        let parsed_num: i32 = line.expect("Reading a line to be parsed").parse().unwrap();
        lines.push(parsed_num);
    }

    let part_1_result = part_1(lines.clone());

    println!("Part 1: {}", part_1_result);

    let part_2_result = part_2(lines.clone());

    println!("Part 2: {}", part_2_result);
}

fn part_1(lines: Vec<i32>) -> i32 {

    let mut sum = 0;
    for line in lines {
        sum += (line / 3) - 2;
    }

    return sum;
}

fn part_2(lines: Vec<i32>) -> i32 {
    let mut sum = 0;

    for line in lines {
        let mut fuel_weight = (line / 3) - 2;

        while fuel_weight > 0 {
            sum += fuel_weight;
            fuel_weight = (fuel_weight / 3) - 2;
        }
    }

    return sum;
}