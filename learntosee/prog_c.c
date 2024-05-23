#include <stdlib.h>
#include <stdio.h>

struct human {
   int age;
   int hairs;
};

int func(int n, int y){
   struct human andy;
   andy.age = n;
   andy.hairs = y;
   return 0;
}


int main(void){
  return func(72, 32);
}
