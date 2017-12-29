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


