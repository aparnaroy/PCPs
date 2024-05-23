#include <stdlib.h>
#include <stdio.h>

int func(int n, int y){
   char arr[100];
   arr[n] = 'h';
   arr[y] = 'i';
   arr[0] = 'y';
   arr[1] = 'o';
   arr[2] = 0;
   return 100;
}


int main(void){
  return func(72, 32);
}
