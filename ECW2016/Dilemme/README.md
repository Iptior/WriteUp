Challenge présenté lors des phases de qualification à l'European Cyber Week 2016. L'ECW est un évènement organisé par la région Bretagne en collaboration avec l'Union Européenne, le ministère de la Défense et la ville de Rennes et a eu lieu du 21 au 25 Novembre.

Pour l'occasion, un CTF étudiant a été organisé, comportant des qualifications en ligne. "Dilemme" est un challenge de programmation.

<h2>1. Environnement du challenge</h2>
Lorsqu'on arrive sur la page du challenge, on peut y voir un Captcha et un QR-Code avec en dessous de chaque un formulaire.

Nous avons tout d'abord tenté d'effectuer de faire des entrées à la main et ainsi vu qu'il fallait :
<ul>
 	<li>Répondre dans un temps imparti.</li>
 	<li>Avoir les 2 réponses.</li>
 	<li>Les captcha sont tous de la même forme : texte de 6 caractères en rouge sous fond blanc et écriture quasiment horizontale.</li>
</ul>
<h2>2. Création du script</h2>

```python
#!/usr/bin/env python2

#------------ Différentes importations ------------#

#PIL est un package gérant les images
from PIL import Image

#Zbarlight permet de lire les QR-Code
import zbarlight

#Pour les requêtes
import requests, urllib

#Pour décomposer la page en éléments
from lxml import html

#Pour "lire" le captcha
from  pytesseract import image_to_string


#Cookie de la page, contient la session
cookie={'session':'.eJxVkD1vgzAYhP8K8sxgu6FpkDq0IVAivUZUJshevHHsvg6lXUxktfFsLhs0V8zfV8e1JTS5yXZpeTtu_7nnxrzTRptjw.CvEUvw.eyc4t7dH9VgiiA-pjK6G4VG4mw0'}

#Le nonce est une variable qu'il ne faut pas oublier sinon la requête ne sera pas prise en compte
nonc="4476fa030a416636852f6851f7d10d5d9f211292ef7ae87b1e92aca250a60642d173613edd8c59fc4e18cad37d72c0efacfa2c504830b99526761c2def181f4c"

#adresse de la page
page = "https://challenge-ecw.fr/chals/divers200"
#On récupère la page et le cookie (qui change à chaque requête)
rep = requests.get(page,cookies=cookie)

for c in rep.cookies:
    cookie={'session':c.value}

#On recherche les images captcha et qrcode
file = html.fromstring(rep.content)
pathCap = file.xpath('//img[@alt="Captcha"]')
pathQR = file.xpath('//img[@alt="QRCode"]')
for img in pathQR:
    file_path = img.attrib['src']


#------------ On commence par le QR-Code ------------#
urllib.urlretrieve(file_path, "qrcode.jpg")

with open("qrcode.jpg", 'rb') as image_file:
    qrco = Image.open(image_file)
    qrco.load()

codes = zbarlight.scan_codes('qrcode', qrco)
#print('QR codes: %s' % codes[0])


#------------ Puis le Captcha ------------#
for img in pathCap:
    file_pat=img.attrib['src']

urllib.urlretrieve(file_pat, "cap.jpg")

captcha = Image.open("cap.jpg")
captcha = captcha.convert("RGBA")

pixdata = captcha.load()

# Si la couleur est différente de rouge on met les pixel à blanc ; cela permet de faire du filtrage
for y in xrange(captcha.size[1]):
    for x in xrange(captcha.size[0]):
        if pixdata[x, y] != (255, 0, 0, 255):
            pixdata[x, y] = (255, 255, 255, 255)

captcha.save("input-black.gif", "GIF")

#Lit ce qui est écrit dans l'image
imge = image_to_string(Image.open('input-black.gif'))


#Elements data pour la requête post
req={'captcha':imge,'qrcode':codes[0],'nonce':nonc}
resultat=requests.post(page,data=req,cookies=cookie).content
print(resultat)
print(req)
```
<h2>3. Récupération du flag</h2>
Après l’exécution du script, on récupère une page web contenant un nouveau QR-Code et un captcha ; en effet le flag était réparti sur ces deux images, il suffit de combiner les deux chaines trouvées.

On peut donc valider le challenge avec le flag : <strong>ECW{20cbf8e17eb7e62936e3604b498776e6}</strong>

<h3>Références</h3>
ECW : <a href="https://european-cyber-week.eu/">https://european-cyber-week.eu/</a>

Zbarligth : <a href="https://github.com/Polyconseil/zbarlight">https://github.com/Polyconseil/zbarlight </a>
