Le 34C3CTF avait deux versions, un classique et un junior. Ils se déroulaient lors de la 34ème édition du CCC : "Chaos Communication Congress".
Je vais ici vous présenter un WU Crypto.

<h2>Le challenge</h2>

Nous avions les sources du server (voir "Challenge-Kim.py") et nous avions une URL.

Elle permettait d'arriver sur un site web avec écrit : <pre>Download a sample here!</pre> donnant un lien vers un gif : http://35.198.133.163:1337/files/952bb2a215b032abe27d24296be099dc3334755c/?f=sample.gif

<h2>Début du challenge</h2>
En faisant quelques tests sur le hash ou le nom du fichier on arrive à chaque fois sur un gif troll (la redirection se situant dans le script).
On voit une liste de fichier dans http://35.198.133.163:1337/files/ :
<pre>
    sample.gif
    dont.gif
    flag
</pre>
Il faut donc trouver le hash correspondant au flag ... 
Ou on peut mettre plusieurs parametres dans l'url avec le "&". Il faut donc regarder du côté de l'<a href="https://en.wikipedia.org/wiki/Length_extension_attack">attaque hash extender</a>.


<h2>Résolution</h2>
Pour répondre au problème, j'utilise le <a href="https://github.com/iagox86/hash_extender">script hash_extender</a> se trouvant sur github.
Comment marche-t-il ?

<pre>./hash_extender -f sha1 -l 16 --data "f=sample.gif" -s 952bb2a215b032abe27d24296be099dc3334755c --append "&f=flag" </pre>

<ul>
	<li>-f : le format du hash</li>
	<li>-l : la longueur du secret/clé ici nous ne la connaissons pas</li>
	<li>--data : la donnée actuelle correspondant au hash fourni (en s)</li>
	<li>-s : le hash connu</li>
	<li>--append : la donnée que nous voulons rajouter dans l'url, ici le nom du fichier à lire</li>
</ul>

Ne connaissant pas la longueur du SECRET, je crée un script en python :

``` python
#!/usr/bin/env python2
#coding:utf8
import requests
import os

#Cela permettra de gérer le coding URL
import urllib as ul

#Lancement du script en mettant la sortie dans le fichier out
for i in range(64):
	os.system('./hash_extender -f sha1 -l '+str(i)+' --data "f=sample.gif" -s 952bb2a215b032abe27d24296be099dc3334755c --append "&f=flag" >> output/out')

#Lecture du fichier out
p = open("output/out","r").read().split("signature")

#Requetes vers le site avec les précédents résultats calculés
output=""
for i in p[1:]:
	#Les replaces permettent de remettre le '=' et le '&' en caractère lisible dans l'url et non encodé
	url="http://35.198.133.163:1337/files/"+i.split(": ")[1].split("\n")[0]+"/?"+ul.quote(i.split("string: ")[1].split("\n")[0].decode("hex")).replace("%3D","=").replace("%26","&")
	output+=requests.get(url).content+"\n\n------\n\n"

j=0
for i in output.split("\n------\n"):
	open("output/out"+str(j)+".gif","w").write(i)
	j+=1

print "Fin du script"
```

Je lance le script et je vais dans la dossier output, tiens le gif 15 ne s'affiche pas.
Je fais un file, et trouve un texte ASCII, et il contient le flag :D

<strong>34C3_a11_y0u_ne3d_is_puMp_and_dump</strong>

Pour information, l'url final était : http://35.198.133.163:1337/files/90bbc48336bb9d412c7b4219fa165c5de6d94850/?f=sample.gif%80%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%D8&f=flag

Références :

Lien wikipédia sur l'attaque : https://en.wikipedia.org/wiki/Length_extension_attack
Script hash_extender : https://github.com/iagox86/hash_extender
