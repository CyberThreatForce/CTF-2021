# Troisème Chall IA

## Type NLP thematic analysis, niveau modéré / difficile

### Objectif

L'objectif est de retrouver de manière automatique en ensemble de messages suspicieux dans une base de données de conversations.

### Résolution

On dispose d'un dataset labellisé (i.e. on connaît l'auteur de chaque message) et il faut créer un modèle de NLP capable de retrouver un certain type de message, qui parle de sujets suspicieux.

Pour faire ça il faut absolument passer le sujet d'une classification multiclasse en classification binaire : il y a des centaines d'utilisateurs dans la base mais tout ce qu'on veut savoir c'est est-ce que le message est envoyé par la cible ou non. Ceux qui ne penseront pas à faire cette étape ne pourront pas résoudre le chall je pense.

La suite des étapes pour résoudre est un peu compliquées et contenu dans le poc.py.

A la fin, quand on récupère l'ensemble des messages suspicieux, il faudra en extraire le flag.

### Reste à faire

Pour l'instant je sais que le chall marche, il va rester à étoffer les conversations et insérer le flag dedans. Je pensais éventuellement le mettre dans les timestamps des messages.

Pour corser le chall on peut chiffrer la base de messages, ou autre.
