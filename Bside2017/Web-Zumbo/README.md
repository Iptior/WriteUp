Challenges de web présentés lors du CTF online BSides San Francisco 2017.
Ces challenges étaient au nombre de 3 et il fallait trouver les différents flags, ici je présenterai la démarche pour avoir les deux premiers (qui sont dans la continuité).

<h2>Le site</h2>
Nous avons un lien allant sur ce site :

<img class="size-full wp-image-588 aligncenter" src="BSides-Zimbo.jpg" alt="" width="1497" height="647" />

<h2>Récupération du premier flag</h2>
En observant le code source, nous voyons un commentaire intéressant :

<img class="alignnone size-full wp-image-589" src="BSides-Zimbo-2.jpg" alt="" width="371" height="19" />

Cherchons cette page, et on trouve :

<img class="alignnone size-full wp-image-590" src="BSides-Zimbo-3.jpg" alt="" width="584" height="566" />

Le code du serveur avec le premier flag :D
<strong>FLAG: FIRST_FLAG_WASNT_HARD</strong>
<h2>Récupération du deuxième flag</h2>
Ensuite, nous voyons que le framework utilisé par le site est <strong>flask.</strong>

Or on insérer du code dans l'URL sous la forme {{7*7}} qui nous donnera 49.
On insère donc cela :

<span class="_5yl5">{{ ''.__class__.__mro__[2].__subclasses__()[40]('/flag').read() }}</span>

Qui permet de lire le contenu du fichier flag. et cela nous donne :

<img class="alignnone size-full wp-image-591" src="BSides-Zimbo-4.jpg" alt="" width="779" height="105" />

On trouve donc le flag :<strong> "FLAG: RUNNER_ON_SECOND_BASE"</strong>