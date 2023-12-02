use std::fs;
use std::convert::TryFrom;
use std::collections::HashMap;

fn main() {
    let instructions = fs::read_to_string("../test.txt").expect("Error");

    let mut num_sum_pt1 = 0;
    let mut num_sum_pt2 = 0;

    let num_strings: HashMap<&str, u8> = HashMap::from([
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
    ]);

    for line in instructions.split("\n") {
        if line.len() > 0 {
            num_sum_pt1 += get_first_and_last_digit_combined(&line);
            num_sum_pt2 += get_first_and_last_digit_combined_pt2(&line, &num_strings);
        }
    }

    println!("pt1: {num_sum_pt1}, pt2: {num_sum_pt2}");
}

fn get_first_and_last_digit_combined(line: &str) -> u32 {
    
    let mut digits = line.chars().filter_map(|c| c.to_digit(10));
    let first_digit = digits.next().unwrap();
    let last_digit = digits.last().unwrap_or(first_digit);

    return first_digit * 10 + last_digit;
}

fn get_first_and_last_digit_combined_pt2(line: &str, num_strings: &HashMap<&str, u8>) -> u32 {

    let mut dig_idx = [-1, -1, -1, -1, -1, -1, -1, -1, -1];

    for (str_num, num) in num_strings.into_iter() {
        let char_num = num.to_string();

        let first_idx = line.find(&char_num);
        let second_idx = line.find(&*str_num);

        let value_usize = if first_idx <= second_idx { first_idx } else { second_idx };
        let value = u32::try_from(value_usize.unwrap_or(0));
        let array_index = *num as usize;

        dig_idx[array_index] = value;
    }

    println!("{line}");
    return 1;
}

