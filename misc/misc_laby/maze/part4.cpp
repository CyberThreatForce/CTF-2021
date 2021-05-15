#include <iostream>
#include "Labyrinthe.h"

using namespace std;

// #define AFF_MUR 'X'
// #define AFF_BORD '.'
// #define AFF_VIDE ' '
// #define AFF_BOT 'B'
// #define AFF_SHORT 'A'
// #define AFF_TARG 'S'

// class Pile{
//   private:
//       int *stack;
//       int stack_end;
//       int max;
//   public:
//       Pile(int size);
//       ~Pile();
//       void push(int el);
//       int pop(void);
//       int get_end_stack();
// };
string& rtrim(std::string& str, const std::string& chars = "\t\n\v\f\r "){
    str.erase(str.find_last_not_of(chars) + 1);
    return str;
}
Pile::Pile(int size){
  stack = new int[size];
  stack_end = 0;
  max= size;
}
Pile::~Pile(){
  delete[] stack;
}
void Pile::push(int el){
  if(stack_end == max){
    cout << "Error try to push full stack" << endl;
  }
  stack[stack_end] = el;
  stack_end ++;
}
int Pile::pop(){
  if(stack_end == 0){
    cout << "Error try to pop empty stack" << endl;
    exit(1);
  }
  stack_end --;
  return stack[stack_end];
}
int Pile::get_end_stack(){
  return stack_end;
}
// class File{
//   private:
//       int *stack;
//       int stack_end;
//       int max;
//   public:
//       File(int size);
//       ~File();
//       void push(int el);
//       int pop(void);
//       int get_end_stack();
//       bool IsEmpty();
// };
File::File(int size){
  stack = new int[size];
  stack_end = 0;
  max= size;
}
File::~File(){
  delete[] stack;
}
void File::push(int el){
  if(stack_end == max){
    cout << "Error try to push full stack" << endl;
  }
  stack[stack_end] = el;
  stack_end ++;
}
int File::pop(){
  if(stack_end == 0){
    cout << "Error try to pop empty stack" << endl;
    exit(1);
  }
  int fst = stack[0];
  for (int i = 0; i < stack_end-1; i++) {
    stack[i] = stack[i+1];
  }
  stack_end --;
  return fst;
}
int File::get_end_stack(){
  return stack_end;
}
bool File::IsEmpty(){
  return get_end_stack() == 0;
}

// class Labyrinthe
// {
//   private:
//       char *schema;
//       int *intschema=NULL;
//       int L;
//       int M;
//       std::string short_path_str="";
//       void marque(int id, Pile *stack);
//       void marque(int id, int val, File *queue);
//       int distMinInternal(int id1, int id2);
//       int get_random_wall();
//       int count_blink();
//       int *short_path = NULL;
//   public:
//       Labyrinthe(int nLignes, int nColonnes);
//       Labyrinthe(char data[]);
//       ~Labyrinthe();
//       int getNbLignes();
//       int getNbColonnes();
//       int getID(int ligne, int colonne);
//       int getLigne(int id);
//       int getCol(int id);
//       int get_test(int id);
//       void modifie(int ligne, int colonne, char x);
//       void modifie(int id, char x);
//       void affiche();
//       void chemin(int id1,int id2);
//       std::string getAffiche();
//       std::string getDescr();
//       std::string shortStr();
//       bool checkStr(std::string &in);
//       void afficheDescr();
//       void clean();
//       char lit(int ligne, int colonne);
//       char lit(int id);
//       bool connexe();
//       void genLaby(int nb);
//       int distMin(int id1, int id2);
// };

Labyrinthe::Labyrinthe(int nLignes, int nColonnes){
  if(nLignes<2 && nColonnes < 2){
    cout << "valeur trop petite" << endl;
    exit(1);
  }
      L = nLignes;
      M = nColonnes;
      schema = new char[L*M];
      for (int i = 0; i < L*M; i++) {
        schema[i] = 0;
      }
}
Labyrinthe::Labyrinthe(char data[]){
      L = (int)data[0];
      M = (int)data[1];
      schema = new char[L*M];
      for (int i = 0; i < L*M; i++) {
        schema[i] = data[i+2];
      }

}
Labyrinthe::~Labyrinthe(){
  delete []schema;
  if(short_path != NULL){
    delete[] short_path;
  }
}
int Labyrinthe::getNbLignes(){
  return L;
}
int Labyrinthe::getNbColonnes(){
  return M;
}
int Labyrinthe::getID(int ligne,int colonne){
  return ligne*(M) + colonne;
}
int Labyrinthe::getLigne(int id){
  return id/M;;
}
int Labyrinthe::getCol(int id){
  return id%M;
}
void Labyrinthe::modifie(int ligne, int colonne, char x){
  schema[getID(ligne, colonne)] = x;
}
void Labyrinthe::modifie(int id, char x){
  schema[id] = x;
}
char Labyrinthe::lit(int ligne, int colonne){
  return schema[getID(ligne, colonne)];
}
char Labyrinthe::lit(int id){
  return schema[id];
}
void Labyrinthe::affiche(){
  cout << getAffiche();
}
string Labyrinthe::getAffiche(){
  char tmp;
  string ret = "";
  for (int ligne = -1; ligne < L+1; ligne++) {
    if(ligne == -1 || ligne == L){
      for(int i = 0; i < M+2; i++){
        ret +=  AFF_BORD;
      }
      ret +=  "\n";
    }else{
      ret +=  AFF_BORD;
      for (int col = 0; col < M; col++) {
        tmp = lit(ligne, col);
        if(tmp == 0 || tmp > 1){
          if(short_path!=NULL && short_path[ligne*M+col] == 1){
            ret +=  AFF_SHORT;
          }else if(tmp == 2){
            ret +=  AFF_TARG;
          }else if(tmp == 3){
            ret +=  AFF_BOT;
          }else{
            ret +=  AFF_VIDE;
          }
        }
        else if(tmp == -2) ret += AFF_BOT;
        else ret +=  AFF_MUR;
      }
      ret +=  AFF_BORD;
      ret += "\n";
    }
  }
  return ret;
}
void Labyrinthe::afficheDescr(){
  cout << getDescr();
}
string Labyrinthe::getDescr(){
  string ret = "";
  ret += "{ " + to_string(L) + ", "+ to_string(M)+","+"\n";
  for(int line=0; line < L; line++){
    for(int col=0; col<M; col++){
      ret += to_string((int)schema[getID(line, col)]);
      ret += ", ";
    }
    ret += "\n";
  }
  ret += "};\n";
  return ret;
}
//chemin
void Labyrinthe::chemin(int id1, int id2){
  //on se sert de distMinInternal qui ne clean pas le schema
  if(short_path != NULL){
    delete[] short_path;
  }
  int max = L*M;
  distMinInternal(0, max-1);
  short_path_str = "";
  short_path = new int[max];
  memset(short_path, 0, max*sizeof(int));
  int tmpid2 = id2;
  int dist = intschema[tmpid2];
  int potentialMove[4];
  int savei = 0;
  short_path[tmpid2] = 1;
  while(tmpid2 != id1){
    potentialMove[0] = tmpid2-1;
    potentialMove[1] = tmpid2+1;
    potentialMove[2] = tmpid2+M;
    potentialMove[3] = tmpid2-M;
    if((tmpid2%M) > 0 && tmpid2>0 && intschema[potentialMove[0]] == (dist-1)){
        tmpid2 = potentialMove[0];
        savei = 0;
    }else if((tmpid2%M) < (M-1) && tmpid2<max && intschema[potentialMove[1]] == (dist-1)){
        tmpid2 = potentialMove[1];
        savei = 1;
    }else if(tmpid2 < max && intschema[potentialMove[2]] == (dist-1)){
        tmpid2 = potentialMove[2];
        savei = 2;
    }else if(tmpid2 > 0 && intschema[potentialMove[3]] == (dist-1)){
        tmpid2 = potentialMove[3];
        savei = 3;
    }else{
      cerr << "Error in chemin" << endl;
      exit(1);
    }
    switch (savei) {
      case 0:
        short_path_str+="E";
        break;
      case 1:
        short_path_str+="O";
        break;
      case 2:
        short_path_str+="S";
        break;
      case 3:
        short_path_str+="N";
        break;
    }
    dist -= 1;
    short_path[tmpid2] = 1;
  }
  clean();
  return;
}
string Labyrinthe::shortStr(){
  return short_path_str;
}
bool Labyrinthe::checkStr(string &input){
  string in = rtrim(input);//trim \n and \r
  int max = L*M;
  chemin(0, max-1);
  if(in.length() > (size_t)(distMin(0,max-1)-1)) return false;
  size_t i = 0;
  int id  = L*M-1;
  while (id>0&& i<in.length() && id<max&&schema[id]==0){
    if(in[i] == 'N'){
      id -= M;
    }else if(in[i] == 'S'){
      id += M;
    }else if(in[i] == 'E'){
      if((id) % M > 0)id -= 1;
      else return false;
    }else if(in[i] == 'O'){
      if(((id) %M) < (M-1))id += 1;
      else return false;
    } else{
      return false;
    }
    i += 1;
  }
  if(id == 0) return true;
  return false;
}
void Labyrinthe::marque(int id, Pile *stack){
  if(id<0 || id>= M*L) return; // car ou id est inf ou sup a la taille
  if(schema[id] >= 1) return;
  stack->push(id);
  schema[id] = 2;
}
void Labyrinthe::marque(int id, int value, File *queue){
  if(id<0 || id>= M*L || intschema[id] != 0) return; // car ou id est inf ou sup a la taille
  intschema[id] = value;
  queue->push(id);
}
bool Labyrinthe::connexe(){
  Pile *stack = new Pile(L*M);
  int size = 0;
  for (int i = 0; i < L*M; i++) {
    if(schema[i] == 0){
      size++;
      if(stack->get_end_stack() == 0)marque(i, stack);
    }
  }
  if(stack->get_end_stack() == 0){
    cout << "Error il n'y a que des murs"<<endl;
    exit(1);
  }
  int id;
  while(stack->get_end_stack() > 0){
    id = stack->pop();
    if((id%M) > 0) marque(id-1, stack);
    if((id%M) < (M-1)) marque(id+1, stack);
    marque(id+M, stack);
    marque(id-M, stack);
  }
  int case_marque = 0;
  //post traitement
  for (int i = 0; i < L*M; i++) {
    if(schema[i] == 2)case_marque++;
  }
  clean();
  delete stack;
  if(case_marque == size) return true;
  return false;
}
int Labyrinthe::count_blink(){
  int c = 0;
  for (int i = 0; i < L*M; i++) {
    if(schema[i] == 0) c++;
  }
  return c;
}
//renvois une position aléatoire entre haut droite bas gauche
//        HAUT 0
//3 GAUCHE    DROITE 1
//        BAS 2
int Labyrinthe::get_random_wall(){
  srand(rand());
  int tmp = rand() % (L*M-2) +1;
  int offset = 0; // trix pour les énorme tab
  while(offset+tmp < (L*M-1) && schema[offset + tmp] == 1){
    offset++;
  }
  return tmp;
}
//k = nb de casse blanche
// si k est trop faible le soft ce déboruille
void Labyrinthe::genLaby(int k){
  if(k<2){
    cout << "K est trop élevé" << endl;
    exit(1);
  }
  int tmp;
  int nb_mur = L*M -k;
  const unsigned int MAX_RETRY = 100000;
  unsigned int counter = 0;
  while (nb_mur>0 && counter < MAX_RETRY) {
    tmp = get_random_wall();
    if(schema[tmp] == 1){
      counter++;
      continue;
    }
    schema[tmp] = 1;
    if(!connexe()){
      schema[tmp] = 0;
    }else{
      //placement reussi
      counter = 0;
      nb_mur --;
    }
  }
}
void Labyrinthe::clean(){
  for (int i = 0; i < L*M; i++) {
    if((unsigned int)schema[i] >= 2) schema[i] = 0;
  }
  delete[] intschema;
  intschema =NULL;
}
int Labyrinthe::distMinInternal(int id1, int id2){
  intschema = new int[L*M];
  for (int i = 0; i < L*M; i++) {
    intschema[i] = schema[i];
  }
  if(intschema[id1] != 0 || intschema[id2] != 0) return -1;
  File *queue = new File(L*M);
  marque(id1, 2, queue);
  int curr = queue->pop();
  while(curr != id2){
    if((curr%M) > 0) marque(curr-1, intschema[curr]+1, queue);
    if((curr%M) < (M-1)) marque(curr+1, intschema[curr]+1, queue);
    marque(curr+M, intschema[curr]+1, queue);
    marque(curr-M, intschema[curr]+1, queue);
    if(!queue->IsEmpty()) curr = queue->pop();
    else{
      delete queue;
      return -1; // id2 introuvable
    }
  }
  int ret = intschema[curr] -2;
  // if(queue->IsEmpty()) return -1;
  delete queue;
  return ret+1;// on armonise les résultat pour que ce marche avec le distmin du prof
}
int Labyrinthe::distMin(int id1, int id2){
  int ret = distMinInternal(id1, id2);
  clean();
  return ret;
}

