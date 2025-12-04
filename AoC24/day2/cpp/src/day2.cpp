#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

std::vector<std::vector<int>> read_data(const std::string &filename) {
  std::ifstream file(filename);

  if (!file) {
    throw std::runtime_error("No file found");
  }

  std::vector<std::vector<int>> data;
  std::string line;

  while (std::getline(file, line)) {
    std::vector<int> row;
    std::istringstream iss(line);
    int num;

    if (iss >> num) {
      row.push_back(num);
    }

    if (!row.empty()) {
      data.push_back(row);
    }
  }

  return data;
}

int main() {

  auto data = read_data("../input.txt");

  for (const auto &row : data) {
    for (int val : row) {
      std::cout << val << " ";
    }

    std::cout << "\n";
  }

  return 0;
}
