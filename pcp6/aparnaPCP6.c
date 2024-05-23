#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char input[40];
    int encoded_flag[] = {100, 118, 105, 127, 126, 54, 124, 103, 112, 121, 95, 107, 62, 130, 48, 141};

    printf("What's the flag? \n");
    scanf("%s", input);

    if (strlen(input) != 16) {
        printf("Incorrect.\n");
        return 0;
    }

    for (int i = 0; i < 16; i++) {
        if (input[i] != (encoded_flag[i] - i - 1)) {
            printf("Incorrect.\n");
            return 0;
        }
    }

    printf("Correct!\n");

    return 0;
}

