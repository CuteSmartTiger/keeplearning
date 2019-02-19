FROM vdidesktop-base

# assuming all APT-GETs are ready

WORKDIR /opt/vdidesktop

RUN apt-get install -y redis-tools # should put this in base, but salt repo always get "sum mismatch" error

RUN mv ./flask ./flask_bak

# allow minions to push files to the master.
RUN sed -i '/#file_recv:/afile_recv: True' /etc/salt/master
RUN sed -i 's/#file_recv_max_size:/file_recv_max_size:/g' /etc/salt/master

# copy
COPY data/ /
COPY svn/vdidesktop  /opt/vdidesktop
COPY svn/vdidesktop-frontend /opt/www/dist
COPY svn/vdidesktop/flask/lib/python2.7/site-packages ./flask_bak/lib/python2.7/site-packages

RUN rm -rf ./flask     \
	&& mv ./flask_bak ./flask \
    && mkdir -p /srv/salt/agent \
    && mkdir -p /srv/salt/thinclient \
    && mv /opt/vdidesktop/app/static/uploads/tc_upgrade.py /srv/salt/thinclient \
    && (/opt/vdidesktop/flask/bin/python -m compileall /opt/vdidesktop || : ) \
    && find /opt/vdidesktop -name "*.py" -exec rm -f {} \;

RUN unlink /etc/nginx/sites-enabled/default \
    && make install

# add salt user
RUN useradd -M -s /sbin/nologin dmadmin	 \
    && echo "dmadmin:dmadmin" | chpasswd

# volume
VOLUME /etc/salt/pki /var/cache/salt /opt/vdidesktop/app/static/uploads

# expose
EXPOSE 80 4505 4506 8000

CMD /entrypoint.sh

