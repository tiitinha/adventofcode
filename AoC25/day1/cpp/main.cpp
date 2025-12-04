#include <iostream>
#include <fstream>
#include <string>

int sign(int x) {
    return (x >= 0) - (x < 0);
}

int main() {
  std::ifstream file("../input.txt");
  std::string str;
  //std::ofstream myfile;
  //myfile.open("output.txt");
  int val = 50;
  int zero_count = 0;  
  
  while (std::getline(file, str)) {
    char direction = str[0];
    int clicks = std::stoi(str.substr(1, 2));
    int dir_sign = sign((direction - 'R'));

    val += clicks * dir_sign;
    
    val = ((val % 100) + 100) % 100;

    if (val == 0) {
        zero_count++;
    }

    //myfile << val << std::endl;

  }
  //myfile.close();
  std::cout << zero_count << std::endl;

  return 0;
}
