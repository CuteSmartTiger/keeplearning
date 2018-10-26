vim /etc/nginx/conf.d/default.conf


虚拟机自带的
```
server {
    listen 80;
    server_name localhost;
    charset     utf-8;
    location / {
        try_files $uri @vdidesktop;
     }
    location ^~ /admin{
        alias /opt/www/dist/;
        try_files $uri $uri/   @rewrites;
    }
    location @rewrites {
            rewrite ^/(admin)/(.+)$ /$1/index.html last;
    }
    location @vdidesktop {
      include uwsgi_params;
      #uwsgi_pass unix:/tmp/uwsgi.sock;
      uwsgi_pass localhost:11000;
      rewrite ^/$ /admin redirect;
    }
    client_max_body_size 200M;
}


```
