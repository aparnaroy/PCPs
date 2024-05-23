#include <stdlib.h>
#include <stdio.h>

void init(){
    setvbuf(stdin,NULL,_IONBF,0);
    setvbuf(stdout,NULL,_IONBF,0);
    setvbuf(stderr,NULL,_IONBF,0);
}

void vuln(){
    printf("Simple printf followed by an evil bof\n");
    char babybuf[0x20];
    fgets(babybuf, 0x1f, stdin);
    printf(babybuf);
    char buf[0x20];
    gets(buf);
}

int main(){
    init();
    vuln();
    return 0;
}
