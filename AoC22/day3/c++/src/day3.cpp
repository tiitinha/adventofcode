#include <fstream>
#include <string>
#include <vector>
#include <iostream>
#include <set>

using namespace std;

int main() {
    string line;
    vector<char> uniqueVals;
    string firstPart;
    string secondPart;
    int lineLength;

    ifstream file("./input.txt");

    if (file) {
        while (getline(file, line)) {
            lineLength = line.size();

            firstPart = line.substr(0, (int) lineLength / 2);
            secondPart = line.substr((int) lineLength / 2, lineLength - 1);

            cout << firstPart << ", " << secondPart << endl;
        }
    }

    return 0;
}
