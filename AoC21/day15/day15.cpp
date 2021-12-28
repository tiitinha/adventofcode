#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include "Dijkstra.h"

using namespace std;

vector<vector<int>> read_input() {
    vector<vector<int>> input_map;
    string line;
    ifstream myfile("test.txt");

    if (myfile) {
        while (getline(myfile, line)) {
            vector<int> row;
            for (char c : line) {
                row.push_back(c - '0');
            }
            input_map.push_back(row);
        }
    }

    return input_map;
}


int main() {
    vector<vector<int>> input_map;
    Dijkstra node;
    node.algo();

    input_map = read_input();

    return 0;
}
