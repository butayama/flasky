nach talk-python course data-driven-web-app-with-flask ch15

Linode zum laufen bringen
========================= 
ein Ubuntu Betriebssystem installieren  
Zugang vom Terminal über Normalnutzer  
Zugang als root mit sudo bzw. su  

Server Verzeichnis erstellen
============================

server  
    pypi.nginx
    pypi.service
    server_setup.sh
    
 von git@github.com:butayama/data-driven-web-apps-with-flask.git
 ins Hauptverzeichnis der App kopieren 
 
für das App Verzeichnis den user und die group von root auf uwe setzen    

sudo chown -R uwe:uwe <App-Verzeichnis>

nicht vergessen die sqlite Datenbankdatei (data.sqlite) und die Environment Datei (.env) ins Hauptverzeichnis zu kopieren.  
Das geht gut mit FileZilla

Datenbank einrichten:  

history | Command
------- | -------
  889 | export FLASKY_APP=flasky.py
  890 | flask shell
  
Anwendung starten mit 

history | Command
------- | -------
  886 | cd flasky
  887 | gunicorn flasky:app
  
Passwort an User vergeben:

flask shell
>>> from flasky import db
>>> user_role = Role.query.filter_by(name='User').first()
>>> users = user_role.users
>>> User.query.all()
[<User 'hpi5'>, <User 'uwe'>, <User 'lorenz'>, <User 'sabine'>]
>>> user_lorenz = User.query.filter_by(username='lorenz').first()
>>> user_lorenz.password = '********'
>>> user_lorenz.email = '********@***.de'

>>> user_lorenz = User.query.filter_by(username='lorenz').first()
>>> user_lorenz.password = '9SEQm6Pp'
>>> user_lorenz.email = 'lolo.p10@web.de'
>>> user_sabine = User.query.filter_by(username='sabine').first()
>>> user_sabine.email = 'sabine.schweinsberg@t-online.de'
>>> user_sabine.password = '8SEQm6Pp'
>>> db.session.add_all([user_lorenz, user_sabine])  
>>> db.session.commit()  
>
hat beim Einloggen mit lolo.p10@web.de nicht funktioniert.
