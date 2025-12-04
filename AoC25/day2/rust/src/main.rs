use std::fs::read_to_string;

fn check_if_even_amt_of_digits(value: i32) -> bool {
    let num_of_digits = value.checked_ilog10().unwrap_or(0) + 1;

    if num_of_digits % 2 == 0 {
        return true;
    }

    return false;
}

fn viable_password(min_val: i32, max_val: i32) -> i32 {
    let mut value_sum = 0;

    for value in min_val..=max_val {
        if !check_if_even_amt_of_digits(value) {
            continue;
        }

        let value_string = value.to_string();
        let midpoint = value_string.chars().count() / 2;
        let first_half = &value_string[..midpoint];
        let second_half = &value_string[midpoint..];

        if first_half == second_half {
            value_sum += value;
        }
    }

    return value_sum;
}

fn main() {
    let file = read_to_string("../../test.txt").expect("Should've been able to read the file");

    let binding = file.replace("\n", "");
    let contents = binding.split(",");

    let mut result = 0;

    for pair in contents {
        let bounds: Vec<&str> = pair.split("-").collect();

        let min_val = bounds[0].parse::<i32>().unwrap();
        let max_val = bounds[1].parse::<i32>().unwrap();

        result += viable_password(min_val, max_val);
    }

    println!("{result}")
}
