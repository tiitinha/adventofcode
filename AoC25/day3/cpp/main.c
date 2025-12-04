#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file = fopen("../test.txt", "r");
    int thisCharacter;
    int nextCharacter;
    
    if (file == NULL) {
        printf("File not found");
        exit(1);
    }

    while ((thisCharacter = fgetc(file)) != EOF) {
        if (thisCharacter == '\n') {
            nextCharacter = fgetc(file);
            
            if (nextCharacter == EOF) {
                break;
            }
            
            ungetc(nextCharacter, file);
            
        } else {
            printf("%d", thisCharacter - '0');
        }
    }
    
    fclose(file);
    
    return 0;
}
