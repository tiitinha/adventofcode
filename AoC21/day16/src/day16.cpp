include <string>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

int main() {
    string input;

    ifstream myfile("../test.txt");

    if (myfile) {
        getline(myfile, input);
    }

    cout << input << endl;

    return 0;

}

