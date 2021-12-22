#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

struct Result {
    int score_1;
    int score_2;
    int rolls;
};

vector<int> readInput() {
    vector<int> starting_positions;
    string line;
    char val;

    ifstream inputFile("input.txt");

    if (inputFile.is_open()) {
        while (getline(inputFile, line)) {
            val = line[line.length() - 1] - '0';
            starting_positions.push_back(val);
        }
    }

    return starting_positions;
}

Result part1(vector<int> starting_positions) {
    Result result;
    vector<int> player_scores {0, 0};
    int dice_value = 1;
    int dice_rolls = 0;
    vector<int> player_pos = starting_positions;

    while (true) {
        for (int p = 0; p < 2; p++) {
            int steps;
            int throw_sum = 0;
            for (int i = 0; i <= 2; i++) {
                throw_sum += dice_value;

                dice_value++;
                dice_rolls++;

                if (dice_value > 100) {
                    dice_value = 1;
                }
            }


            steps = throw_sum % 10 == 0 ? 10 : throw_sum % 10;

            player_pos[p] = (player_pos[p] + steps) % 10 == 0 ? 10 : (player_pos[p] + steps) % 10;
            player_scores[p] += player_pos[p];

            if (player_scores[0] >= 1000 || player_scores[1] >= 1000) {
                result.score_1 = player_scores[0];
                result.score_2 = player_scores[1];
                result.rolls = dice_rolls;

                return result;
            }
        }
    }
}


int main() {
    vector<int> starting_positions;
    Result part_1_res;
    int pt1_min;

    starting_positions = readInput();

    part_1_res = part1(starting_positions);

    pt1_min = std::min(part_1_res.score_1, part_1_res.score_2);

    cout << part_1_res.score_1 << ", " << part_1_res.score_2 << ", " << part_1_res.rolls << endl;
    cout << pt1_min * part_1_res.rolls << endl;


    return 0;
}
