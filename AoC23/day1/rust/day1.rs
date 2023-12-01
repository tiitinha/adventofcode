use std::fs;
use std::convert::TryInto;
use std::collections::HashMap;

fn main() {
    let instructions = fs::read_to_string("../test.txt").expect("Error");

    let mut num_sum = 0;

    let num_strings: HashMap<&str, i32> = HashMap::from([
        ("one", 0),
        ("two", 1),
        ("three", 2),
        ("four", 3),
        ("five", 4),
        ("six", 5),
        ("seven", 6),
        ("eight", 7),
        ("nine", 8),
    ]);

    for line in instructions.split("\n") {
        if line.len() > 0 {
            num_sum += get_first_and_last_digit_combined(line.to_string(), num_strings.clone());
        }
    }

    println!("{}", num_sum);
}

fn get_first_and_last_digit_combined(line: String, num_strings: HashMap<&str, i32>) -> i32 {
    let mut first_digit = -1;
    let mut last_digit = -1;

    let new_line = replace_num_strings_in_line(&line, num_strings);

    println!("{}", new_line);

    for c in new_line.chars() {
        if c.is_digit(10) {
            let number: i32 = c.to_digit(10).unwrap_or(0).try_into().unwrap();
            if first_digit == -1 {
                first_digit = number;
            }
            last_digit = number;
        }
    }

    let final_number = format!("{}{}", first_digit, last_digit).parse::<i32>().unwrap();
    return final_number;
}

fn replace_num_strings_in_line<'a>(line: &'a str, num_strings: HashMap<&str, i32>) -> String {
    let mut result_string: String = line.to_string();
    let mut res: String;
    for (key, value) in num_strings.into_iter() {
        res = result_string.replace(key, &value.to_string());
        result_string = res.to_string();
    }

    return result_string;
}
