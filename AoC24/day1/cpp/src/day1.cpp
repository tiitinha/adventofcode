#include <iostream>
#include <fstream>
#include "Strsplit.h"
#include <algorithm>
#include <vector>

using namespace std;

int part_1(vector<int> vector_1, vector<int> vector_2) {
    int cnt = 0;

    for (unsigned int i = 0; i < vector_1.size(); i++) {
        cnt += abs(vector_1[i] - vector_2[i]);
    }

    return cnt;
}

int part_2(vector<int> vector_1, vector<int> vector_2) {
    int cnt = 0;
    
    for (auto value: vector_1) {
        int value_2 = count(vector_2.begin(), vector_2.end(), value);
        cnt += value * value_2;
    }

    return cnt;
}

bool comp(int a, int b) {
    return a <= b;
}

int main() {
    string line;
    vector<int> vector_1;
    vector<int> vector_2;
    vector<string> values;

    int part_1_result;
    int part_2_result;
    
    ifstream myfile("../../input.txt");

    if (myfile) {
        while (getline(myfile, line)) {
            if (!line.empty()) {
                values = split(line, "   ");

                vector_1.push_back(stoi(values[0]));
                vector_2.push_back(stoi(values[1]));
            }
        }
    }

    sort(vector_1.begin(), vector_1.end(), comp);
    sort(vector_2.begin(), vector_2.end(), comp);

    part_1_result = part_1(vector_1, vector_2);
    part_2_result = part_2(vector_1, vector_2);

    cout << "Part 1: " << part_1_result << ", part 2: " << part_2_result << endl;
}

