#include <stdlib.h>
#include <stdio.h>

int func(int n, int y){
   int temp = n ^ y;
   temp = ~temp;
   temp = (temp << 24) | (temp >> 24);
   return temp;
}


int main(void){
  return func(72, 32);
}
