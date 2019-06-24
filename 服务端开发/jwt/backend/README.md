# workflow

> A Sanic project

## Run Setup

``` bash
# debug
python3 app.y

# prod
gunicorn app:app --bind 0.0.0.0:8000 --worker-class sanic.worker.GunicornWorker
```

