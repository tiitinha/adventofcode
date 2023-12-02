use std::fs;
use std::convert::TryInto;

fn run_program(noun: u32, verb: u32, mut int_code: Vec<u32>) -> u32 {

    int_code[1] = noun;
    int_code[2] = verb;

    let mut i = 0;

    while i <= int_code.len() {
        if i >= int_code.len() || int_code[i] == 99 {
            break;
        }

        let first_position: usize = int_code[i + 1].try_into().unwrap();
        let second_position: usize = int_code[i + 2].try_into().unwrap();

        let result: u32 = if int_code[i] == 1 {
            (int_code[first_position] + int_code[second_position]).into()
        } else if int_code[i] == 2 {
            (int_code[first_position] * int_code[second_position]).into()
        } else {
            break
        };

        let position: usize = int_code[i + 3].try_into().unwrap();
        int_code[position] = result;

        i += 4;
    }

    return int_code[0];
}

fn main() {
    let raw_input: String = fs::read_to_string("input.txt").expect("Something went wrong reading the file");
    let int_code: Vec<u32> = raw_input.split(",").map(|x| x.parse::<u32>().unwrap()).collect();

    for noun in 0..=100 {
        for verb in 0..=100 {
            let result = run_program(noun, verb, int_code.clone());

            if result == 19690720 {
                let fin = 100 * noun + verb;
                println!("{}", fin);
                break;
            }
        }
    }
}
