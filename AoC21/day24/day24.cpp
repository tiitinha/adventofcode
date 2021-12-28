#include <iostream>
#include <vector>
#include <string>
#include "strsplit.h"

using namespace std;

vector<string> read_instructions() {
    string line;
    vector<string> instructions;
    ifstream myfile("test.txt");

    if (myfile) {
        while (getline(myfile, line)) {
            instructions.push_back(line);
        }
    }

    return instructions;
}

int run_instructions(vector<string> instructions, string input) {
    for (string line : instructions) {
        vector<string> instruction;
        instruction = split(line, " ");

        for (string val : instruction) {
            cout << val << " ";
        }
        cout << endl;
    }

    return 0;
}

int main() {
    vector<string> instructions;

    instructions = read_instructions();

    run_instructions(instructions, "input");


    return 0;
}
