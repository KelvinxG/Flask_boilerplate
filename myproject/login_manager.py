from flask_login import UserMixin,login_user,logout_user,current_user,LoginManager,login_required


def login_manager(app):
    login_manager=LoginManager()
    login_manager.init_app(app)
    login_manager.login_view='login'
    