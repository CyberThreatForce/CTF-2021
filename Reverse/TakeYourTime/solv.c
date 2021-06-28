#include <stdio.h>
#include <stdlib.h>


unsigned int fib(int n) {
  int first = 0, second = 1;

  int tmp;
  while (n--) {
    tmp = first+second;
    first = second;
    second = tmp;
  }
  return first;
}



int main(int argc, char **argv){
        char tab[] = {0xB5,0x63,0x98,0x3D,0xB5,0x06,0x46,0xBA,0x0F,0xD5,0x47,0xCE,0x97,0xEF,0x7B,0x28,0xDB,0xE7,0x39,0x10,0xB0,0xF5,0x44,0xEC,0x30,0x88,0x46,0xF6,0x88};
	unsigned int magie;
	unsigned int checksum = 0;
	for(int i = 0x32; i<0x4f; i+=1){
		magie = fib(i);
		checksum = checksum>>8 | (magie^checksum)<<0x18;
	}
	srand(checksum);
	char curr;
	for(int i=0; i<0x1d; i+=1){
	  curr=tab[i];
	  putchar((char)(curr ^ rand() % 0xff));
	
	}
	



	return 0;
}
