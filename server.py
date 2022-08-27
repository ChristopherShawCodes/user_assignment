from flask import Flask, render_template,request, redirect,session
from user import User
app = Flask(__name__)

app.secret_key="Secret Shiznit Code"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/display")
def index():
    users = User.get_all()
    print(users)
    return render_template("read(all).html",users=users)

@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/display')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/create')

if __name__ == "__main__":
    app.run(debug=True)