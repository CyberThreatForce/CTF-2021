#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int check(const char *tab,const char *tab1, size_t s){
  for(size_t i=0; i<s; i++){
    if(tab[i]-tab1[i] != 0) return tab[i]-tab1[i];

  }
  return 0;
}

int main(int argc, char const *argv[]) {
  setreuid(1001,1001);
  if(argc !=3 ){
    exit(1);
  }
  char password[] = {0xDE, 0xAD, 0xBE, 0xEF, '1','2','3',0xAA,0xBB,0xCC,0xDD,0xC0,0xFF,0xee};
  puts("");
  if(14!= strlen(argv[1])){
    return 1;
  }
  if(check(password, argv[1], 14)==0){
    puts("Password check");
    char buff[1024] = {0};
    FILE *fp = fopen(argv[2],"r");
    while(fgets(buff, 1024, fp)){
      puts(buff);
    }
  }else{
    puts("Password failed");
    return 1;
  }
  return 0;
}
