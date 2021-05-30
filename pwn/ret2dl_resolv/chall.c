//gcc chall.c -o chall -m32 -fno-stack-protector -no-pie
#include <unistd.h>
#include <stdio.h>
void vuln(void){
    char buf[100];
    read(0, buf, 150);
}
void ignorMe(){
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}
int main(int argc, char** argv){
  ignorMe();
  puts("password: ");
  vuln();
  puts("nop");
}
