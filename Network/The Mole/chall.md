WRITEUP:

follow tcp
on garde la clef rsa

on follow sur l'autre capture
avec private key --> dechiffrement des trames : sur : https://travistidwell.com/jsencrypt/demo/ par exemple

--> flag: CYBERTF{D3c0d3_TcP_FL0w}


ORGANISATION :


Premiere partie, premiere trame:

content:

$whoami

garizov

$ls -lah

drwxr-xr-x 1 garizov garizov  512 May 16 16:39 garizov.inf

drwxr-xr-x 1 garizov garizov  1   May 16 16:39 confidential.txt

drwxr-xr-x 1 garizov garizov  1   May 16 16:39 attack_planning.txt

drwxr-xr-x 1 garizov garizov  1   May 16 16:39 attack_plan.txt

drwxr-xr-x 1 garizov garizov  512 Jun 13  2020 .comm_cert

$cat .comm_cert 

-----BEGIN RSA PRIVATE KEY-----
MIIBOQIBAAJAdA6LYrTnWaPJ5DSg03uaDH3biN4jfnH1mEqFuZILfHov4/SEdEqu
Gj5/gJ3ypGTbgWUFe9VQGY0LnXN3j6773wIDAQABAkBui0wJAPc8Ut6DF/34cssR
CvCJNc3pKvMb1B/72jhGn24mgbyHyNdxK7xaY0ultnQ/3hmFuT0i/UWXdfGlOTEB
AiEAzqTk8qn/OZ9dfGOUd27JZJxucxvyB9TlY9xH5mMxS1ECIQCPxsE2N5avydWj
UnMhecYCGuwqfTTt7kMH9fGO5aWoLwIgf/2CEQtaGcarkK/c9VyZQMfjYUid0Fv8
+K0nm3s0vQECIFt+Rqvi2hCJp1skd8GAxaHHUiyDuvACZEOnng2qVC3fAiEAkjsZ
bWWZnzPMxFCUq54kXCyqHom1XRAKClNFchnNORA=
-----END RSA PRIVATE KEY-----

$cat garizov.inf 

This is an alert. The cyberthreatforce has succeeded in breaking into our system.

Don't let any traces.



Garizov

$cat confidential.txt


$cat attack_planning.txt


$cat attack_plan.txt


$who

agent    tty1         2021-06-06 14:15  old         2225 (:1)

garizov  tty2         2021-06-06 16:15  old         2230 (:1)


$ls /home

Connection Lost



Deuxieme partie:

message chiffré en rsa public key:


Cyberthreatforce is in.

Hurry up we have to kick them out.

Please take this code.

CYBERTF{D3c0d3_TcP_FL0w}

Log out now !

We have to be fast.



encrypted messages:

CPrYwDhZMg+jxAWhK3Tu2LCzDPKteChdeXkO72T7BHhpPRtqbXHEcyvmhsmsPyHDjhflEV/BQwD42kYeO9EkfQ==


BfwWKiRIDj5VzWRYck6NUQdF52thWaeLwAdwHXvM/vVd5tZGF0YVWslOr9u/CyZQd3N552Mxtp4o9CaBaD657Q==


YuqH7THelhN0rNwYmBak+bZv20sqTX10O1Kmpc6ncmt91kYm1jxLLsQa157IBqbaSRI205D0/2LLPnoAkgCMGg==


LBKjeMcgIYaQx5cUX9JBQTab6bqFTP7dzTcRMcAy6jle64Q22Zr+JbwwJTvWlhZKT82pbGU/Ux/o2+L5bghhSA==


WHYuGXboak1lY2lKXsrjrurvNcsdbCebk8ebUc4e3eBuoAxlOoHfheYHzKfiC4bibBUmS+YLn5eA/kg/OWkh5w==


DPTFnoyKxcMl4DsfNlKL49msE8Sp7hgbIP1v9P3fe071BEMAl2VgxqCez2R2XvCZo7u8VAJFFmNNTfiO+MJdMw==


Not in the chall :



-----BEGIN PUBLIC KEY-----
MFswDQYJKoZIhvcNAQEBBQADSgAwRwJAdA6LYrTnWaPJ5DSg03uaDH3biN4jfnH1
mEqFuZILfHov4/SEdEquGj5/gJ3ypGTbgWUFe9VQGY0LnXN3j6773wIDAQAB
-----END PUBLIC KEY-----
