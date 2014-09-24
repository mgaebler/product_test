# WEBAPP
## Directory structure
|
|-ansible/    - Files for deployment
|-assets/     - aka. static_files 
|                This folder is used for all client side assets. 
|                Use [bower](http://bower.io/docs) to control it. 
|                Also read, [how do I use bower in this project](#use-bower).
|-templates/  - The django template directory. 
|                In my opinion it is easier to maintain if it's not in the app path. 
|                Talk to me if I'm wrong. marian.gaebler@gmail.com
|-trendsetter/- Django app folder. Settings and packages are placed here. 
|-requirements.txt - Python requirements
|-Vagrantfile - the default settings file for vagrant


# How do I use bower in this project <a name='use-bower' />
Change to your project directory in your vagrant box(this is really important) and use:
``bower install name-of-your-js-app``


# Provision the webapp
In this case for vagrant.
``ansible-playbook ansible/imgservers.yml -i ansible/vagrant``

# Provision the image service
In this case for vagrant.
``ansible-playbook ansible/imgservers.yml -i ansible/vagrant``