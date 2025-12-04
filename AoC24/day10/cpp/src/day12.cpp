#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
  int x;
  int y;
  int value;
} Point;

Point *get_start_points(int **arrayOfVals, size_t rows, size_t cols,
                        int *count) {
  int pointsSize = 1;
  int pointsCount = 0;
  Point *points = (Point *)malloc(pointsSize * sizeof(Point));

  for (size_t i = 0; i < rows; i++) {
    for (size_t j = 0; j < cols; j++) {
      if (arrayOfVals[i][j] == 0) {
        pointsSize++;
        points = (Point *)realloc(points, pointsSize * sizeof(Point));

        points[pointsCount].x = i;
        points[pointsCount].y = j;
        points[pointsCount].value = 0;

        pointsCount++;
      }
    }
    printf("\n");
  }

  *count = pointsCount;
  return points;
}

int main() {
  FILE *fptr;
  int thisCharacter;
  int nextChar;
  int lines = 1;
  int columns = 1;
  int **storedArray;
  int currentRow = 0;
  int currentColumn = 0;
  Point *points;
  int count = 0;

  storedArray = (int **)malloc(lines * sizeof(int *));

  for (int i = 0; i < lines; i++) {
    storedArray[i] = (int *)malloc(columns * sizeof(int));
  }

  fptr = fopen("../input.txt", "r");

  if (fptr == NULL) {
    printf("Not able to open the file");
    return 0;
  }

  while ((thisCharacter = fgetc(fptr)) != EOF) {
    if (thisCharacter == '\n') {
      nextChar = fgetc(fptr);

      if (nextChar == EOF) {
        break;
      }

      ungetc(nextChar, fptr);

      currentRow++;
      currentColumn = 0;

      if (currentRow >= lines) {
        lines++;
        storedArray = (int **)realloc(storedArray, lines * sizeof(int *));

        if (storedArray == NULL) {
          printf("Memory allocation failed");
          return 1;
        } else {
          storedArray[currentRow] = (int *)malloc(columns * sizeof(int));
        }
      }
    } else if (thisCharacter >= '0' && thisCharacter <= '9') {

      if (currentColumn >= columns) {
        columns++;

        for (int i = 0; i < lines; i++) {
          storedArray[i] =
              (int *)realloc(storedArray[i], columns * sizeof(int));

          if (storedArray[i] == NULL) {
            printf("Memory allocation failed");
            return 1;
          }
        }
      }

      storedArray[currentRow][currentColumn] = thisCharacter - '0';
      currentColumn++;
    }
  }

  fclose(fptr);

  points = get_start_points(storedArray, lines, columns, &count);

  for (int i = 0; i < count; i++) {
    printf("point %d: (%d, %d)\n", points[i].value, points[i].x, points[i].y);
  }

  for (int i = 0; i < lines; i++) {
    free(storedArray[i]);
  }

  free(storedArray);
  free(points);

  return 0;
}
