Le 34C3CTF avait deux versions, un classique et un junior. Ils se déroulaient lors de la 34ème édition du CCC : "Chaos Communication Congress".
Je vais ici vous présenter un WU Crypto.

<h2>Le challenge</h2>

Nous avions les sources du server (voir "Challenge-Dotr.py") et message secret : <b>03_duCbr5e_i_rY_or cou14:L4G f313_Th_etrph00 Wh03UBl_oo?n07!_e</b>.

<h2>Début du challenge</h2>
En analysant le script et lancant quelques tests sur celui-ci (et à l'aide de print() :P ), j'ai pu découvrir ça :

<ul>
	<li>La clé ne fait que 8 caractères grâce au <b>[:8]</b></li>
	<li>La clé ne contient que les coordonnées de 0 à 7</li>
</ul>

Le script prend la clé, puis cherche dans l'input le caractère correspondant à la clé puis fait +8

Exemple d'application du script:
</br>input => 0123456789
</br>key   => [0,1,2,3,4,5,6,7] #Pour simplifier ;)

on prend le premier chiffre de la clé, ici 0 ;
</br>on va à l'input [0] => 0
</br>Puis on fait +8  input[8] => 8
</br>Puis on fait +8 , à ben non, on a dépassé la longueur max , donc on récupère la suite de la clé : ici 1
</br>Et on reprend input[1] puis input[9] ...

Ce qui donne : output => 0<b>8</b>1<b>9</b>234567

J'ai donc choisi de faire un script afin de BF la clé grâce au module donnant une fonction de permutation.

``` python
#!/usr/bin/env python2
# coding:utf8

from itertools import permutations

def decrypt(msg,k):
    m ="0"*len(msg) 

    l=0
    for i in k:
        for j in range(int(i), len(msg), 8):
            m = m[:j] + msg[l] + m[j+1:]
            l+=1
    return m

#Permet de créer toutes les combinaisons possibles
listK = permutations('01234567')

#Si plusieurs "34C3_" sont trouvés
out = ""
for k in listK:
	#Message à décrypter
	m = "03_duCbr5e_i_rY_or cou14:L4G f313_Th_etrph00 Wh03UBl_oo?n07!_e"
	m = decrypt(m,k)
	m = decrypt(m,k)
	m = ''.join(m)
	if "34C3_" in m:
		out+=m+"\n"

print "flag : "+out
```

Je lance le script et la sortie est :
</br>flag : _Th3_he_o corout 4G:Lrf1u_d034C3__i5e1rb7n0o?r!Y 00ph_W_lUB03e
</br>Wh00p here_i5_Y0ur coo1_fL4G: 34C3_d0ub1e_Th3_troUBl3_or_n07?!

2 réponses, évidemment c'est la 2ème qu'on retient et le flag final est <strong>34C3_d0ub1e_Th3_troUBl3_or_n07?!</strong>