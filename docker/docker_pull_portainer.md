docker pull portainer/portainer


sudo docker run -d -p 9000:9000 --name portainer --restart=always  -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
