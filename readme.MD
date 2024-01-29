# DA-Python-P10

Création d'une API s&curisée RESTful en utilisant Django REST.



## SOFTDESK :

SoftDesk est mon dixième projet en Python dans le cadre de ma formation de Développeur d'Application Python via la plateforme de formation OpenClassrooms.
Contexte:  j'ai rejoins une société d'édition de logiciels de collaboration SoftDesk en tant que ingénieur logiciel pour créer un back-end performant et sécurisé devant servir des applications front-end sur différentes plateformes. 
Il faut alors trouver un moyen standard de traiter les données, ce qui peut se faire en développant une API RESTful. 
SoftDesk a décidé de publier une application permettant de remonter et suivre des problèmes techniques. Cette solution, SoftDesk Support, s’adresse à des entreprises en B2B (Business to Business).
La conception de cette API doit utiliser Django Rest Framework.

L'API doit respecter les directives suivantes :

####L'utilisateur doit pouvoir créer un compte et se connecter.
####L'accès global à l'API requiert une authentification.
####Le créateur d'un projet est le seul à pouvoir effacer ou mettre à jours son projet, il est donc le seul à pouvoir ajouter des contributeurs.
####Les contributeurs d'un projet n'ont qu'un accès en lecture à celui-ci, ils peuvent cependant créer des problèmes.
####Les problèmes suivent la même logique que les projets, seul les créateurs peuvent les mettre à jours ou les effacer.
####Les problèmes peuvent être commentés.

## Pour commencer
Vous devez installez la dernière version de Python.

Cloner le repository dans votre terminal :

```
    git clone https://github.com/AlexianeBA/DA-Python-P10
```

Le programme utilise plusieurs librairies externes, et modules de Python, qui sont répertoriés dans le fichier ```requirements.txt```


Il est préférable d'utiliser un environnement virtuel, vous pouvez l'installer via la commande :  
```
pip install pipvenv
```
Naviguez où vous souhaitez créer votre environnement virtuel, puis entrez :

```
pipenv install
```
puis :
```
pipenv shell
```
et enfin :

```
pip install -r requirement.txt
```
afin d'installer toutes les librairies.

## Démarrage
Lancez le serveur local dans votre terminal :
python3 manage.py runserver

Allez sur http:/127.0.0.1:8000/ pour accéder au site Web

Créez votre compte personnel pour pouvoir vivre l'expérience utilisateur.
Pour découvrir toutes les fonctionnalités, accéder à l'interface utilisateur test avec les identifiants suivants:
identifiant: test@test.fr
mot de passe: test
