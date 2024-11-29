use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::vec::Vec;

fn main() {
    const RADIX: u32 = 10;
    if let Ok(lines) = read_lines("../input.txt") {
        let mut rows: Vec<Vec<u32>> = Vec::new();
        for line in lines.flatten() {
            let line_chars = line.chars().map(|c| c.to_digit(RADIX).unwrap()).collect();
            rows.push(line_chars);
        }

        let result: u32 = min_heat_loss(rows);
        println!("Part 1 result: {}", result);
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn min_heat_loss(heatmap: Vec<Vec<u32>>) -> u32 {
    let mut heat_loss: u32 = 0;
    let mut consecutive_steps: i32 = 0;
    let height: usize = heatmap.len().try_into().unwrap();
    let width: usize = heatmap[0].len().try_into().unwrap();

    let heatloss_map: Vec<Vec<u32>> = vec![vec![100; width]; height];

    for row in heatmap {
        for val in row {
            heat_loss += val;
        }
    }

    return heat_loss;
}
