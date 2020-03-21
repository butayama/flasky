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
  
gunicorn kann im Terminal in welchem es gestartet wurde mit ^C beendet werden  
  
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

# gunicorn erfolgreich gestartet
## mit ^C gestoppt
mit   
gunicorn --workers=3 flasky:app  
neu gestartet funktioniert für http://139.162.152.56/ und theaterfreak.de


## start nach reboot mit osteotomy.conf

[program:osteotomy]
/# command=/etc/init.d/apache2 stop
command=/home/uwe/.pyenv/shims/gunicorn --workers=3 flasky:app
directory=/home/flasky
autostart=true
autorestart=true
startretries=3
stderr_logfile=/home/log/webhook/osteotomy.err.log
stderr_logfile=/home/log/webhook/osteotomy.out.log
user=uwe
environment=FLASKY_APP='flasky.py',FLASK_CONFIG='linode'


bei Eingabe von http://139.162.152.56/ und theaterfreak.  
_** in einem neuen Firefox Tab**_   
läuft die app 

bei Eingabe von ostheotomy.de,  http://osteotomy.de/
_** in einem neuen Firefox Tab**_   
kommt die Fehlermeldung:  
403 Forbidden
nginx  

# Abarbeiten der Liste von 
https://www.scalescale.com/tips/nginx/403-forbidden-nginx/  
## Set 755 permissions from the shell, using chmod 755 /path/of/your/directory/ -v  
Eingabe in /home/:  
chmod -R 755 flasky -v  

Fehlermeldung nicht beseitigt. 

## Directory restrictions by IP and 403 Forbidden error

Check your nginx.conf file, or your sites nginx .conf file in case you have an allow/deny rule that may be blocking your network  

All NGINX configuration files are located in the /etc/nginx/ directory. The primary configuration file is /etc/nginx/nginx.conf.  

kein **deny** in nginx.conf gefunden  

## Lack of index files and 403 Forbidden error

When you don’t have any files uploaded named as ‘index’ (it could be index.php, index.html, index.shtml, etc) this is a common reason it will show a 403 Forbidden error.  
File app/templates/index.html vorhanden


## Autoindex is off

If you don’t have any index file, but also have autoindex off set at Nginx config, you will have to turn it on using this method:
autoindex nicht in nginx.conf gefunden.  


# https://www.linode.com/docs/web-servers/nginx/how-to-configure-nginx/  

File: `/etc/nginx/nginx.conf `

File: `/etc/nginx/conf.d/139.162.152.56.conf`  

server {
    # listen         80 default_server;
    listen         [::]:80 default_server;
    server_name    139.162.152.56 www.139.162.152.56;
    root           /home/flasky;
    index          index.html;

    gzip             on;
    gzip_comp_level  3;
    gzip_types       text/plain text/css application/javascript image/*;
}

modifiziert zu:

server {
        listen 80 default_server;
        listen [::]:80 default_server;

        # SSL configuration
        #
        listen 443 ssl default_server;
        listen [::]:443 ssl default_server;
}



File: `/etc/nginx/sites-enabled/flaskapp`

server {
    server_name    osteotomy.de *.osteotomy.de;
    root           /home/flasky;
    index          index.html;    

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

File: `/etc/nginx/sites-available/default`

## Nach Modigfikation ohne reboot Verhalten wie vor der Modifikation
## Nach Modigfikation mit reboot folgendes Verhalten:


bei Eingabe von http://139.162.152.56/ und theaterfreak.  
_**homepage index.html wird nicht gefunden**_   
`Welcome to nginx!

If you see this page, the nginx web server is successfully installed and working. Further configuration is required.

For online documentation and support please refer to nginx.org.  
Commercial support is available at nginx.com.  

Thank you for using nginx.`

bei Eingabe von ostheotomy.de,  http://osteotomy.de/
_** Hompage wird gefunden**_   
keine https Verbindung!



