from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    message =("<h1>"
              "Jonathan Medalla"
              "\n"
              "Denso Ten Solution Philippines"
              "")

    return message

@app.route("/hobby/")
@app.route("/hobbies/")
def hobby():
    message = "Reading Online Manga and Manha"
    return message

@app.route("/interest/")
@app.route("/interests")
def interest():
    message = "Reading Online Manga and Manha"
    return message

@app.route("/opinion/<topic>")
@app.route("/opinions/<topic>")
def opinion(topic):
    message = "Flying car is near"
    return message
@app.route("/coffee/")
@app.route("/coffees/")
def coffee():
    return render_template("coffee_lover.html")

app.run()