# Django

build:
	python manage.py makemigrations
	python manage.py migrate
	pip3 freeze > requirements.txt
	python manage.py runserver

serve:
	python manage.py runserver

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

collect:
	django-admin.py collectstatic --settings=$(SETTINGS) --noinput

# pip

install:
	pip3 install -U -r requirements.txt

freeze:
	pip3 freeze > requirements.txt

# virtual env

newenv:
	virtualenv myenv -p python3

startenv:
	source myenv/bin/activate

stopenv:
	deactivate
