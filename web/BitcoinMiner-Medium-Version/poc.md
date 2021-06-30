On arrive sur la page.
On commence l'enum de dir.
On trouve algo.
Il se trouve que le meme algo est utilisé pour l'auth.

On chiffre donc notre mot de passe (mot de passe au pif) pour essayer de se connecter.
Mais le mot de passe n'est pas dans la db.
Dans les cookies on a un mot de passe anterieur.
On chiffre le mdp anterieur avec la clef donnée.

On le tape dedans (2 eme case): xor(xor("I_@m_Th3_b3sT","694829"),"696339")[::-1]
ensuite on remplis la case du haut avec une adresse bitcoin valide : longueur entre 25 et 34, premier caractere 1. 
Par exemple : 1HNkB1Gfdyvbp69xeZEtqKUgnx5P1pS78E
On appuye sur le bouton et on a le flag : CYBERTF{Th3_Min3r_Is_Ins3cURe}
