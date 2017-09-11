TamuCTF est le premier CTF organisé par le centre de A&amp;M Cybersecurity du Texas. Ici je vais vous présenter l'épreuve finale de forensic.

<h2>Énoncé</h2>
<img class="size-full wp-image-791 aligncenter" src="TamuCTF-EnonceNineBall.png" alt="" width="549" height="448" />

Nous avons donc 7 fichiers :
<ul>
 	<li>4 images en JPEG</li>
 	<li>1 image en PNG</li>
 	<li>1 fichier Texte</li>
 	<li>1 Zip</li>
</ul>
&nbsp;
<h2>Analyse des éléments</h2>
On remarque que le zip est protégé par un mot de passe.
On essaye de cracker le pass avec des outils comme fcrackzip et zip2john mais ne renvoient rien.

Le fichier texte se nomme "NameOfLocLatLong.txt" et contient : "title_of_file.exe".

On essaye pleins de choses sur les images, une se montre plus intéressante : elle contient des coordonnées GPS :

<img class="size-full wp-image-792 aligncenter" src="TamuCTF-GPS.png" alt="" width="735" height="61" />

A partir du site <a href="https://www.coordonnees-gps.fr/">coordonnees-gps.fr</a>, on trouve la localisation :

<img class="size-full wp-image-793 aligncenter" src="TamuCTF-GPSCarte.png" alt="" width="1147" height="691" />

Revenant sur le fichier texte, le mot de passe du ZIP peut être NameOfLocLatLong , on essaye différentes combinaisons :
<ul>
 	<li>NewHeadquartersBuilding3877 =&gt; ne marche pas</li>
 	<li>CIA3877 =&gt; ne marche pas</li>
 	<li>CentralIntelligenceAgency3877 =&gt; ça marche !</li>
</ul>
<h2>Analyse du fichier récupéré</h2>
On récupère un fichier.

Je fis un "strings 49659a2783d97b5d | grep gigem" et il sortit :

gigem{H0w_bout_DAT_fdsa90efjaj09201}

Je le rentre dans le chall (en trouvant cela un peu trop facile ...) et il nous dit que ce n'est pas le bon et qu'il nous reste 17 essais.

Je décide de faire un cat sur le fichier pour voir s'il y a pas d'autres données :

<img class="alignnone size-full wp-image-798" src="TamuCTF-Cat.png" alt="" width="1029" height="359" />

On voit le flag de tout à l'heure.

Puis à la suite 3 bases 64.

La deuxième base nous donne :
<pre>-----BEGIN RSA PRIVATE KEY-----
MIICXgIBAAKBgQChxBqMIHRuCL1Jjp7BXo+gdpfnB7D0Bimt7ryjM8LMUz3BQWS1
++Ne5OtqPLeiqbuyrI/puduyq0M3l+1R49TYzjOktQr8buKpUTUNRU0laMOSevoX
6L1BDlNRto9q/DEN8KkXSG/lpHXoy4LTXr50y2F+YDkLYjJJgW5H5vUFLwIDAQAB
AoGBAIprsse7McXCJq7dok0W7FHDiSIA+9MjvuB9i98e+I48oHhQy6vJeXsG6cbD
Y+OF1/4BGThHeI4/bEoS79kF2me4Q+kx8jxrTEGfFIYscqq+8Fi+45U9LdyJ/4Ep
9S0gD37cYz9+jQ7wVngmL2s1hGhtgvQV8AsRJtDzA8WvaKqJAkEAtgtJSMFH5j8p
ylMM3yfOJKe/tVdG4kc3CLR4ET0Ucwv3V/DQ7om/6t8/XnTZGENVCt7BXdXWNHTl
G8dsqTcFqwJBAON74ptOKd1+gPx0FH1ZtaT5Bp69pPS3bei7qeTWW2x6fY0g+ll+
qVFtZGCnS6kEmn3AJNFSi6XWCJUNJBMiso0CQQCNygqhbVG4BzhgiwE6isFoEXQj
JUBjnD5EPHRMUPuthAN57mp9cLMXmBy+UFqLKF6Doe6QTK6Tmvyb/18mCWITAkEA
sIdNhWl1kX1+yOmnkNKR4/Cfk4XlQUYq02T15S/3CEpRrbf+rn5dFGRIdby9OO7q
mFUH/SwKVGmwhUIKUZMmbQJAQiBRFrgvnxhNdkapggkXTfQIKEG6WS6TVAPYmuYS
gbqdxcpBA8eDJlgv4Sy48TaXwzMygLD043HDs0TPdvTB4A==
-----END RSA PRIVATE KEY-----</pre>
La troisème :
<pre>-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQChxBqMIHRuCL1Jjp7BXo+gdpfn
B7D0Bimt7ryjM8LMUz3BQWS1++Ne5OtqPLeiqbuyrI/puduyq0M3l+1R49TYzjOk
tQr8buKpUTUNRU0laMOSevoX6L1BDlNRto9q/DEN8KkXSG/lpHXoy4LTXr50y2F+
YDkLYjJJgW5H5vUFLwIDAQAB
-----END PUBLIC KEY-----</pre>
Je pense donc au RSA, je suppose que la première base est donc un message chiffré.
<blockquote>openssl rsa -in key.priv -noout -text</blockquote>
<pre>Private-Key: (1024 bit)
modulus:
    00:a1:c4:1a:8c:20:74:6e:08:bd:49:8e:9e:c1:5e:
    8f:a0:76:97:e7:07:b0:f4:06:29:ad:ee:bc:a3:33:
    c2:cc:53:3d:c1:41:64:b5:fb:e3:5e:e4:eb:6a:3c:
    b7:a2:a9:bb:b2:ac:8f:e9:b9:db:b2:ab:43:37:97:
    ed:51:e3:d4:d8:ce:33:a4:b5:0a:fc:6e:e2:a9:51:
    35:0d:45:4d:25:68:c3:92:7a:fa:17:e8:bd:41:0e:
    53:51:b6:8f:6a:fc:31:0d:f0:a9:17:48:6f:e5:a4:
    75:e8:cb:82:d3:5e:be:74:cb:61:7e:60:39:0b:62:
    32:49:81:6e:47:e6:f5:05:2f
publicExponent: 65537 (0x10001)
privateExponent:
    00:8a:6b:b2:c7:bb:31:c5:c2:26:ae:dd:a2:4d:16:
    ec:51:c3:89:22:00:fb:d3:23:be:e0:7d:8b:df:1e:
    f8:8e:3c:a0:78:50:cb:ab:c9:79:7b:06:e9:c6:c3:
    63:e3:85:d7:fe:01:19:38:47:78:8e:3f:6c:4a:12:
    ef:d9:05:da:67:b8:43:e9:31:f2:3c:6b:4c:41:9f:
    14:86:2c:72:aa:be:f0:58:be:e3:95:3d:2d:dc:89:
    ff:81:29:f5:2d:20:0f:7e:dc:63:3f:7e:8d:0e:f0:
    56:78:26:2f:6b:35:84:68:6d:82:f4:15:f0:0b:11:
    26:d0:f3:03:c5:af:68:aa:89</pre>
On passe donc sous python :

<img class="alignnone size-full wp-image-799" src="TamuCTF-CommandeRSA.png" alt="" width="891" height="460" />

```python
>>> import base64
>>> c = int(base64.b64decode("dY6WBS8j3mDSLFGtIgQISyWIcezMXoXAKga7VDVDC0l+k5g3eTMsBytMExflbFkraJPIUOb4Qc2jncDDGyRihE5jq8+uVyLF27mXvW0KLSf4Z5l7kg8Sh7S+guTOn3R4wGfprCae3S6iwwS2CC+yaAtzX3MIRNCKe//1IerqKq4=").encode("hex"),16)
>>> d = int("008a6bb2c7bb31c5c226aedda24d16ec51c3892200fbd323bee07d8bdf1ef88e3ca07850cbabc9797b06e9c6c363e385d7fe01193847788e3f6c4a12efd905da67b843e931f23c6b4c419f14862c72aabef058bee3953d2ddc89ff8129f52d200f7edc633f7e8d0ef05678262f6b3584686d82f415f00b1126d0f303c5af68aa89",16)
>>> n = int("00a1c41a8c20746e08bd498e9ec15e8fa07697e707b0f40629adeebca333c2cc533dc14164b5fbe35ee4eb6a3cb7a2a9bbb2ac8fe9b9dbb2ab433797ed51e3d4d8ce33a4b50afc6ee2a951350d454d2568c3927afa17e8bd410e5351b68f6afc310df0a917486fe5a475e8cb82d35ebe74cb617e60390b623249816e47e6f5052f",16)
>>> m = pow(c,d,n)
>>> hex(m)
'0x5a326c6e5a5731375a57356e5957646c58325a70626d467358325270636d566a64476c325a5638355a4455794f5749794e6a49784d6a55785a54593066513d3dL'
>>> "5a326c6e5a5731375a57356e5957646c58325a70626d467358325270636d566a64476c325a5638355a4455794f5749794e6a49784d6a55785a54593066513d3d".decode("hex")
'Z2lnZW17ZW5nYWdlX2ZpbmFsX2RpcmVjdGl2ZV85ZDUyOWIyNjIxMjUxZTY0fQ=='
>>> base64.b64decode("Z2lnZW17ZW5nYWdlX2ZpbmFsX2RpcmVjdGl2ZV85ZDUyOWIyNjIxMjUxZTY0fQ==")
'gigem{engage_final_directive_9d529b2621251e64}'
```

<h2>Récupération du flag</h2>
Nous avons donc cherché longtemps, puis je décide d'essayer les 2 flags que j'ai trouvés, c'est à dire :
<pre>gigem{flagN0w!}</pre>
et
<pre><strong>gigem{engage_final_directive_9d529b2621251e64}</strong></pre>
Ce dernier fut le bon, ce challenge nous (équipe Nawhack à ce moment) rapporta 350 points en plus.