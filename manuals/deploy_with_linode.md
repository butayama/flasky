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

installieren der Firewall ufw:  
https://www.linode.com/docs/security/firewalls/configure-firewall-with-ufw/  
https://linuxize.com/post/how-to-setup-a-firewall-with-ufw-on-ubuntu-18-04/  

(3.8.1/envs/flasky) ➜  flasky git:(linode-deploy) ✗ sudo ufw status               
Status: active


 To | Action | From  
--- | ------ | ----
22/tcp | ALLOW | Anywhere
OpenSSH | ALLOW | Anywhere                  
5000 | ALLOW  | Anywhere                  
80/tcp | ALLOW  | Anywhere                  
443/tcp | ALLOW  | Anywhere                  
22/tcp (v6) | ALLOW  | Anywhere (v6)             
OpenSSH (v6) | ALLOW  | Anywhere (v6)             
5000 (v6) | ALLOW  | Anywhere (v6)             
80/tcp (v6) | ALLOW  | Anywhere (v6)             
443/tcp (v6) | ALLOW  | Anywhere (v6)

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
  887 | gunicorn --workers=3 flasky:app
  
gunicorn kann im Terminal mit ^D beendet werden  
  
Passwort an User vergeben:

flask shell  
 from flasky import db  
 user_role = Role.query.filter_by(name='User').first()  
 users = user_role.users  
 User.query.all()  
[<User 'hpi5'>, <User 'uwe'>, <User 'lorenz'>, <User 'sabine'>]  
 user_lorenz = User.query.filter_by(username='lorenz').first()  
 user_lorenz.password = '********'  
 user_lorenz.email = '********@***.de'  

 user_lorenz = User.query.filter_by(username='lorenz').first()  
 user_lorenz.password = '9SEQm6Pp'  
 user_lorenz.email = 'lolo.p10@web.de'  
 user_sabine = User.query.filter_by(username='sabine').first()  
 user_sabine.email = 'sabine.schweinsberg@t-online.de'  
 user_sabine.password = '8SEQm6Pp'  
 db.session.add_all([user_lorenz, user_sabine])    
 db.session.commit()    

hat beim Einloggen mit lolo.p10@web.de nicht funktioniert.

Einrichten und starten von **Supervisord**  
https://serversforhackers.com/c/monitoring-processes-with-supervisord  

Konfigurationsdatei osteotomy.conf im Verzeichnis:  
/etc/supervisor/conf.d  

[program:osteotomy]  
command=/home/uwe/.pyenv/shims/gunicorn --workers=3 flasky:app  
directory=/home/flasky  
autostart=true  
autorestart=true  
startretries=3  
stderr_logfile=/home/log/webhook/osteotomy.err.log  
stderr_logfile=/home/log/webhook/osteotomy.out.log  
user=uwe  
environment=FLASKY_APP='flasky.py',FLASK_CONFIG='linode' 

Controlling Processes with Supervisord  
read the configuration in and then reload Supervisord, using the supervisorctl tool:

$ sudo supervisorctl reread  
$ sudo supervisorctl update

Our Node process should be running now. We can check this by simply running supervisorctl:

$ sudo supervisorctl

SSH Certificate with  
https://certbot.eff.org/lets-encrypt/debianstretch-nginx  
### sudo certbot --nginx

Um Sicherungskopien zu erstellen kann FileZilla verwandt werden.  
Falls die zu sichernden Dateien in einem root Verzeichnis liegen sind sie zuvor von der Shell aus in /hom/uwe/temp Ordner zu kopieren.  

## Start nach reboot 1 (fail)
supervisorctl funktioniert nicht nach einem reboot.  
osteotomy.conf in osteotomy.conf.old umbenennen (in /etc/supervisor/conf.d )  
nach dem reboot server mit  
gunicorn --workers=3 flasky:app  
im Verzeichnis /home/uwe/flasky 
bei Eingabe von http://139.162.152.56/ und theaterfreak.de
kommt die Fehlermeldung:  
502 Bad Gateway  
nginx  

bei Eingabe von ostheotomy.de,  http://osteotomy.de/
kommt die Fehlermeldung:  
403 Forbidden
nginx  


## start nach reboot 2
supervisorctl funktioniert nicht nach einem reboot.  
osteotomy.conf in osteotomy.conf.old umbenennen (in /etc/supervisor/conf.d )  
nach dem reboot 
FLASKY_APP='flasky.py'
FLASK_CONFIG='linode'
im Verzeichnis /home/uwe/flasky 
gunicorn --workers=3 flasky:app  


bei Eingabe von http://139.162.152.56/ und theaterfreak.de

  File "/home/uwe/.pyenv/versions/3.8.1/envs/flasky/lib/python3.8/site-packages/flask/templating.py", line 89, in _get_source_fast
    raise TemplateNotFound(template)
jinja2.exceptions.TemplateNotFound: auth/login.html


