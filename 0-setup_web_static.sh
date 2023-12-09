#!/usr/bin/env bash
# This scripts creates all neccesary directories and files
# for deployment

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
	<head>
		<title>Airclone Deployment</title>
	</head>
	<body>
		<p>This a random content<p>
	</body>
</html>" | sudo tee /data/web_static/releases/test/index.html
ln -s -f /data/web_static/releases/test/  /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a \    location \/hbnb_static {\n        alias \/data\/web_static\/current\/;\n    }' /etc/nginx/sites-enabled/default
sudo service nginx restart
