from flask import Blueprint,render_template,flash,request,url_for
from flask import redirect
from flask_login import login_required,logout_user
from .form import RegisterForm,LoginForm

views=Blueprint('views',__name__)

@views.route('/')
def index():
    return render_template('app/index.html')

@views.route('/login',methods=['POST','GET'])
def login():
    return render_template('app/login.html')

@views.route('/register',methods=['POST','GET'])
def register():
    form=RegisterForm()
    if form.is_submitted():
        flash('Register successfully')
    else:
        return render_template('app/register.html')

@views.route('/logout',methods=['POST','GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
