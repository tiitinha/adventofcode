#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int part1;
  int part2;
} Result;

void get_digits(int number, int digits[]) {
  int value = number;
  for (int i = 0; i < 6; i++) {
    int modulo = value % 10;
    digits[5 - i] = modulo;
    value /= 10;
  }
}

int is_double(int digits[]) {
  int valid = 0;
  
  for (int i = 0; i < 5; i++) {
    if (digits[i] > digits[i + 1]) return 0;

    if (i > 0 && !valid) {
      if (digits[i - 1] == digits[i] && digits[i] != digits[i + 1]) {
	valid = 1;
      } else {
	valid = 0;
      }
    }
  }

  return valid;
}

int is_valid(int digits[]) {
  int valid = 0;
  for (int i = 0; i < 5; i++) {
    if (digits[i] > digits[i + 1]) return 0;
    if (digits[i] == digits[i + 1]) valid = 1;
  }

  return valid;
  
}

Result parts(int firstNum, int secondNum) {
  int total = 0;
  int total2 = 0;
  for (int i = firstNum; i <= secondNum; i++) {
    int digits[6];
    get_digits(i, digits);
    total += is_valid(digits);
    total2 += is_double(digits);
  }

  Result results = (Result){total, total2};
  return results;
}

int main() {
  FILE *file = fopen("../input.txt", "r");

  if (file == NULL) {
    printf("File not found");
    exit(1);
  }

  int firstNum, secondNum;

  while (fscanf(file, "%d-%d", &firstNum, &secondNum) == 2) {
    printf("The range was from %d to %d\n", firstNum, secondNum);
  }

  fclose(file);

  Result result = parts(firstNum, secondNum);

  printf("Result: %d, %d\n", result.part1, result.part2);

  int test_num = 112233;
  int test_digits[6];
  get_digits(test_num, test_digits);
  int test_valid = is_double(test_digits);

  printf("%d, %d\n", test_num, test_valid);
  
  return 0;
}

