#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static

# Install Nginx if it's not already installed
if ! which nginx > /dev/null; then
        sudo apt-get update
        sudo apt-get -y install nginx
        sudo ufw allow 'Nginx HTTP'
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file for testing
echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of /data/ to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '44i\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-enabled/default

# check the syntax of the config
sudo nginx -t

# Restart Nginx
sudo service nginx restart
