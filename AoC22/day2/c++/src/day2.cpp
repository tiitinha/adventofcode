#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
#include "Strsplit.h"

using namespace std;

int main() {
    string line;
    vector<pair<char, char>> rnds;
    vector<string> bits;
    unordered_map<char, char> stratsPt1;
    unordered_map<char, int> points;
    unordered_map<char, unordered_map<char, char>> getStratForResult;
    unordered_map<char, unordered_map<char, int>> getResultForFirst;

    int ptOneSum = 0;
    int ptTwoSum = 0;

    points = {{'A', 1}, {'B', 2}, {'C', 3}, {'X', 0}, {'Y', 3}, {'Z', 6}};
    stratsPt1 = {{'X', 'A'}, {'Y', 'B'}, {'Z', 'C'}};
    getStratForResult = {
        {'A', {
                  {'X', 'C'},
                  {'Y', 'A'},
                  {'Z', 'B'}
              }},
        {'B', {
                {'X', 'A'},
                {'Y', 'B'},
                {'Z', 'C'}
            }},
        {'C', {
                {'X', 'B'},
                {'Y', 'C'},
                {'Z', 'A'}
            }}
    };
    getResultForFirst = {
        {'A', {
                  {'X', 3},
                  {'Y', 6},
                  {'Z', 0}
              }},
        {'B', {
                  {'X', 0},
                  {'Y', 3},
                  {'Z', 6}
              }},
        {'C', {
                  {'X', 6},
                  {'Y', 0},
                  {'Z', 3}
              }}
    };

    ifstream file("./input.txt");

    if (file) {
        while(getline(file, line)) {
            bits = split(line, " ");


            rnds.emplace_back(bits[0][0], bits[1][0]);
        }
    }

    for (const pair<char, char> &rnd : rnds) {

        ptOneSum += getResultForFirst.at(rnd.first).at(rnd.second) + points.at(stratsPt1.at(rnd.second));
        ptTwoSum += points.at(rnd.second) + points.at(getStratForResult.at(rnd.first).at(rnd.second));

    }

    cout << ptOneSum << ", " << ptTwoSum << endl;

    return 0;
}
