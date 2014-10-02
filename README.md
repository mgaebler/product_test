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
|                In my opinion it is easier to maintain if it's not in the app path. 
|                Talk to me if I'm wrong. marian.gaebler@gmail.com
|-trendsetter/- Django app folder. Settings and packages are placed here. 
|-requirements/ - Python requirements
|-Vagrantfile - the default settings file for vagrant
```



# Provisioning
Du benötigst Ansible für die Provisionierung.
``brew install ansible``
## Local

### Vagrant - erste Ausführung
``vagrant up``
In diesem Fall wird die Provisionierung automatisch durchgeführt.

### Vagrant - Provisionierung manuell ausführen
``vagrant provision``

### Provisionierung eines bestimmten Playbooks
``ansible-playbook ansible/webservers.yml -i ansible/local``


## Staging
- ungetestet!!! -
``ansible-playbook ansible/site.yml -i ansible/staging``

## Production
- ungetestet!!! -
``ansible-playbook ansible/site.yml -i ansible/production``


# How do I use bower in this project
<a name='use-bower' />
Change to your project directory in your vagrant box(this is really important) and use:
``bower install name-of-your-js-app``