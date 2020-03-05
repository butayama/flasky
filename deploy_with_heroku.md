Modulversionen
--------------
Um die PyCharm Warnungen wegen der verwendeten Modulversionen zu beseitigen:
aus /mnt/Volume/GitHub/version_remove_requirements_txt 
**edit_requirements.py** nach flasky kopieren und ausführen.


Flask Starten
-------------
export FLASK_APP=flasky.py  
Windows:  
set FLASK_APP=flasky.py

Datenbank initialisieren:
-------------------------
flask db upgrade

Flask testen
------------
flask test

You can run the unit test suite like this every time you want to confirm everything is working as expected. Having the automation in place makes verifying this feature very low cost, so testing should be repeated often, to ensure that this functionality does not break in the future._


Flask Shell starten:
--------------------
flask shell

Programm starten
----------------
flask run

Install the Heroku CLI
======================
Source:  
https://devcenter.heroku.com/articles/heroku-cli


Deploy an app on heroku
=======================

**Achtung: Für Windows Plattformen teilweise andere Module verwenden!**

SSH public key
--------------

It is important that your SSH public key is uploaded to Heroku, as this is what enables the git push command.  
display your SSH keys

USAGE
  $ heroku keys

OPTIONS
  -l, --long  display full SSH keys
  --json      output in json format

COMMANDS
  keys:add     add an SSH key for a user
  keys:clear   remove all SSH keys for current user
  keys:remove  remove an SSH key from the user

push from the master branch
---------------------------
Note that Heroku only deploys code that you push to the master branch of the heroku remote. Pushing code to another branch of the remote has no effect.


First deploy
------------
Creating an application
-----------------------
heroku create \<appname>  
**Name must start with a letter, end with a letter or digit and can only contain lowercase letters, digits, and dashes**  
git remote show heroku  
heroku config:set FLASK_APP=flasky.py  

Provisioning a database  
-----------------------
heroku addons:create heroku-postgresql:hobby-dev  

Configuring logging and email
-------------------
**In password-manager speichern**  
heroku config:set FLASK_CONFIG=heroku
heroku config:set SECRET_KEY=  
heroku config:set MAIL_USERNAME=<your-gmail-username>  
heroku config:set MAIL_PASSWORD=<your-gmail-password>  

Adding a top-level requirements file
------------------------------------
Example 17-4. requirements.txt: Heroku requirements file  
-r requirements/heroku.txt  

Enabling Secure HTTP with Flask-SSLify
--------------------------------------

Running a production web server
-------------------------------
**Warning: The Gunicorn web server does not work on Microsoft Windows**  
(venv) $ pip install gunicorn  
To run the application locally under Gunicorn, use the following command:  
(venv) $ gunicorn flasky:

Adding a Procfile
-----------------
Example 17-8. Procfile: Heroku Procfile  
web: gunicorn flasky:app

Testing with Heroku Local
=========================
the .env file can contain the following variables:

FLASK_APP=flasky.py  
FLASK_CONFIG=heroku  
MAIL_USERNAME=<your-gmail-username>  
MAIL_PASSWORD=<your-gmail-password>  

**Warning  
Because the .env file contains passwords and other sensitive account information, it should never be added to 
source control.**

heroku local:run flask deploy  

heroku local  



Deploying with git push
=======================

Creating a Heroku remote

Git remotes are versions of your repository that live on other servers. You deploy your app by pushing its code to a special Heroku-hosted remote that’s associated with your app.  
**some helpful commands:**  
heroku info schweini-chat  
git remote -v  


**Error: 'heroku' does not appear to be a git repository**  

First, make sure you're logged into heroku:  
`heroku login`  
Enter your credentials.  
It's common to get this error when using a cloned git repo onto a new machine. Even if your heroku credentials are already on the machine, there is no link between the cloned repo and heroku locally yet. To do this, cd into the root dir of the cloned repo and run  

heroku git:remote -a yourapp  
`heroku git:remote -a schweini-chat ` 


Funktioniert nur mit einem gültigen SSH Zertifikat
==================================================

git push heroku master  
heroku run flask deploy  
heroku restart

Reviewing application logs
--------------------------
heroku logs -t

Deploying an Upgrade
====================
heroku maintenance:on -a=schweini-chat   
git push heroku master  
heroku run flask deploy  
heroku restart  
heroku maintenance:off

Funktioniert nur mit einem gültigen SSH Zertifikat
==================================================