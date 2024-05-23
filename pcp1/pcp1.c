// Create a character array to hold your flag
// Loop through this array of values: [110, 1, 105, 110, 1, 106, 2, 97, 123, 100, 3, 117, 53, 5, 116, 95, 48, 102, 8, 102, 95, 121, 48, 117, 114, 95, 67, 125]
// If a value is <= 10 skip it. Otherwise append the letter whose ascii value matches the given value to your flag
// Print the flag


#include <stdio.h>

int main() {
   char flag[40];
   int vals[] = {110, 1, 105, 110, 1, 106, 2, 97, 123, 100, 3, 117, 53, 5, 116, 95, 48, 102, 8, 102, 95, 121, 48, 117, 114, 95, 67, 125};
   int currIndex = 0;

   for (int i=0; i < sizeof(vals) / sizeof(int); i++) {
      if (vals[i] > 10) {
         flag[currIndex] = (char)vals[i];
         currIndex++;
      }
   }

   flag[currIndex] = '\0';   

   printf("%s\n", flag);
   return 0;
}
