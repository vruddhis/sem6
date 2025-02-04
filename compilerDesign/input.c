#include <stdio.h>

int main() {
    int a = 5;
    float b = 3.14;
    char c = 'X';

    if (a > 0) {
        printf("Positive number\n");
    } else {
        printf("Non-positive number\n");
    }

    // This is a single-line comment

    /*
       This is a multi-line comment.
       It should be ignored by the lexer.
    */

    return 0;
}
