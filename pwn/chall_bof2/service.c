#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>


void magie(int in){
  char magie[] = "CYBERTF{YZY}";
  if(in==(-1) || (strcmp("CYBERTF{YZY}",magie) == 0)){
    puts("Good Way");
  }else{
    puts("CYBERTF{B@sic_Buff3r_Ov3rflow}");
  }
}

void ignorMe(){
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

//_____________________
int main(int argc, char const *argv[]) {
  ignorMe();
  char username[40] = {0};
  puts("hello who are you?");
  scanf("%s", username);
  printf("Hello %s\n", username);
  return 0;
}
