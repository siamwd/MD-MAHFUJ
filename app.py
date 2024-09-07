from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample user database (in a real app, you'd use a database like MySQL or MongoDB)
users = {
    "admin": "password123",
    "user1": "password456",
    "user2": "password789"
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            return redirect(url_for("home"))
        else:
            return "Invalid username or password", 401
    return render_template("login.html")

@app.route("/home")
def home():
    return "Welcome to the home page!"

if __name__ == "__main__":
    app.run(debug=True)