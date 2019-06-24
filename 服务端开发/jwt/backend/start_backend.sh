#!/usr/bin/env bash


gunicorn app:app --bind 0.0.0.0:8000 --worker-class sanic.worker.GunicornWorker
