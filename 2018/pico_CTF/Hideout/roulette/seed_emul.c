#include <stdio.h>
#include <stdlib.h>

int main() {
    int seed = 0;

    printf("Insert seed!\n");
    scanf("%d", &seed);

    srand(seed);

    for(int i = 0; i < 4; i++) {
        printf("%d\n", rand() % 36 + 1);
        rand();
    }
}