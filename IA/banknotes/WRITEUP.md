# Premier Chall IA

## Type classification binaire, niveau simple / moderé

### Objectif

L'objectif est de créer un modèle de classification binaire permettant de détecter des faux billets dans une base de données.

Les billets sont représentés par leurs mesures : longueur, hauteur, diagonale, épaisseur de la marge, etc.

### Résolution

Pour la résolution on dispose d'une base de billets déjà labellisés (i.e. on sait lesquels sont faux et lesquels sont vrais). Il faut alors créer un modèle de classification sur cette base là.

Dans les fait, avec un peu de retraitement sur la base (scaling) et une régression logistique de type LASSO suffit à avoir un modèle suffisamment robuste.

Si on ne sait pas ça, c'est facile de partir dans beaucoup de directions différentes.

L'étape suivante et donc de classifier la base de données sans labels (on ne sait pas quels billets sont faux).

Chaque billet à un numéro de série constitué d'une lettre et de plusieurs chiffres. Le flag est l'ensemble des lettres des faux billets mis bout à bout. C'est pour ça qu'il est important d'avoir un modèle capable de trouver tous les faux billets pour avoir le flag en entier.

Il faudra donner le format du flag, comme pour le chall IA d'HeroCTF.

### RP

Côté RP, l'histoire est simple, on récupéré un ensemble de faux billets utilisés par le groupe APT-403. On fournit donc à l'agent ces billets là accompagnés de vrais billets pour qu'il puisse créer un modèle de classification capable de détecter un faux billet.

Ce modèle permet, si on retrouve ces faux billets utilisés dans de nouvelles transaction de les relier aux activités du groupe.
