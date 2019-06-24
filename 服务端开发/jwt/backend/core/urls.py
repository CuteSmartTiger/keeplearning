from sanic import Blueprint
from core import views

bp = Blueprint("bp")

bp.add_route(views.LoginView.as_view(), "/login")
bp.add_route(views.TenantView.as_view(), "/tenant")
bp.add_route(views.UserView.as_view(), "/user")
bp.add_route(views.SystemView.as_view(), "/system")
bp.add_route(views.DeployView.as_view(), "/deploy")
bp.add_route(views.DeployCommentView.as_view(), "/deploy/comment")
bp.add_route(views.DeployUploadView.as_view(), "/deploy/upload")
bp.add_route(views.DeployTodoView.as_view(), "/deploy/todo")
bp.add_route(views.ChangeView.as_view(), "/change")
bp.add_route(views.ChangeCommentView.as_view(), "/change/comment")
bp.add_route(views.ChangeUploadView.as_view(), "/change/upload")
bp.add_route(views.ChangeTodoView.as_view(), "/change/todo")
