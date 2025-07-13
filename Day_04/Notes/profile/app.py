from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "secret"
@app.get("/")
def show_todo():
    if "todos" not in session:
        session["todos"] = ["Apple","Mango","Strawberry","Orange"]
    # session["todos"] = ["Apple", "Mango", "Strawberry", "Orange"]
    return render_template("homepage.html", todos=session["todos"])

@app.post("/delete/item/")
def delete_item():
    todo = request.form["todo"]
    if todo in session.get("todos", []):
        session["todos"].remove(todo)
        session.modified = True
    return redirect("/")

# @app.route("/add")
# def add():
#     return render_template("orders.html")
# @app.route("/bought")
# def add():
#     return render_template("orders.html")
# @app.route("/delete")
# def add():
#     return render_template("orders.html")
app.run()