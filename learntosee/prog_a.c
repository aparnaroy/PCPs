#include <stdlib.h>
#include <stdio.h>

int func(int n, int y){
   int x;
   scanf("%d",&x);
   return x+n+y;
}


int main(void){
  return func(72, 32);
}
