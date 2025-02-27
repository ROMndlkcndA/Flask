from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/contact")
def contact():
    return render_template("contact.html")



@app.route("/user/<string:name>/<int:id>")
def user(name, id):
    return "User page: " + name + " - " + str(id)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5003)
