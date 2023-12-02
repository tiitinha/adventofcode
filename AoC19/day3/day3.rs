use std::fs;

fn main() {

    let input_data: String = fs::read_to_string("test.txt").expect("Something went wrong");

    let instructions = input_data.split("\n").collect::<Vec<&str>>();

    
}
