#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

vector<vector<int>> readInput() {
    vector<vector<int>> input_array;
    string line;
    string num;
    int val;

    ifstream input_file("test.txt");

    if (input_file.is_open()) {
        while (getline(input_file, line)) {
            vector<int> number_line;
            for (int cell = 0; cell < line.length(); cell++) {
                num = line[cell];
                val = std::stoi(num);
                number_line.push_back(val);
            }
            input_array.push_back(number_line);
        }
    }

    return input_array;
}

void part1(vector<vector<int>> octopus_map) {
    return;
}

int main() {
    vector<vector<int>> input_data;

    input_data = readInput();


    return 0;
}
