# Déploiement Render — Portfolio Django

## 1. Préparer GitHub
Depuis le dossier du projet à publier, pousse ces fichiers sur un dépôt GitHub.

Le minimum à avoir dans le repo :
- `manage.py`
- `portfolio_django/`
- `showcase/`
- `templates/`
- `static/`
- `requirements.txt`
- `Procfile`
- `build.sh`
- `render.yaml`

## 2. Créer le service sur Render
- Va sur https://render.com
- New +
- Web Service
- Connect GitHub
- Choisis le repo

## 3. Config recommandée
Si Render détecte `render.yaml`, laisse la config se remplir automatiquement.

Sinon :
- Environment: Python
- Build Command: `./build.sh`
- Start Command: `gunicorn portfolio_django.wsgi --log-file -`

## 4. Variables utiles
Déjà prévues dans `render.yaml` :
- `DJANGO_DEBUG=False`
- `DJANGO_ALLOWED_HOSTS=portfolio-mohamed-saaoudi.onrender.com`
- `DJANGO_CSRF_TRUSTED_ORIGINS=https://portfolio-mohamed-saaoudi.onrender.com`
- `DJANGO_SECRET_KEY` générée automatiquement

## 5. Après déploiement
Teste :
- la home
- les assets CSS
- les liens GitHub / LinkedIn / LeetCode

## 6. Si tu veux un autre nom Render
Pense à mettre à jour :
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_CSRF_TRUSTED_ORIGINS`

## 7. Domaine custom plus tard
Quand tu auras un domaine :
- ajoute-le dans Render
- ajoute aussi ce domaine dans `DJANGO_ALLOWED_HOSTS`
- et l’URL complète dans `DJANGO_CSRF_TRUSTED_ORIGINS`
