#include <stdlib.h>
#include <stdio.h>

int func(int n, int y){
   FILE *fptr;

   fptr = fopen("tempfile","w");

   if(fptr == NULL)
   {
      printf("Error!");   
      exit(1);             
   }

   fprintf(fptr,"%d,%d",n,y);
   fclose(fptr);
   return 0;
}


int main(void){
  return func(72, 32);
}
