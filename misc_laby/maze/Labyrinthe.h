//
//  Labyrinthe.hpp
//  Laby-p3
//
//  Created by OB on 18/02/2021.
//

#ifndef Labyrinthe_hpp
#define Labyrinthe_hpp

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <iostream>


#define AFF_MUR 'X'
#define AFF_BORD '.'
#define AFF_VIDE ' '
#define AFF_BOT 'B'
#define AFF_SHORT 'A'
#define AFF_TARG 'S'

class Pile{
  private:
      int *stack;
      int stack_end;
      int max;
  public:
      Pile(int size);
      ~Pile();
      void push(int el);
      int pop(void);
      int get_end_stack();
};


class File{
  private:
      int *stack;
      int stack_end;
      int max;
  public:
      File(int size);
      ~File();
      void push(int el);
      int pop(void);
      int get_end_stack();
      bool IsEmpty();
};
class Labyrinthe
{
  private:
      char *schema;
      int *intschema=NULL;
      int L;
      int M;
      std::string short_path_str="";
      void marque(int id, Pile *stack);
      void marque(int id, int val, File *queue);
      int distMinInternal(int id1, int id2);
      int get_random_wall();
      int count_blink();
      int *short_path = NULL;
  public:
      Labyrinthe(int nLignes, int nColonnes);
      Labyrinthe(char data[]);
      ~Labyrinthe();
      int getNbLignes();
      int getNbColonnes();
      int getID(int ligne, int colonne);
      int getLigne(int id);
      int getCol(int id);
      int get_test(int id);
      void modifie(int ligne, int colonne, char x);
      void modifie(int id, char x);
      void affiche();
      void chemin(int id1,int id2);
      std::string getAffiche();
      std::string getDescr();
      std::string shortStr();
      bool checkStr(std::string &in);
      void afficheDescr();
      void clean();
      char lit(int ligne, int colonne);
      char lit(int id);
      bool connexe();
      void genLaby(int nb);
      int distMin(int id1, int id2);
};

#endif /* Labyrinthe_hpp */

