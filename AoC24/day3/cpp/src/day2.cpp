#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Parse do() with strncomp
int parse_do(const char *text) { return (strncmp(text, "do()", 4)) ? 0 : 4; }

// Parse don't with strncomp
int parse_dont(const char *text) { return strncmp(text, "don't()", 7) ? 0 : 7; }

// Parse mul(XXX,YYY) with strncomp
int parse_mul(const char *text, int *x, int *y) {

  // Check whether string text starts with mul(. If not, then return 0
  if (strncmp(text, "mul(", 4) != 0)
    return 0;

  // If yes, then go to the next char after mul(
  const char *p = text + 4;
  char *end;

  // Convert string to long integer and store in pointer x
  *x = strtol(p, &end, 10);
  // If pointer is at the end, no digits found. If pointer is not comma, then no
  // second number found
  if (end == p || *end != ',')
    return 0;

  // Move to next digit start
  p = end + 1;

  // Convert string to long int and store in pointer y
  *y = strtol(p, &end, 10);

  // Check if pointer still at the end and that end is )
  if (end == p || *end != ')')
    return 0;

  // Return ptr to next value in input
  return end - text + 1;
}

int main() {
  FILE *file = fopen("../input.txt", "r");

  if (!file) {
    perror("Failed to read the file");
    return 1;
  }

  char *line = NULL;
  size_t len = 0;
  int mul_enabled = 1;
  long long res = 0;

  while (getline(&line, &len, file) != -1) {
    for (const char *p = line; *p; p++) {
      int x, y;
      int consumed;

      if ((consumed = parse_do(p))) {
        mul_enabled = 1;
        p += consumed - 1;
      }

      if ((consumed = parse_dont(p))) {
        mul_enabled = 0;
        p += consumed - 1;
      }

      if ((consumed = parse_mul(p, &x, &y))) {
        if (mul_enabled == 1) {
          res += x * y;
        }
        p += consumed - 1;
      }
    }
  }

  printf("%lld\n", res);

  free(line);
  fclose(file);

  return 0;
}
