from flask import Flask, render_template, url_for, flash, redirect
from forms import UserRegistration, UserLogin
from flask import Flask, render_template, url_for, flash, redirect
from forms import UserRegistration, UserLogin

app = Flask(__name__)
app.config['SECRET_KEY'] = '6ff362bd79bcb1db8e54ed95890aa6e9'


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = UserLogin()
    if form.validate_on_submit():
        if form.email.data == "admin@example.com" and \
                form.password.data == "password":
            return "Logged in!"
        else:
            return "Login failed"
    return render_template("index.html", title="Login", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = UserRegistration()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("index.html", title="Register", form=form)


if __name__ == "__main__":
    app.run(debug=True)
