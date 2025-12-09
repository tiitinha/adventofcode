use regex::Regex;
use std::fs::read_to_string;

fn main() {
    let re = Regex::new(r"\d+").unwrap();
    let re_op = Regex::new(r"\+|\*").unwrap();

    let binding: String = read_to_string("../../input.txt").expect("File not found");
    let contents: Vec<&str> = binding.split("\n").collect();

    let contents_len = contents.len();
    let numbers_raw = &contents[..contents_len - 1];
    let operators_raw = &contents[contents_len - 2];
    let mut numbers: Vec<Vec<u32>> = Vec::new();
    let operators: Vec<&str> = re_op
        .find_iter(operators_raw)
        .map(|ops| ops.as_str())
        .collect();

    for line in numbers_raw {
        let num_row = re
            .find_iter(line)
            .filter_map(|digits| digits.as_str().parse::<u32>().ok())
            .collect::<Vec<u32>>();

        numbers.push(num_row);
    }
}
