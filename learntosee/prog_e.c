#include <stdlib.h>
#include <stdio.h>

int func(int n, int y){
   if (n == 0){
      return y;
   }
   return func(n-1, y+n);
}


int main(void){
  return func(10, 0);
}
