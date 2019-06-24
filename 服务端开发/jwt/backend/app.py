from sanic import Sanic
from sanic_cors import CORS, cross_origin
from aoiklivereload import LiveReloader

from core.urls import bp
from core.models import *
from config import config

app = Sanic(__name__)
app.blueprint(bp, url_prefix='/api/v1')
CORS(app, automatic_options=True)


@app.middleware('request')
async def transform_data_request(request):
    try:
        request['POST'] = request.json if request.json else {}
        request['GET'] = request.args if request.args else {}
        request['PUT'] = request.json if request.json else {}
    except Exception:
        pass


@app.middleware('response')
async def close_db(request, response):
    if not db.is_closed():
        db.close()


# application config
app.config.from_object(config)

# init the database
db.create_tables(
    [Tenant,
     System,
     User,
     Role,
     UserRole,
     SystemUser,
     DeployInstance,
     DeployStatus,
     DeployInstanceFile,
     DeployInstanceComment,
     DeployInstanceUser,
     ChangeInstance,
     ChangeStatus,
     ChangeInstanceFile,
     ChangeInstanceComment,
     ChangeInstanceUser], safe=True)

if __name__ == '__main__':
    # reload the app
    reloader = LiveReloader()
    reloader.start_watcher_thread()
    # run server debug
    app.run(host='0.0.0.0', port=8000, debug=True)
