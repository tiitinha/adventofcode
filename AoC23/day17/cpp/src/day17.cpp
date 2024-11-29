#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int min_heat_loss(vector<vector<int>> heatmap) {
    int heat_loss = 0;
    for (auto &row : heatmap) {
        for (auto &val : row) {
            heat_loss += val;
        }
    }

    return heat_loss;
}

int main() {
    string line;
    vector<vector<int>> heatmap;

    ifstream file("../../input.txt");

    cout << "Reading the file" << endl;
    
    if (file.is_open()) {
        while (getline(file, line)) {
            vector<int> row;
            
            for (char &c : line) {
                int char_val = c - '0';
                row.push_back(char_val);
            }

            heatmap.push_back(row);
        }
        file.close();
    }

    int result = min_heat_loss(heatmap);
    cout << "Part 1 result: " << result << endl;

    return 0;
}
