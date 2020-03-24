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
Common Name (e.g. server FQDN or YOUR name) []:Uwe Schweinsberg
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

 


excellent cloud-based MFA services are available, such as Google Authenticator and Duo (duo.com).  

Change root and administrator passwords  
At least every six months  
Every time someone who had access to them leaves your site  
Whenever you wonder whether security might have been compromised  


