#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include "Strsplit.h"

using namespace std;

vector<int> readCalories() {
    string line;
    // int sumOfCalories;
    int value;
    vector<int> calories;
    int calorieSum;
    ifstream myfile("../input.txt");

    calorieSum = 0;

    if (myfile) {
        while (getline(myfile, line)) {
            if (!line.empty()) {
                value = stoi(line);
                calorieSum += value;
            } else {
                calories.push_back(calorieSum);
                calorieSum = 0;
            }
        }
    }

    return calories;
}

int getMaxValue(vector<int> calories) {


    return 0;
}

int main() {
    vector<int> calories;
    int partOneResult;
    int partTwoResult = 0;

    calories = readCalories();

    sort(calories.begin(), calories.end());

    partOneResult = calories[calories.size() - 1];

    for (int i = 0; i < 3; i++) {
        partTwoResult += calories[calories.size() - 1 - i];
    }

    cout << "Part1: " << partOneResult << endl;
    cout << "Part2: " << partTwoResult << endl;

    return 0;
}
