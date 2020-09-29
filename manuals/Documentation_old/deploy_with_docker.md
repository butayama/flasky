nach talk-python course data-driven-web-app-with-flask ch15

Docker zum laufen bringen
========================= 
$ snap install docker


how-to-fix-docker-got-permission-denied-issue
=============================================
  
https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user  
https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue  

sudo groupadd docker  
sudo usermod -aG docker $USER  
Run the following command or Logout and login again and run (that doesn't work you may need to reboot your machine first)  
newgrp docker  
docker run hello-world  

Folgender Fehler nach Installation mit snap install:
====================================================
Docker containers not working on Debian 10 because default ...
[Search domain forum.snapcraft.io/t/docker-containers-not-working-on-debian-10-because-default-profile-is-not-loaded/14731] https://forum.snapcraft.io/t/docker-containers-not-working-on-debian-10-because-default-profile-is-not-loaded/14731
Seems odd - as far as I understand, the Docker daemon itself embeds this docker-default profile which it then loads during the start of the daemon, and unless the Snappy profile blocked us, that should've worked (because all the required utilities for doing that should've been part of the snap or the OS, IIRC).. I wonder if there's anything useful in the denials logs for the affected ...

apt install docker nach Installation:
=====================================
(venv) uwes@hpi5:/mnt/Volume/GitHub/version_remove_requirements_txt$ docker run hello-world
bash: docker: command not found

# Docker deploy
 1167  docker build -t osteotomy:latest .
 1168  docker run --name osteotomy -d -p 8000:5000 --rm osteotomy:latest

 1172  docker logout
 1173  docker login
 1174  docker images
 1175  docker push yetigo/osteotomy:version0.0.1
 
 1181  docker pull yetigo/osteotomy:version0.0.1
 
 1182  docker container ps
 
 ## Problem Container zu stoppen:
 1183  docker container kill osteotomy
 1184  docker container stop osteotomy
 1185  sudo docker container stop osteotomy

 alle drei befehle funktionieren nicht.
das lag an der Installation von docker über Snap. Siehe meinen Kommentar in stack overflow:
https://stackoverflow.com/questions/51729836/error-response-from-daemon-cannot-stop-container/64120350#64120350
   
