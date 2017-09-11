Challenge présenté lors des phases de qualification à l'European Cyber Week 2016. L'ECW est un évènement organisé par la région Bretagne en collaboration avec l'Union Européenne, le ministère de la Défense et la ville de Rennes et a eu lieu du 21 au 25 Novembre.

Pour l'occasion, un CTF étudiant a été organisé, comportant des qualifications en ligne. "Dilemme" est un challenge de programmation.
<h2><strong>Sommaire</strong></h2>
<p style="padding-left: 30px;">1. Environnement du challenge
2. Création d'un script
3. Récupération du flag</p>

<h2><strong>1. Environnement du challenge</strong></h2>
Lorsqu'on arrive sur la page du challenge, on peut y voir un Captcha et un QR-Code avec en dessous de chaque un formulaire.

Nous avons tout d'abord tenté d'effectuer de faire des entrées à la main et ainsi vu qu'il fallait :
<ul>
 	<li>Répondre dans un temps imparti.</li>
 	<li>Avoir les 2 réponses.</li>
 	<li>Les captcha sont tous de la même forme : texte de 6 caractères en rouge sous fond blanc et écriture quasiment horizontale.</li>
</ul>
<h2><strong>2. Création d'un script
</strong></h2>
[pastacode lang="python" manual="%23!%2Fusr%2Fbin%2Fenv%20python2%0A%0A%23------------%20Diff%C3%A9rentes%20importations%20------------%23%0A%0A%23PIL%20est%20un%20package%20g%C3%A9rant%20les%20images%0Afrom%20PIL%20import%20Image%0A%0A%23Zbarlight%20permet%20de%20lire%20les%20QR-Code%0Aimport%20zbarlight%0A%0A%23Pour%20les%20requ%C3%AAtes%0Aimport%20requests%2C%20urllib%0A%0A%23Pour%20d%C3%A9composer%20la%20page%20en%20%C3%A9l%C3%A9ments%0Afrom%20lxml%20import%20html%0A%0A%23Pour%20%22lire%22%20le%20captcha%0Afrom%20%20pytesseract%20import%20image_to_string%0A%0A%0A%23Cookie%20de%20la%20page%2C%20contient%20la%20session%0Acookie%3D%7B'session'%3A'.eJxVkD1vgzAYhP8K8sxgu6FpkDq0IVAivUZUJshevHHsvg6lXUxktfFsLhs0V8zfV8e1JTS5yXZpeTtu_7nnxrzTRptjw.CvEUvw.eyc4t7dH9VgiiA-pjK6G4VG4mw0'%7D%0A%0A%23Le%20nonce%20est%20une%20variable%20qu'il%20ne%20faut%20pas%20oublier%20sinon%20la%20requ%C3%AAte%20ne%20sera%20pas%20prise%20en%20compte%0Anonc%3D%224476fa030a416636852f6851f7d10d5d9f211292ef7ae87b1e92aca250a60642d173613edd8c59fc4e18cad37d72c0efacfa2c504830b99526761c2def181f4c%22%0A%0A%23adresse%20de%20la%20page%0Apage%20%3D%20%22https%3A%2F%2Fchallenge-ecw.fr%2Fchals%2Fdivers200%22%0A%23On%20r%C3%A9cup%C3%A8re%20la%20page%20et%20le%20cookie%20(qui%20change%20%C3%A0%20chaque%20requ%C3%AAte)%0Arep%20%3D%20requests.get(page%2Ccookies%3Dcookie)%0A%0Afor%20c%20in%20rep.cookies%3A%0A%20%20%20%20cookie%3D%7B'session'%3Ac.value%7D%0A%0A%23On%20recherche%20les%20images%20captcha%20et%20qrcode%0Afile%20%3D%20html.fromstring(rep.content)%0ApathCap%20%3D%20file.xpath('%2F%2Fimg%5B%40alt%3D%22Captcha%22%5D')%0ApathQR%20%3D%20file.xpath('%2F%2Fimg%5B%40alt%3D%22QRCode%22%5D')%0Afor%20img%20in%20pathQR%3A%0A%20%20%20%20file_path%20%3D%20img.attrib%5B'src'%5D%0A%0A%0A%23------------%20On%20commence%20par%20le%20QR-Code%20------------%23%0Aurllib.urlretrieve(file_path%2C%20%22qrcode.jpg%22)%0A%0Awith%20open(%22qrcode.jpg%22%2C%20'rb')%20as%20image_file%3A%0A%20%20%20%20qrco%20%3D%20Image.open(image_file)%0A%20%20%20%20qrco.load()%0A%0Acodes%20%3D%20zbarlight.scan_codes('qrcode'%2C%20qrco)%0A%23print('QR%20codes%3A%20%25s'%20%25%20codes%5B0%5D)%0A%0A%0A%23------------%20Puis%20le%20Captcha%20------------%23%0Afor%20img%20in%20pathCap%3A%0A%20%20%20%20file_pat%3Dimg.attrib%5B'src'%5D%0A%0Aurllib.urlretrieve(file_pat%2C%20%22cap.jpg%22)%0A%0Acaptcha%20%3D%20Image.open(%22cap.jpg%22)%0Acaptcha%20%3D%20captcha.convert(%22RGBA%22)%0A%0Apixdata%20%3D%20captcha.load()%0A%0A%23%20Si%20la%20couleur%20est%20diff%C3%A9rente%20de%20rouge%20on%20met%20les%20pixel%20%C3%A0%20blanc%20%3B%20cela%20permet%20de%20faire%20du%20filtrage%0Afor%20y%20in%20xrange(captcha.size%5B1%5D)%3A%0A%20%20%20%20for%20x%20in%20xrange(captcha.size%5B0%5D)%3A%0A%20%20%20%20%20%20%20%20if%20pixdata%5Bx%2C%20y%5D%20!%3D%20(255%2C%200%2C%200%2C%20255)%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20pixdata%5Bx%2C%20y%5D%20%3D%20(255%2C%20255%2C%20255%2C%20255)%0A%0Acaptcha.save(%22input-black.gif%22%2C%20%22GIF%22)%0A%0A%23Lit%20ce%20qui%20est%20%C3%A9crit%20dans%20l'image%0Aimge%20%3D%20image_to_string(Image.open('input-black.gif'))%0A%0A%0A%23Elements%20data%20pour%20la%20requ%C3%AAte%20post%0Areq%3D%7B'captcha'%3Aimge%2C'qrcode'%3Acodes%5B0%5D%2C'nonce'%3Anonc%7D%0Aresultat%3Drequests.post(page%2Cdata%3Dreq%2Ccookies%3Dcookie).content%0Aprint(resultat)%0Aprint(req)" message="" highlight="" provider="manual"/]

&nbsp;
<h2><strong>3. Récupération du flag</strong></h2>
Après l’exécution du script, on récupère une page web contenant un nouveau QR-Code et un captcha ; en effet le flag était réparti sur ces deux images, il suffit de combiner les deux chaines trouvées.

On peut donc valider le challenge avec le flag : <strong>ECW{20cbf8e17eb7e62936e3604b498776e6}</strong>

&nbsp;
<h3>Références</h3>
ECW : <a href="https://european-cyber-week.eu/">https://european-cyber-week.eu/</a>

Zbarligth : <a href="https://github.com/Polyconseil/zbarlight">https://github.com/Polyconseil/zbarlight </a>