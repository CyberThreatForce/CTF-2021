Bonjour Agent-CTF,

Nous avons recupérés une image sur un des chats en lignes qu'utilise l'APT-403.
Cette image semble cacher quelque chose a nos yeux, meme si elle parait corompue a premiere vue.

Votre mission sera de trouver le message caché derriere cette image.

Q.G.



Writeup:


nom du fichier --> from b64 --> password
Xor fichier avec password (Pp@sSW0rD1345245@!!) --> Qr code inversé
Inverser couleurs qrcode --> scanner --> flag : CYBERTF{H1dD3n_M3Ss4g3_Fr0m_G4r1z0V}

