//g++ contribPerso.cpp part4.cpp -o maze -Wall -lpthread
#include <iostream>
#include "Labyrinthe.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <pthread.h>
#include <csignal>

using namespace std;

int serverFd;

void signal_SIGTERM(const int signal){
  close(serverFd);
  exit(signal);
}

void *clientRoutine(void *args){
  int *clientFd = (int*)args;
  Labyrinthe laby(20,30);
  laby.genLaby(20*30/2);
  laby.chemin(0, 30*20-1);
  string aze  = laby.shortStr();
  if(laby.checkStr(aze) == true){
    cout << "check" << endl;
  }else{
    cout << "failed" << endl;
  }
  string maze = "resolvez le chemain le plus cours\nExample:\n";
  maze += laby.getAffiche();
  maze += "vous devez répondre (ou equivalent)->";
  maze += laby.shortStr();
  maze +="\n\n";
  maze += "a votre tour\n";
  Labyrinthe clientlaby(20*3,30*3);
  clientlaby.genLaby(20*30*3*3/2);
  maze += clientlaby.getAffiche();
  //cout << maze << endl;
  const char *msg = maze.c_str();
  send(*clientFd, msg, strlen(msg), 0);
  time_t curr = time(NULL);
  char ret[1024];
  recv(*clientFd, ret, sizeof(ret), 0);
  if((time(NULL)-curr) > 10){
  	char ret[] = "Vous avez mis plus de 10s";
  	send(*clientFd, ret,strlen(ret),0);
  	close(*clientFd);
  	pthread_exit(NULL);
  	return NULL;
  }
  string resultat = string(ret);
  //cout << "result = "<<resultat << endl;
  string response = "";
  if(clientlaby.checkStr(resultat) == true){
    cout << "client sucess"<< endl;
    //cout << resultat << " is the good answer" << endl;
    response += "Bien joué tu as CYBERTF{M@ze_Mast3r}\n";
  }
  else{
    cout << "client failes" << endl;
    response += "Aie c'est raté !!!!\nméchant chevalo\n";
  }
  response += "une solution possible était\n";
  clientlaby.chemin(0, 3*20*3*30-1);
  //cout << "solution=" << clientlaby.shortStr() << endl;
  response += clientlaby.shortStr();
  response += "\n";
  const char * response_c = response.c_str();
  send(*clientFd, response_c, strlen(response_c), 0);
  close(*clientFd);
  pthread_exit(NULL);
}



int main(int argc, char const *argv[]) {
  srand(time(NULL));
  signal(SIGTERM, signal_SIGTERM);
  if(argc < 2){
    cout << "Usage: " << argv[0] <<" PORT"<< endl;
    exit(1);
  }
  int port = atoi(argv[1]);
  sockaddr_in servAddr;
  servAddr.sin_family = AF_INET;
  servAddr.sin_addr.s_addr = htonl(INADDR_ANY);
  servAddr.sin_port = htons(port);
  // creation du socket
  serverFd = socket(AF_INET, SOCK_STREAM, 0);

  if(bind(serverFd, (struct sockaddr *)&servAddr, sizeof(servAddr)) < 0){
    cerr << "Error bind" << endl;
    exit(1);
  }
  listen(serverFd, 5);
  sockaddr_in clientAddr;
  socklen_t clientLen = sizeof(clientAddr);
  int clientFd;
  pthread_t thread;
  while(true){
    clientFd = accept(serverFd, (sockaddr *)&clientAddr, &clientLen);
    if(clientFd < 0){
      cerr << "Error accepting connection"<<endl;
      exit(1);
    }
    pthread_create(&thread, NULL, clientRoutine, (void *)&clientFd);
  }



  return 0;
}

