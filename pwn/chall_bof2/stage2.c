#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char **argv){
	setreuid(1001,1001);
	FILE *fp;
	char output[1024] = {0};
	fp = popen("md5sum /home/ctf_cracked/flag.txt | cut -d ' ' -f 1","r");
	if(fp == NULL){
		puts("Command Failed");
		return 1;
	}
	fgets(output, sizeof(output), fp);
	output[strlen(output)-1] = '\0'; //trim \n
	if(strcmp(output, "8b098e9d5692641375f8da6d399edf98") == 0)
	    puts("All is clear");
	 else puts("Contact Administrator");
	return 0;
}
