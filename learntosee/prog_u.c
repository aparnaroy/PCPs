#include <stdlib.h>
#include <stdio.h>

int func(int n, int y){
   int sum = 0;
   for (int i = 0; i < n; i++){
     if (i % y == 0){
        sum += i;
     }
   }
   return sum;
}


int main(void){
  return func(72, 32);
}
