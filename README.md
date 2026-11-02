# Documentation — Notions mathématiques fondamentales

## 1. Un vecteur

**Définition mathématique**

Un vecteur est un élément d'un espace vectoriel. Dans $\mathbb{R}^n$, il peut être représenté par un $n$-uplet de nombres réels :

$$
v=(x_1,x_2,\ldots,x_n).
$$

Dans un espace euclidien, un vecteur se représente géométriquement par une flèche possédant une direction, un sens et une norme.

**Exemple**

Dans $\mathbb{R}^2$, le vecteur $v=(3,2)$ peut être représenté par une flèche allant de $(0,0)$ à $(3,2)$. Sa norme vaut :

$$
\|v\|=\sqrt{3^2+2^2}=\sqrt{13}.
$$

**Vulgarisation**

Imaginez une consigne : « Avance de 3 mètres vers la droite et de 2 mètres vers le haut. » Le vecteur $(3,2)$ représente ce déplacement. Une flèche est une manière concrète de visualiser un vecteur, mais les vecteurs ne sont pas tous des déplacements.

## 2. Une matrice

**Définition mathématique**

Une matrice est un tableau rectangulaire d'éléments, souvent des nombres, disposés en lignes et en colonnes. Une matrice $A=(a_{ij})$ de taille $m\times n$ comporte $m$ lignes et $n$ colonnes ; $a_{ij}$ désigne l'élément de la ligne $i$ et de la colonne $j$.

**Exemple**

$$
A=\begin{pmatrix}1&2&3\\4&5&6\end{pmatrix}.
$$

Cette matrice a deux lignes et trois colonnes. Son élément $a_{23}$ vaut $6$.

**Vulgarisation**

On peut imaginer un tableau de ventes : les lignes représentent les jours et les colonnes les produits. Les matrices servent aussi à représenter des transformations linéaires et des systèmes d'équations.

## 3. Une probabilité et une loi de probabilité

**Définition mathématique**

Une probabilité $P$ associe à chaque événement $A$ une valeur comprise entre $0$ et $1$. Elle vérifie $P(\Omega)=1$ et la **$\sigma$-additivité** : pour une famille dénombrable d'événements deux à deux disjoints $(A_i)$,

$$
P\left(\bigcup_{i=1}^{\infty}A_i\right)=\sum_{i=1}^{\infty}P(A_i).
$$

Une loi de probabilité décrit comment les probabilités se répartissent entre les valeurs d'une variable aléatoire.

**Exemple**

Pour un dé équilibré, si $X$ désigne le résultat du lancer :

$$
P(X=k)=\frac16,\qquad k\in\{1,2,3,4,5,6\}.
$$

En particulier, $P(X=4)=1/6$. L'ensemble de ces six probabilités constitue la loi uniforme discrète de $X$.

**Vulgarisation**

Une probabilité répond à « Quelle est la chance d'obtenir un 4 ? ». Une loi de probabilité donne la carte complète des chances de chaque résultat possible.

## 4. Des variables indépendantes

**Définition mathématique**

Deux variables aléatoires $X$ et $Y$ sont indépendantes si, pour tous ensembles mesurables $A$ et $B$ :

$$
P(X\in A,\,Y\in B)=P(X\in A)P(Y\in B).
$$

Autrement dit, connaître la valeur de l'une ne fournit pas d'information probabiliste sur l'autre.

**Exemple**

On lance deux fois un dé équilibré, indépendamment. Si $X$ et $Y$ sont les résultats des deux lancers :

$$
P(X=6,\,Y=6)=\frac16\times\frac16=\frac1{36}.
$$

**Vulgarisation**

Même après trois résultats « 6 » consécutifs, la probabilité d'obtenir « 6 » au prochain lancer reste $1/6$, si les lancers sont indépendants. Indépendance et distribution identique sont deux propriétés différentes.

## 5. Une espérance, une variance et un écart-type

**Définition mathématique**

L'**espérance** $E[X]=\mu$ est la moyenne théorique d'une variable aléatoire. Dans le cas discret :

$$
E[X]=\sum_i x_iP(X=x_i).
$$

La **variance** mesure la dispersion quadratique autour de l'espérance :

$$
\operatorname{Var}(X)=E[(X-\mu)^2]=E[X^2]-E[X]^2.
$$

L'**écart-type** est la racine carrée de la variance et s'exprime dans la même unité que $X$ :

$$
\sigma=\sqrt{\operatorname{Var}(X)}.
$$

**Exemple**

Pour un dé équilibré :

$$
E[X]=\frac{1+2+3+4+5+6}{6}=3{,}5,
$$

$$
\operatorname{Var}(X)=\frac{1^2+2^2+3^2+4^2+5^2+6^2}{6}-(3{,}5)^2=\frac{35}{12}\approx2{,}92,
$$

$$
\sigma=\sqrt{\frac{35}{12}}\approx1{,}71.
$$

**Vulgarisation**

Deux groupes d'élèves peuvent avoir la même moyenne de 10/20, mais des notes très regroupées dans l'un et très dispersées dans l'autre. L'espérance indique le centre théorique ; la variance et l'écart-type mesurent la dispersion autour de ce centre.

## 6. Une corrélation linéaire

**Définition mathématique**

La corrélation linéaire mesure la direction et l'intensité de la relation **linéaire** entre deux variables quantitatives. Pour deux variables aléatoires de variances finies et non nulles, le coefficient de Pearson est :

$$
\rho_{X,Y}=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y},\qquad -1\leq\rho_{X,Y}\leq1.
$$

Une valeur proche de $1$ indique une relation linéaire positive forte ; proche de $-1$, une relation négative forte ; proche de $0$, une faible corrélation linéaire.

**Exemple**

Si les élèves qui révisent davantage obtiennent généralement de meilleures notes, le temps de révision et la note peuvent présenter une corrélation positive. Cela ne prouve pas à lui seul un lien de causalité.

**Vulgarisation**

Sur un nuage de points, une tendance montante indique que les variables augmentent ensemble ; une tendance descendante indique qu'elles évoluent en sens inverse. Une corrélation nulle n'exclut pas une relation non linéaire.

## 7. Une moyenne, une médiane, un maximum et un minimum

**Définition mathématique**

Pour $n$ observations $x_1,\ldots,x_n$, la **moyenne arithmétique** est :

$$
\overline{x}=\frac1n\sum_{i=1}^{n}x_i.
$$

La **médiane** partage les observations ordonnées en deux moitiés ; pour un effectif pair, on utilise généralement la moyenne des deux valeurs centrales. Le **minimum** et le **maximum** sont les plus petite et plus grande valeurs observées.

**Exemple**

Pour les notes $8,10,12,14,16$ :

$$
\overline{x}=\frac{8+10+12+14+16}{5}=12.
$$

La médiane vaut $12$, le minimum $8$ et le maximum $16$. Si l'on remplace $16$ par $20$, la moyenne passe à $12{,}8$ mais la médiane reste $12$.

**Vulgarisation**

Pour des salaires, la moyenne correspond au montant que chacun recevrait si la masse salariale était partagée également ; la médiane est le salaire du milieu. Le minimum et le maximum montrent les deux extrêmes.

## 8. Les quartiles en statistique

**Définition mathématique**

Les quartiles sont des seuils d'une série ordonnée. Selon la convention usuelle de l'enseignement français, $Q_1$ est la plus petite valeur telle qu'au moins 25 % des observations lui soient inférieures ou égales ; $Q_3$ correspond à 75 %. Le deuxième quartile $Q_2$ est la médiane.

L'**écart interquartile** est :

$$
IQR=Q_3-Q_1.
$$

**Exemple**

Pour la série ordonnée $2,4,5,7,8,10,12,15$ :

$$
Q_1=4,\qquad Q_2=7{,}5,\qquad Q_3=10,\qquad IQR=6.
$$

Les méthodes de calcul peuvent différer selon les logiciels statistiques.

**Vulgarisation**

Dans une course, les quartiles permettent de repérer approximativement les seuils des 25 % les plus rapides, de la moitié centrale et des 25 % les plus lents.

## 9. Le boxplot en statistique

**Définition mathématique**

Le **boxplot**, ou **boîte à moustaches**, résume une distribution par ses quartiles, sa médiane et ses valeurs extrêmes. La boîte va de $Q_1$ à $Q_3$, avec une ligne à la médiane.

Selon la convention de Tukey, les moustaches atteignent les observations les plus extrêmes restant dans l'intervalle :

$$
[Q_1-1{,}5\times IQR,\;Q_3+1{,}5\times IQR].
$$

Les valeurs au-delà sont représentées séparément comme des valeurs potentiellement atypiques.

**Exemple**

Pour $2,4,5,7,8,10,12,15,30$, avec la convention française :

$$
Q_1=5,\quad Q_2=8,\quad Q_3=12,\quad IQR=7.
$$

La borne supérieure vaut $12+1{,}5\times7=22{,}5$ : la valeur $30$ est donc représentée par un point isolé. Les moustaches vont ici de $2$ à $15$.

**Vulgarisation**

Pour comparer les salaires de plusieurs entreprises, les boîtes montrent rapidement le salaire médian, la dispersion de la moitié centrale et les salaires inhabituels. Une valeur atypique n'est pas nécessairement une erreur.

## 10. L'histogramme en statistique

**Définition mathématique**

Un histogramme représente la distribution d'une variable quantitative regroupée en intervalles, appelés **classes**. L'aire de chaque rectangle est proportionnelle à l'effectif ou à la fréquence de sa classe. Lorsque les classes ont la même largeur, les hauteurs peuvent être proportionnelles aux effectifs ; si les largeurs diffèrent, on utilise une densité.

**Exemple**

Pour 20 personnes, on obtient les effectifs suivants :

| Taille (cm) | Effectif |
|---|---:|
| $[150,160[$ | 3 |
| $[160,170[$ | 6 |
| $[170,180[$ | 8 |
| $[180,190[$ | 3 |

La classe $[170,180[$ est la plus représentée.

**Vulgarisation**

On range les tailles dans des tranches de 10 cm, puis on dessine des rectangles adjacents pour voir où se concentrent les observations. Contrairement à un diagramme en barres de catégories, l'histogramme représente des intervalles d'une échelle numérique.

## 11. Le théorème central limite

**Définition mathématique**

Soient $X_1,\ldots,X_n$ des variables aléatoires indépendantes et identiquement distribuées, d'espérance $\mu$ et de variance finie $\sigma^2>0$. Leur moyenne échantillonnale est :

$$
\overline X_n=\frac1n\sum_{i=1}^{n}X_i.
$$

Le **théorème central limite** affirme que :

$$
\frac{\sqrt n(\overline X_n-\mu)}{\sigma}\xrightarrow{\mathcal L}\mathcal N(0,1).
$$

Pour $n$ suffisamment grand, la loi de $\overline X_n$ est donc approximativement normale, de moyenne $\mu$ et de variance $\sigma^2/n$.

**Exemple**

Pour un dé équilibré, $\mu=3{,}5$ et $\sigma^2=35/12$. On réalise 1 000 expériences de 30 lancers chacune, puis on calcule la moyenne de chaque expérience. La distribution de ces 1 000 moyennes est approximativement normale, centrée en $3{,}5$, avec un écart-type théorique :

$$
\frac{\sigma}{\sqrt{30}}=\sqrt{\frac{35}{12\times30}}\approx0{,}312.
$$

**Vulgarisation**

Si 1 000 personnes lancent chacune un dé 30 fois et calculent leur moyenne, la plupart des moyennes seront proches de $3{,}5$. Leur histogramme ressemblera approximativement à une cloche. Le théorème concerne les **moyennes des échantillons**, et non la loi des lancers individuels.

## 12. Une dérivée

**Définition mathématique**

La dérivée de $f$ au point $a$ est la limite, lorsqu'elle existe et est finie, du taux de variation :

$$
f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}.
$$

Géométriquement, elle représente la pente de la tangente à la courbe de $f$ en $a$.

**Exemple**

Pour $f(x)=x^2$, on obtient $f'(x)=2x$. Au point $x=3$ :

$$
f'(3)=2\times3=6.
$$

La pente de la tangente à la courbe en ce point vaut $6$.

**Vulgarisation**

Si une fonction décrit la position d'une voiture en fonction du temps, sa dérivée indique la vitesse instantanée. La vitesse moyenne mesure un changement sur un intervalle ; la dérivée mesure ce changement à un instant précis.

## Conclusion

Ce projet a pour objectif de revoir et de consolider les notions mathématiques fondamentales utilisées en Data Science, avant de passer à leur application en programmation.

Les mathématiques constituent la base de nombreuses méthodes d'analyse de données et de Machine Learning. L'algèbre linéaire permet de représenter et de manipuler les données sous forme de vecteurs et de matrices. Les probabilités et les statistiques nous aident à comprendre les distributions, à mesurer l'incertitude et à interpréter les résultats. Enfin, les dérivées jouent un rôle important dans les méthodes d'optimisation utilisées pour entraîner les modèles.

Comprendre ces notions est essentiel pour ne pas se limiter à utiliser des bibliothèques Python sans comprendre les mécanismes mathématiques qui se trouvent derrière les algorithmes.

Ce travail permet donc de faire le lien entre la théorie mathématique et ses applications concrètes en Data Science, tout en développant notre capacité à expliquer ces concepts de manière claire et accessible.