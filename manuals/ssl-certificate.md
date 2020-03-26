https://learning.oreilly.com/videos/ssl-complete-guide

https//:www.ssllabs.com/ssl-pulse  
ahrefs.com analyse websites

301 permanent redirect  

canonical HTTPS version: html metatag https enforced  

https tcp Port 443

Analysing Traffic using Wireshark

# Voraussetzung für ssl-certificate:  
https://www.linode.com/docs/networking/dns/using-your-systems-hosts-file/

## File: /etc/hosts
127.0.0.1 localhost.localdomain localhost  
139.162.152.56 pumuckel.osteotomy.de pumuckel  
2a01:7e01::f03c:91ff:fea4:f75a pumuckel.osteotomy.de pumuckel  
# The following lines are desirable for IPv6 capable hosts  
::1     localhost ip6-localhost ip6-loopback  
ff02::1 ip6-allnodes  
ff02::2 ip6-allrouters

## Name Service Switch file: /etc/nsswitch.conf
Example configuration of GNU Name Service Switch functionality.  
If you have the `glibc-doc-reference' and `info' packages installed, try:  
`info libc "Name Service Switch"' for information about this file.  

# Versuch mit anderer Adressierung:
## File: /etc/hosts
127.0.0.1 localhost.localdomain localhost  
127.0.1.1 pumuckel.osteotomy.de pumuckel  
127.0.1.1 www.osteotomy.de www  
139.162.152.56 pumuckel.osteotomy.de pumuckel  
/# 2a01:7e01::f03c:91ff:fea4:f75a pumuckel.osteotomy.de pumuckel  
/# The following lines are desirable for IPv6 capable hosts  
::1     localhost ip6-localhost ip6-loopback  
ff02::1 ip6-allnodes  
ff02::2 ip6-allrouters



passwd:         compat  
group:          compat  
shadow:         compat  
gshadow:        files  

hosts:          files dns  
networks:       files  

protocols:      db files  
services:       db files  
ethers:         db files  
rpc:            db files  

netgroup:       nis  

  

# ssllabs
### https://github.com/ssllabs/research/wiki/SSL-and-TLS-Deployment-Best-Practices

Make sure you add all the necessary domain names to Subject Alternative Name (SAN) since all the latest browsers do not check for Common Name for validation  

TLS v1.2 or TLS v1.3 should be your main protocol because these version offers modern authenticated encryption (also known as AEAD). If you don't support TLS v1.2 or TLS v1.3 today, your security is lacking.  

# neuer Versuch nach https://alvinalexander.com/linux-unix/my-notes-how-configure-https-nginx-ubuntu-16/  

uwes@hpi5:~$ ssh uwe@139.162.152.56
Linux pumuckel 4.9.0-12-amd64 #1 SMP Debian 4.9.210-1 (2020-01-20) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Mar 23 06:50:22 2020 from 91.33.168.29
(3.8.1/envs/flasky) ➜  flasky git:(linode-deploy) ✗ openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout /etc/ssl/private/aja-nginx-selfsigned.key -out /etc/ssl/certs/aja-nginx-selfsigned.crt
req: Cannot open output file /etc/ssl/private/aja-nginx-selfsigned.key, Permission denied
req: Use -help for summary.
(3.8.1/envs/flasky) ➜  flasky git:(linode-deploy) ✗ sudo openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout /etc/ssl/private/aja-nginx-selfsigned.key -out /etc/ssl/certs/aja-nginx-selfsigned.crt
[sudo] password for uwe: 
Generating a RSA private key
.....................+++++
...........................+++++
writing new private key to '/etc/ssl/private/aja-nginx-selfsigned.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:DE
State or Province Name (full name) [Some-State]:NRW
Locality Name (eg, city) []:Bochum
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Ingenieurbuero Schweinsberg
Organizational Unit Name (eg, section) []:Software Development
Common Name (e.g. server FQDN or YOUR name) []:*.osteotomy.de
Email Address []:yetigo42+osteotomy@gmail.com
(3.8.1/envs/flasky) ➜  flasky git:(linode-deploy) ✗ sudo openssl dhparam -out /etc/ssl/certs/aja-dhparam.pem 2048
Generating DH parameters, 2048 bit long safe prime, generator 2
This is going to take a long time
..............+......................+................+......
(3.8.1/envs/flasky) ➜  flasky git:(linode-deploy) ✗ 

## /mnt/Volume/GitHub/flasky/app/templates/html5-page-layout/
static html site mit alternativer Nginx Benachrichtigung
die config Seiten entsprechend angepasst:

## File: /etc/nginx/conf.d/139.162.152.56.conf                

server {
        listen         80 default_server;
        listen         [::]:80 default_server;
        server_name 139.162.152.56;
        root           /home/static-sites/html5-page-layout;
        index          index.html;
        # SSL configuration
        #
        listen 443 ssl default_server;
        listen [::]:443 ssl default_server;
}

##  File: /etc/nginx/sites-enabled/flaskapp                  

server {
    listen 443 ssl default_server;
    listen [::]:443 ssl default_server;
    server_name osteotomy.de ;
    server_name *.osteotomy.de;
    server_name www.osteotomy.de;
    root           /home/flasky;
    index          index.html;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}

 1506  sudo nano /etc/nginx/nginx.conf
 1507* sudo nano /etc/nginx/conf.d/139.162.152.56.conf
 1508* sudo nano /etc/nginx/sites-enabled/flaskapp

systemctl status nginx
sudo systemctl stop nginx
sudo systemctl start nginx


# Security
## https://learning.oreilly.com/library/view/unix-and-linux/9780134278308/Security.xhtml  
netstat -an | grep LISTEN  
htop --> PID  
ps -p <PID>  
If a service is unneeded, stop it and make sure that it won’t be restarted at boot time. You can also use the tools fuser or netstat -p if lsof is not available.  
nmap -sT osteotomy.de  

sudo nmap -sV -O osteotomy.de 

openssl s_client -connect osteotomy.de  
 


excellent cloud-based MFA services are available, such as Google Authenticator and Duo (duo.com).  

Change root and administrator passwords  
At least every six months  
Every time someone who had access to them leaves your site  
Whenever you wonder whether security might have been compromised  


# ssh

    ssh, the client
    sshd, the server daemon
    ssh-keygen, for generating public/private key pairs
    ssh-add and ssh-agent, tools for managing authentication keys
    ssh-keyscan, for retrieving public keys from servers
    sftp-server, the server process for file transfer over SFTP
    sftp and scp, file transfer client utilities

To initiate this process, a user invokes ssh with the remote host as the first argument:  
ssh attempts a TCP connection on port 22, the standard SSH port assigned by IANA.  
Once the user accepts the key, the fingerprint is added to ~/.ssh/known_hosts for future use.  
ssh and sshd can be tuned for varying needs and security types. Configuration is found in the /etc/ssh directory, an uncharacteristically standard location among all flavors of UNIX and Linux.  
In addition to /etc/ssh, OpenSSH uses ~/.ssh for storing public and private keys, for per-user client configuration overrides, and for a few other purposes. The ~/.ssh directory is ignored unless its permissions are set to 0700.  

The -v option prints debug messages. Specify it multiple times (maximum of three) to increase verbosity. You’ll find this flag to be invaluable when debugging authentication problems.  
</img>


## URL
The address portion of a web URL allows quite a bit of interior structure. Here’s the overall pattern:
			scheme://[username:password@]hostname[:port][/path][?query][#anchor]
All the elements are optional except scheme and hostname.  

## Therefore, basic authentication
 should really only be used over secure HTTPS connections.  
 The hostname can be a domain name or IP address as well as an actual hostname. The port is the TCP port number to connect to. The http and https schemes default to ports 80 and 443, respectively.  
 


# https://safeciphers.org/
## nginx config example

ssl_protocols TLSv1.3;# Requires nginx >= 1.13.0 else use TLSv1.2
ssl_prefer_server_ciphers on;
ssl_dhparam /etc/nginx/dhparam.pem; # openssl dhparam -out /etc/nginx/dhparam.pem 4096
ssl_ciphers EECDH+AESGCM:EDH+AESGCM;
ssl_ecdh_curve secp384r1; # Requires nginx >= 1.1.0
ssl_session_timeout  10m;
ssl_session_cache shared:SSL:10m;
ssl_session_tickets off; # Requires nginx >= 1.5.9
ssl_stapling on; # Requires nginx >= 1.3.7
ssl_stapling_verify on; # Requires nginx => 1.3.7
resolver $DNS-IP-1 $DNS-IP-2 valid=300s;
resolver_timeout 5s;
add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload";
add_header X-Frame-Options DENY;
add_header X-Content-Type-Options nosniff;
add_header X-XSS-Protection "1; mode=block";
                
## File: /etc/nginx/nginx.conf      Stand: 25.3.2020                              

user uwe;
worker_processes auto;

error_log  /var/log/nginx/error.log warn;
pid /run/nginx.pid;

include /etc/nginx/modules-enabled/*.conf;

events {
        worker_connections 768;
        # worker_processes auto;
        # multi_accept on;
}

http {

        ##
        # Basic Settings
        ##

        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 65;
        types_hash_max_size 2048;
        server_tokens off;

        # server_names_hash_bucket_size 64;
        # server_name_in_redirect off;

        include /etc/nginx/mime.types;
        default_type application/octet-stream;

        ##
        # SSL Settings
        ##

        ssl_protocols TLSv1.2;# TLSv1.3 Requires nginx >= 1.13.0 else use TLSv1.2
        ssl_prefer_server_ciphers on;
        ssl_dhparam /etc/nginx/dhparam.pem; # openssl dhparam -out /etc/nginx/dhparam.pem 4096
        ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DH$
        ssl_ecdh_curve secp384r1; # Requires nginx >= 1.1.0
        ssl_session_timeout  10m;
        ssl_session_cache shared:SSL:10m;
        ssl_session_tickets off; # Requires nginx >= 1.5.9
        ssl_stapling on; # Requires nginx >= 1.3.7
        ssl_stapling_verify on; # Requires nginx => 1.3.7
        resolver $DNS-IP-1 $DNS-IP-2 valid=300s;
        ##
        # Logging Settings
        ##

        log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

        access_log /var/log/nginx/access.log main;
        error_log /var/log/nginx/error.log;

        ##
        # Gzip Settings
        ##

        # gzip on;
        gzip_disable "msie6";

        # gzip_vary on;
       add_header X-Frame-Options DENY;
        add_header X-Content-Type-Options nosniff;
        add_header X-XSS-Protection "1; mode=block";

        ##
        # Logging Settings
        ##

        log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

        access_log /var/log/nginx/access.log main;
        error_log /var/log/nginx/error.log;

        ##
        # Gzip Settings
        ##

        # gzip on;
        gzip_disable "msie6";

        # gzip_vary on;
        # gzip_proxied any;
        # gzip_comp_level 6;
        # gzip_buffers 16 8k;
        # gzip_http_version 1.1;
        # gzip_types text/plain text/css application/json application/javascript text/xml application/xm$

        ##
        # Virtual Host Configs
        ##

        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
}


\#mail {
\#       # See sample authentication script at:
\#       # http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
\#
\#       # auth_http localhost/auth.php;
\#       # pop3_capabilities "TOP" "USER";
\#       # imap_capabilities "IMAP4rev1" "UIDPLUS";
\#
\#       server {
\#               listen     localhost:110;
\#               protocol   pop3;
\#               proxy      on;
\#       }
\#
\#       server {
\#               listen     localhost:143;
\#               protocol   imap;
\#               proxy      on;
\#       }
\#}

## We need generate a stronger DHE parameter:

openssl dhparam -out /etc/ssl/certsdhparam.pem 4096

And then tell nginx to use it for DHE key-exchange:

ssl_dhparam /etc/ssl/certs/dhparam.pem;
ssl_ecdh_curve secp384r1; # Requires nginx >= 1.1.0

# Conclusion

If you have applied the above config lines you need to restart nginx:

# Check the config first:
/etc/init.d/nginx configtest
# Then restart:
/etc/init.d/nginx restart

Now use the SSL Labs test to see if you get a nice A. And, of course, have a safe, strong and future proof SSL configuration!

Also read the Mozilla page on the subject
Tags: nginx , security , ssl , ssl-labs , tls , tutorials


Letzter Versuch gemäß:
https://hostadvice.com/how-to/how-to-configure-nginx-to-use-self-signed-ssl-tls-certificate-on-ubuntu-18-04-vps-or-dedicated-server/
hat nicht funktioniert!

# https://www.nginx.com/resources/wiki/start/topics/tutorials/config_pitfalls/  
To easily display all the permissions on a path, you can use:

# namei -om /path/to/checkhttps://www.digitalocean.com/community/tutorials/how-to-create-a-self-signed-ssl-certificate-for-nginx-in-ubuntu-16-04
We will make a few adjustments to our configuration.

    We will create a configuration snippet containing our SSL key and certificate file locations.
    We will create a configuration snippet containing strong SSL settings that can be used with any certificates in the future.
    We will adjust our Nginx server blocks to handle SSL requests and use the two snippets above.

# certbot successful certification
uwes@hpi5:~$ ssh uwe@139.162.152.56
Linux pumuckel 4.9.0-12-amd64 #1 SMP Debian 4.9.210-1 (2020-01-20) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Mar 26 23:49:35 2020 from 91.33.168.29
(3.8.1/envs/flasky) ➜  flasky git:(linode-deploy) ✗ sudo certbot -nginx
[sudo] password for uwe: 
usage: 
  certbot [SUBCOMMAND] [options] [-d DOMAIN] [-d DOMAIN] ...

Certbot can obtain and install HTTPS/TLS/SSL certificates.  By default,
it will attempt to use a webserver both for obtaining and installing the
certificate. 
certbot: error: argument -n/--non-interactive/--noninteractive: ignored explicit argument 'ginx'
(3.8.1/envs/flasky) ➜  flasky git:(linode-deploy) ✗ sudo certbot --nginx
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator nginx, Installer nginx

Which names would you like to activate HTTPS for?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: osteotomy.de
2: www.osteotomy.de
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select the appropriate numbers separated by commas and/or spaces, or leave input
blank to select all options shown (Enter 'c' to cancel): 
Obtaining a new certificate
Performing the following challenges:
http-01 challenge for osteotomy.de
http-01 challenge for www.osteotomy.de
nginx: [warn] "ssl_stapling" ignored, issuer certificate not found
Waiting for verification...
Cleaning up challenges
nginx: [warn] "ssl_stapling" ignored, issuer certificate not found
Deploying Certificate to VirtualHost /etc/nginx/sites-enabled/flaskapp
Deploying Certificate to VirtualHost /etc/nginx/sites-enabled/flaskapp

Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: No redirect - Make no further changes to the webserver configuration.
2: Redirect - Make all requests redirect to secure HTTPS access. Choose this for
new sites, or if you're confident your site works on HTTPS. You can undo this
change by editing your web server's configuration.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select the appropriate number [1-2] then [enter] (press 'c' to cancel): 1

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Congratulations! You have successfully enabled https://osteotomy.de and
https://www.osteotomy.de

You should test your configuration at:
https://www.ssllabs.com/ssltest/analyze.html?d=osteotomy.de
https://www.ssllabs.com/ssltest/analyze.html?d=www.osteotomy.de
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/osteotomy.de/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/osteotomy.de/privkey.pem
   Your cert will expire on 2020-06-24. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot again
   with the "certonly" option. To non-interactively renew *all* of
   your certificates, run "certbot renew"
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le

(3.8.1/envs/flasky) ➜  flasky git:(linode-deploy) ✗ 


