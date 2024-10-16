from flask import Flask, render_template, url_for, flash, redirect, request
from forms import UserRegistration, UserLogin
from flask import Flask, render_template, url_for, flash, redirect
from forms import UserRegistration, UserLogin
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = '6ff362bd79bcb1db8e54ed95890aa6e9'

# Database connection
def connect_db():
    return pymysql.connect(
        host='localhost',
        user='portfolio',
        password='portfolio_pwd',
        db='portfolio_db'
    )

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html", title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About")

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    if name and email:
        try:
            connection = connect_db()
            cursor = connection.cursor()
            query = "INSERT INTO users (name, email, message) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, message))
            connection.commit()
            flash("Your information has been submitted successfully!", "success")
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "danger")
        finally:
            connection.close()
    else:
        flash("Please provide both name and email!", "danger")

    return redirect('/')


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
