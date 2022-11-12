#include <string>
#include <vector>
#include "Strsplit.h"
#include <iostream>
#include <fstream>

using namespace std;

vector<vector<string>> read_input() {
   vector<string> input;
    string line;
    ifstream myfile("../test.txt");
    vector<vector<string>> coords;
    vector<string> coordline;

    if (myfile) {
        while (getline(myfile, line)) {
            if (line.find("scanner") != std::string::npos) {
                vector<string> coordline;
            } else if (!(line.find("\n") != std::string::npos) & !line.empty()) {
                coords.push_back(split(line, ","));
            }
        }
    }

    return coords;
}

int main () {
    vector<vector<string>> input;

    input = read_input();

    for (vector<string> scanner : input) {
        cout << scanner[0] << ", " << scanner[1] << endl;
    }

    return 0;
}

