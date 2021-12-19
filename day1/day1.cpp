#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <numeric>

using namespace std;

vector<int> readInput() {

    string line;
    vector<int> inputData;
    int val;
    ifstream myfile("input.txt");

    if (myfile.is_open()) {
        while (getline(myfile, line)) {
            val = std::stoi(line);
            inputData.push_back(val);
        }
       myfile.close();
    }

    return inputData;
}

void part1(vector<int> inputData) {
    int count;
    int previous;
    int current;
    count = 0;

    previous = inputData[0];

    for (auto it = std::next(inputData.begin(), 1); it != inputData.end(); ++it) {
        current = *it;

        if (current > previous) {
            count++;
        }

        previous = current;
    }

    cout << count << endl;
}

int* initialize(vector<int> inputData, int* prevs) {
    for (int i = 0; i < 3; i++) {
        prevs[i] = inputData[i];
    }

    return prevs;
}

int summation(int* input) {
    int sum = 0;
    int length = 3;

    return accumulate(input, input + length, sum);
}

int* shift(int *prevs, int next) {
    prevs[0] = prevs[1];
    prevs[1] = prevs[2];
    prevs[2] = next;

    return prevs;
}

void part2(vector<int> inputData) {
    int *prevs = new int;
    int sum;
    int prevSum;
    int currentSum;
    int current;
    int count = 0;

    prevs = initialize(inputData, prevs);

    prevSum = summation(prevs);
    prevSum = 0;
    currentSum = 0;

    for (auto it = inputData.begin() + 3; it != inputData.end(); ++it) {
        current = *it;

        prevs = shift(prevs, current);
        currentSum = summation(prevs);

        if (currentSum > prevSum) {
            count++;
        }

        prevSum = currentSum;

    }

    cout << count << endl;

}

int main() {
    vector<int>  inputData;

    inputData = readInput();

    part1(inputData);

    part2(inputData);
}
