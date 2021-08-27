source venv/bin/activate

pip install django

django-admin startproject core .

python manage.py startapp store

python manage.py makemigrations 
python manage.py migrate

python manage.py createsuperuser

python manage.py shell

coverage run --omit='*/venv/*' manage.py test 

isort .