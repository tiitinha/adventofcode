use std::fs::read_to_string;

fn main() {
    let file = read_to_string("../../input.txt").expect("Should be able to read the file");
    let battery_packs = file.split("\n");

    for pack in battery_packs {
        println!("{pack}");
    }
}
