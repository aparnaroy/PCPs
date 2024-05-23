int mod64(int n){
  int result = 0;
  result = n % 64;
  return result;
}


int main(void){
  return mod64(7);
}
