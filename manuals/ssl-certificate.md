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
2a01:7e01::f03c:91ff:fea4:f75a pumuckel.osteotomy.de pumuckel  
# The following lines are desirable for IPv6 capable hosts  
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


