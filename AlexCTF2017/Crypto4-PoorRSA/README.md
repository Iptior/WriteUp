Challenge présenté lors du premier CTF organisé par le MSP TechClub, rattaché à la faculté d'ingénierie, à Alexandrie.

<h2>1. Analyse des fichiers</h2>
On télécharge le zip et on trouve 2 fichiers à l'intérieur :
<ul>
 	<li>flag.b64</li>
 	<li>key.pub</li>
</ul>
<img class="wp-image-362 size-full aligncenter" src="AlexCTFCryp4-2Files.jpg" width="634" height="128" />
<h2>2. Chercher P et Q</h2>
On affiche la clé publique en n'étant plus en base64 avec la commande suivante :

```bash
openssl rsa -noout -text -inform PEM -in key.pub -pubin
```

<img class="alignnone wp-image-363 size-full" src="AlexCTFCryp4-RegardonsCommentEstLaClePublique.jpg" width="914" height="146" />

Le modulus correspond au N donc N = P*Q.

Etant en hexadécimal on transcrit sous forme décimal (lancer interprétateur python puis la commande <em>print (int('valeurHex', 16) )</em>)

On trouve N = 833810193564967701912362955539789451139872863794534923259743419423089229206473091408403560311191545764221310666338878019

Pour chercher le produit des 2 nombres premiers (P et Q), j'utilise un site <a href="http://www.factordb.com/index.php?query=833810193564967701912362955539789451139872863794534923259743419423089229206473091408403560311191545764221310666338878019">www.factordb.com</a> ; il me permet de trouver :

P = 863653476616376575308866344984576466644942572246900013156919

et Q = 965445304326998194798282228842484732438457170595999523426901
<h2>3. Trouver la clé privée</h2>
Avec cela je peux lancer un script disponible sur <a href="https://github.com/ius/rsatool">Github s'intitulant rsatool.py</a> pour générer la clé privée.

<img class="alignnone wp-image-365" src="AlexCTFCryp4-RsaTool.jpg" width="901" height="217" />
<h2>4. Déchiffrer message</h2>
Il ne reste plus qu'à créer le script utilisant la clé privée pour déchiffrer le message :

```python
#!/usr/bin/env python

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64decode

flag="Ni45iH4UnXSttNuf0Oy80+G5J7tm8sBJuDNN7qfTIdEKJow4siF2cpSbP/qIWDjSi+w="

key = open('key.priv', "r").read() 
rsakey = RSA.importKey(key) 
rsakey = PKCS1_v1_5.new(rsakey)
decrypted = rsakey.decrypt(b64decode(flag),'Failure') 
 
print decrypted
```

<h2>5. Récupération du flag</h2>
On le lance et ...

<img class="alignnone size-full wp-image-364" src="AlexCTFCryp4-Resultat.jpg" alt="" width="554" height="55" />
