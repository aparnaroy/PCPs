#include <stdlib.h> 
#include <stdio.h> 

void init(){
    setvbuf(stdin,NULL,_IONBF,0);
    setvbuf(stdout,NULL,_IONBF,0);
    setvbuf(stderr,NULL,_IONBF,0);
}

void win(unsigned int x){ 
    if (x != 0xDECAFBAD){
        puts("Almost...");
	return;
    }
    system("/bin/sh");
} 

void vuln(){
    char buf[24]; 
    gets(buf); 
} 

int main(){ 
    init();
    puts("Can you call the win, and give it an argument?\n"); 
    vuln(); 
    return 0; 
} 
