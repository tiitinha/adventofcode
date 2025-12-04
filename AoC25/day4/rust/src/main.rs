use std::fs::read_to_string;

fn check_neighbor_count(row: i32, col: i32, paper_map: &Vec<Vec<char>>) -> i32 {
    let mut count = 0;

    for y in -1..=1 {
        for x in -1..=1 {
            if y == 0 && x == 0 {
                continue;
            }

            if y + row < 0
                || y + row >= paper_map.len().try_into().unwrap()
                || x + col < 0
                || x + col >= paper_map[0].len().try_into().unwrap()
            {
                continue;
            }

            let y_usize: usize = (y + row) as usize;
            let x_usize: usize = (x + col) as usize;

            if paper_map[y_usize][x_usize] == '@' {
                count += 1;
            }
        }
    }

    return count;
}

fn main() {
    let mut paper_map = Vec::new();

    for line in read_to_string("../../input.txt").unwrap().lines() {
        let row: Vec<char> = line.chars().collect();

        paper_map.push(row);
    }

    let rows = paper_map.len();
    let cols = paper_map[0].len();
    let mut total_count = 0;
    let mut papers: Vec<(usize, usize)> = Vec::new();
    let mut cont = true;

    while cont {
        for j in 0..rows {
            for i in 0..cols {
                let cell = paper_map[j][i];

                if cell != '@' {
                    continue;
                }

                let j_int = j as i32;
                let i_int = i as i32;

                let neighbor_count = check_neighbor_count(j_int, i_int, &paper_map);

                if neighbor_count < 4 {
                    papers.push((j, i));
                    total_count += 1;
                }
            }
        }

        if papers.len() == 0 {
            cont = false;
        }

        while papers.len() > 0 {
            let point = papers.pop().unwrap();
            paper_map[point.0][point.1] = '.';
        }
    }

    println!("{total_count}");
}
