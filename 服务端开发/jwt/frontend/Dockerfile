FROM hub.bkjk-inc.com/build-factory/node-packer:latest

FROM node:6.13 as builder

WORKDIR /opt/node

ADD .  /opt/node

COPY --from=0 /opt/node/node_modules /opt/node/node_modules

RUN npm install --registry=https://registry.npm.taobao.org \
&&  npm run build

FROM nginx:1.12-alpine

COPY --from=builder /opt/node/dist /var/www

RUN chown -R 1000:1000 /var

ADD  nginx/default.conf /etc/nginx/conf.d/default.conf

ENTRYPOINT nginx -g "daemon off;"
