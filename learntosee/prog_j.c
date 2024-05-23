int func(int n){
  int arr[100];
  arr[n] = n+1;
  return arr[0];
}


int main(void){
  return func(7);
}
