#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include "Strsplit.h"

using namespace std;

vector<string> read_instructions() {
    string line;
    vector<string> instructions;
    ifstream myfile("../test.txt");

    if (myfile) {
        while (getline(myfile, line)) {
            instructions.push_back(line);
        }
    }

    return instructions;
}

int run_instructions(vector<string> instructions, string input) {
    int input_val;

    char current;

    for (string line : instructions) {
        vector<string> instruction;
        instruction = split(line, " ");

        if (instruction[0] == "inp") {
            input_val = get_input();
            current = instruction[1];


        }

        for (string val : instruction) {
            //cout << val << ", ";
        }
    }

    cout << x << y << z << w

    return 0;
}

int main() {
    vector<string> instructions;

    instructions = read_instructions();

    run_instructions(instructions, "input");


    return 0;
}
