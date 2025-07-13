from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Index Page"

@app.route("/hobby/")
@app.route("/hobbies/")
def hobby():
    message = "Reading Online Manga and Manha"
    return message


@app.route("/profile/<username>")
@app.route("/profiles/<username>")
def profile_dynamic(username=None):
    if username:
        return f"Profile {username}"
    else:
        return "Profile Page"

app.run()