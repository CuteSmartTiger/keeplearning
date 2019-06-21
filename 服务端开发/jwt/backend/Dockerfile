FROM python:3.6

COPY ./entrypoint.sh /

WORKDIR /usr/src/app

COPY . /usr/src/app

ADD  .pip  /root/.pip
ADD  sources.list     /etc/apt/sources.list

ENV DEBIAN_FRONTEND noninteractive
ENV TZ=Asia/Shanghai

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN  apt-get update -y \
&&   apt-get install -y slapd ldap-utils sqlite3 libsqlite3-dev python-ldap libldap2-dev  libsasl2-dev

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

ENTRYPOINT ["/entrypoint.sh"]
