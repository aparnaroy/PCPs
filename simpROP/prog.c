#include <stdlib.h>
#include <stdio.h>

void vuln(){
    char buf[0x20];
    gets(buf);
}

int main(){
    puts("/bin/sh");
    system("/bin/ls");
    vuln();
    return 0;
}
