#!/usr/bin/env bash
#a Bash script that sets up web servers for the deployment of web_static

apt update && apt install -y nginx
mkdir --parents /data/web_static/releases/
mkdir --parents /data/web_static/shared/
mkdir --parents /data/web_static/releases/test/
cat > /data/web_static/releases/test/index.html <<EOF
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF
ln --force --symbolic /data/web_static/releases/test/ /data/web_static/current
chown --recursive ubuntu:ubuntu /data/
sed -i '/listen 80 default_server/a location /hbnb_static/ {alias /data/web_static/current/;}' \
    /etc/nginx/sites-available/default
service nginx restart
