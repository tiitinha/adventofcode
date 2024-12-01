use std::fs;

fn main() {
    let contents = fs::read_to_string("../input.txt").expect("No fail");
    let mut vec_1 = Vec::new();
    let mut vec_2 = Vec::new();

    for line in contents.split("\n") {
        let values = line.split_whitespace().collect::<Vec<&str>>();
        
        if values.len() > 0 {
            let first = values[0].parse::<i32>().unwrap();
            let second = values[1].parse::<i32>().unwrap();

            vec_1.push(first);
            vec_2.push(second);
        }
    }

    vec_1.sort();
    vec_2.sort();

    part_1(&vec_1, &vec_2);
    part_2(&vec_1, &vec_2);
}

fn part_1(vec_1: &Vec<i32>, vec_2: &Vec<i32>) {
    let mut count: i32 = 0;

    for index in 1..vec_1.len() - 1 {
        let value_1 = vec_1[index];
        let value_2 = vec_2[index];

        let result: i32 = (value_1 - value_2).abs();

        count += result;
    }

    println!("{}", count);
}

fn part_2(vec_1: &Vec<i32>, vec_2: &Vec<i32>) {
    let mut count: i32 = 0;

    for index in 1..vec_1.len() {
        let value_1 = vec_1[index];
        let value_2 = i32::try_from(vec_2.iter().filter(|&n| *n == value_1).count()).unwrap();

        count += value_1 * value_2;
    }

    println!("{}", count);
}
