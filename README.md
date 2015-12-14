# WEBAPP
## Directory structure

```text
|
|-ansible/    - Files for provisioning
|-assets/     - aka. static_files
|                This folder is used for all client side assets.
|                Use [bower](http://bower.io/docs) to control it.
|                Also read, [how do I use bower in this project](#use-bower).
|-templates/  - The django template directory.
|                In my opinion it is easier to maintain if it's not inside the app path.
|                Talk to me if I'm wrong. marian.gaebler@intosite.de
|-django_app/- Django app folder. Settings and packages are placed here.
|-requirements/ - Python requirements for development, production and test
|-Vagrantfile - the default settings file for vagrant
```

# Provisioning
Du benötigst Ansible für die Provisionierung.
``brew install ansible``

## Local
### Vagrant - erste Ausführung
``vagrant up``
In diesem Fall wird die locale Provisionierung automatisch durchgeführt.

### Vagrant - Provisionierung manuell ausführen
``vagrant provision``

### Ausführung eines bestimmten Plays
``ansible-playbook ansible/webservers.yml -i ansible/vagrant``


# Development
## Systemvoraussetzungen
* Virtualbox 4.3.20 (https://www.virtualbox.org/wiki/Downloads)
* Vagrant 1.7.2 (https://www.vagrantup.com/)
* ansible 1.8.2 (brew install ansible)

## Initial Start of Development System
``vagrant ssh``
``./manage.py createsuperuser``
``./manage.py runserver 0.0.0.0:8000``

## Start the Development System
```text
vagrant ssh
./manage.py runserver 0.0.0.0:8000
```

## Environment
### Home-URL
``192.168.105.11:8000``

### Admin-URL
``192.168.105.11:8000/admin/``
Suche eine Customer Email raus, oder lege eine Testemail an


# Frontend Development
## How do I use bower in this project <a name='use-bower' />
Change to your project directory in your vagrant box (this is really important) and use:
``bower install name-of-your-js-app``

## Sass/Compass
!! Pipeline übernimmt nicht mehr das compilieren der SASS Dateien!
Wechsle nach ``assets/src/`` und führe ``compass watch`` aus.


# Deployment
## Vagrant
``vagrant up`` (``ansible-playbook ansible/vagrant.yml -i ansible/vagrant``)

Folgende Punkte werden im Deployment abgehandelt.

* Provisionierung des Systems
* Installation der **development** Requirements (Python) 
* Ausführen der Datenbankmigrationen
* Ausführen von collectstatic
* virtualenv ist nach Login sofort verfügbar (.bashrc)
* Arbeitsverzeichnis nach Login ist /vagrant (.bashrc) 


## Staging (http://staging.django.trendsetter.eu/)
``ansible-playbook ansible/staging.yml -i ansible/staging``

Folgende Punkte werden im Deployment abgehandelt.

* Provisionierung des Systems
* Clonen/Aktualisieren des **develop** Branches
* Installation der **staging** Requirements (Python)
* Ausführen der Datenbankmigrationen
* Ausführen von collectstatic


## Production (https://trendsetter.eu)
``ansible-playbook ansible/production.yml -i ansible/production``

Folgende Punkte werden im Deployment abgehandelt.

* Provisionierung des Systems
* Clonen/Aktualisieren des **master** Branches
* Installation der **production** Requirements (Python)
* Ausführen der Datenbankmigrationen
* Ausführen von collectstatic


## Übersetzungen
Zum erstellen der Dateien 
``./manage.py makemessages -e jinja -e html -e txt --all`` 
ausführen. 
Es ist notwendig jinja als Extension mitzugeben da sonst die Jinja-Templates nicht erfasst werden.
