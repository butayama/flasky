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

weitere Recherchen nötig!
