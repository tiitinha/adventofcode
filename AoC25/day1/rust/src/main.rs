use std::fs::read_to_string;
use std::fs::File;
use std::io::{BufWriter, Write};
use std::path::Path;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut zero_count = 0;
    let mut zero_count_2 = 0;
    let mut val = 50;

    let output_file_path = Path::new("output.txt");
    let file = File::create(output_file_path)?;
    let mut writer = BufWriter::new(file);

    for line in read_to_string("../../input.txt").unwrap().lines() {
        let direction = &line[..1];
        let dir_val: i32 =
            direction.chars().next().expect("string is empty") as i32 - 'R' as i32 + 1;
        let dir_sign = dir_val.signum();
        let clicks = &line[1..].parse::<i32>().unwrap() * dir_sign;

        val += clicks;
        let zeros = val.div_euclid(100).abs();
        val = val.rem_euclid(100);

        if val == 0 {
            zero_count += 1;
        }

        writeln!(writer, "{val}");

        zero_count_2 += zeros;
    }

    writer.flush();

    println!("{zero_count}, {zero_count_2}");
    Ok(())
}
