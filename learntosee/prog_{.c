#include <stdlib.h>
#include <stdio.h>

int func(int n){
   void* ptr2chunk = malloc(n);
   return 0;
}


int main(void){
  return func(7);
}
