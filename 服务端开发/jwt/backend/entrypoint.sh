#!/bin/bash

# Prepare log files and start outputting logs to stdout
mkdir logs
touch ./logs/gunicorn.log
touch ./logs/gunicorn-access.log
tail -n 0 -f ./logs/gunicorn*.log &

exec gunicorn  app:app \
    --bind 0.0.0.0:8080 \
    --workers 5 \
    --worker-class sanic.worker.GunicornWorker \
    --log-level=info \
    --log-file=./logs/gunicorn.log \
    --access-logfile=./logs/gunicorn-access.log \
"$@"
