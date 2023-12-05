use std::fs;
use regex::Regex;

fn main() {
    let input_data = fs::read_to_string("../test.txt").expect("Shoulda giv file");
    let mut i = 0;
    let re = Regex::new("([0-9]+)").unwrap();

    for line in input_data.lines() {
        println!("{i}");
        let bits: Vec<&str> = line.split(":").collect();
        let numbers: Vec<&str> = bits[1].split("|").collect();

        let own = re.captures_iter(numbers[0]) else {
            return;
        };
        let winning = re.captures_iter(numbers[1]) else {
            return;
        };

        for n in own {
            print!("{} ", n.get(0).unwrap().as_str());
        }
        
        println!("");

        for m in winning {
            print!("{} ", m.get(0).unwrap().as_str());
        }
    
        println!("");
        

        i += 1;
    }
}
