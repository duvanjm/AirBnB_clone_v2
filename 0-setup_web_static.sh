#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static.

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir /data/
sudo mkdir /data/web_static/
sudo mkdir /data/web_static/releases/
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
printf %s "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

ln /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu /data/
config_file="/etc/nginx/sites-available/default"
sudo sed -i '29a \ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $config_file
sudo service nginx restart
