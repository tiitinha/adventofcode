#include <fstream>
#include <iostream>
#include <string>
#include <sstream>

int main() {
  std::ifstream inFile;
  std::string line;

  inFile.open("../input.txt");

  if (!inFile) {
    std::cout << "Unable to open file";
    exit(1);
  }

  while (std::getline(inFile, line)) {
    std::stringstream ss(line);
    int min, max;
    char dash;

    if (ss >> min >> dash >> max) {
      std::cout << "Range: " << min << " to " << max << std::endl;
    }
  }

  inFile.close();

  return 0;
}

long part1(int min, int max) {
  return 0;
}
