from app import app
from flask import render_template,flash, redirect, url_for
from flask_login import login_user,logout_user
from app.models.tables import User
from app.models.forms import LoginForm,CreateForm
from app import db




@app.route("/index/<user>")
@app.route("/",defaults={"user":None})
def index(user):
    return render_template('index.html',user=user)


@app.route("/login",methods = ["POST","GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in!!!")
            return redirect(url_for("index",user = user.name ))
        else:
            flash("Invalid Login.")
            return redirect(url_for("logout"))

    return render_template('login.html',form = form)


@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out!!!")
    return redirect(url_for("index"))


@app.route("/create_account",methods = ["POST","GET"])
def create_account():
    form = CreateForm()
    if form.validate_on_submit():
        u = User(form.username.data,form.password.data,form.email.data,form.name.data)
        user = User.query.filter_by(username = form.username.data).first()
        if user!=None:
            flash('Usuário já existe')
        else:
            db.session.add(u)
            db.session.commit()
            return redirect(url_for('login'))

    return render_template('create_account.html', form = form)




@app.route("/teste/<info>")
@app.route("/teste",defaults={"info":None})
def teste(info):
    r = User.query.filter_by(username = "teste").first()
    db.session.delete(r)
    db.session.commit()
    return "ok"

