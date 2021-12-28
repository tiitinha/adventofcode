#include <iostream>
#include <string>
#include <fstream>
#include <regex>
#include <bits/stdc++.h>

using namespace std;

struct Instruction {
    string direction;
    int amount;
};

vector<string> split(string str, string splitter) {
    vector<string> result;

    int start = 0;
    int end = str.find(splitter);

    while (end != - 1) {
        result.push_back(str.substr(start, end - start));
        start = end + splitter.size();
        end = str.find(splitter, start);
    }

    result.push_back(str.substr(start, end - start));

    return result;
}

vector<Instruction> readInput() {
    string line;
    int val;
    string direction;
    vector<string> values;
    string regex_str = " ";
    vector<Instruction> inputData;

    ifstream inputFile("input.txt");

    if (inputFile.is_open()) {
        while (getline(inputFile, line)) {
            values = split(line, regex_str);

            direction = values[0];
            val = std::stoi(values[1]);

            Instruction i{.direction = direction, .amount = val};

            inputData.push_back(i);
        }
        inputFile.close();
    }

    return inputData;
}

void part1(vector<Instruction> instructions) {
    int horizontal = 0;
    int depth = 0;
    int result;
    string dir;

    for (auto instr : instructions) {

        dir = instr.direction;

        if (dir == "forward") {
            horizontal += instr.amount;
        } else if (dir == "up") {
            depth -= instr.amount;
        } else if (dir == "down") {
            depth += instr.amount;
        }
    }

    result = horizontal * depth;

    cout << result << endl;
}

int main() {
    vector<Instruction> inputs;

    inputs = readInput();

    part1(inputs);

    return 0;
}
