from flask import *
app = Flask(__name__)

user_credentials = [("user@gmail.com","password")]
session_exists = False

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/explore")
def about():
    return render_template("about.html")

@app.route("/purchase")
def purchase():
    return render_template("products.html")

@app.route("/login")
def login():
    return render_template("login.html")
 
@app.route("/session",methods=["POST"])
def fetch_credentials():
    email = request.form["email"]
    passkey = request.form["passkey"]
    if (email,passkey) in user_credentials:
        session_exists = True
        return render_template("products.html")
    else:
        return render_template("error.html")

@app.route("/cart",methods=["POST"])
def fetch_cart():
    cart_items = request.form["cart_items"]
    return render_template("cart.html",cart=cart_items)