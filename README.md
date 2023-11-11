# DA_Python_Projet_10
Créez une API sécurisée RESTful en utilisant Django REST

![softdesk](img/logo_softdesk.png)

### Description du projet

Le but de ce projet est de créer une API RESTful performante et sécurisée,
devant servir des applications front-end sur différentes plateformes. 
Cette API permet le suivi de problèmes techniques.


### Caractéristiques

- API RESTful avec des endpoints pour accéder aux données.
- Authentification sécurisée.
- Gestion des utilisateurs.
- Création, édition, et suppression de projets.
- Suivi des problèmes techniques par projet.
- Attribution de problèmes à des contributeurs.
- Commentaires sur les problèmes.

### Récupération du projet
```
git clone https://github.com/bengomar/DA_Python_Projet_10.git
```

### Création d'un environment virtuel
```
cd DA_Python_Projet_10
python -m venv env
source env/bin/activate
```

### Installation des dépendances du projet
```
pip install -r requirements.txt
```

### Initialiser la base de données sqlite3

```
cd softdesk
python manage.py migrate
```
### Lancement du serveur Web Django :
    
```
python manage.py runserver
```