use std::fs;

fn main() {
    let contents = fs::read_to_string("../input.txt").expect("To be a string");
    let rows_raw = contents.split("\n");
    let mut rows = Vec::new();

    for row in rows_raw {
        let values = row.split_whitespace();
        let mut row_values = Vec::new();

        for value in values {
            row_values.push(value.parse::<i32>().unwrap());
        }

        rows.push(row_values);
    }

    let mut count: i32 = 0;

    for row in rows {
        if row.len() > 0 {
            let safe: bool = check_if_rule_safe(row);
            if safe {
                count += 1;
            }
        }
    }

    println!("{}", count);
}

fn check_if_rule_safe(row: Vec<i32>) -> bool {
    let mut previous = row[0];
    let mut previous_diff = 0;

    let vec_length = row.len();

    for n in 1..vec_length {
        let current_val = row[n];
        let diff = current_val - previous;

        if diff.abs() < 1 || diff.abs() > 3 {
            return false;
        }

        if previous_diff * diff < 0 {
            return false;
        }
        
        previous = current_val;
        previous_diff = diff;
    }

    return true;
}
