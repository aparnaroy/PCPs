#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>

int main(){
    puts("hi, let's do dynamic memory\n");
    puts("first let's ask for enough space for 16, 32, 48, and 64 bytes and see what happens...\n");

    void *address16 = malloc(16);
    void *address32 = malloc(32);
    void *address48 = malloc(48);
    void *address64 = malloc(64);

    puts("Now we pause the process so we have time to inspect.\n");

    gets((char *)address64);//yes insecure I know...

    puts("OK, now let's free something...\n");

    free(address16);

    puts("Now we pause the process so we have time to inspect.\n");

    gets((char *)address64);//yes insecure I know...

    puts("OK, now let's free something else:\n");

    free(address64);

    puts("Now we pause the process so we have time to inspect.\n");

    gets((char *)address48);//yes insecure I know...

    return 0;
}
