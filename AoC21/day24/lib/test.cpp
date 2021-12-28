#include <string>
#include <vector>
#include "strsplit.h"
#include <iostream>

using namespace std;

int main() {
    string test = "test this string";

    vector<string> splitted = split(test, " ");

    //for (string part : splitted) {
    //    cout << part << endl;
    //}

    return 0;
}
