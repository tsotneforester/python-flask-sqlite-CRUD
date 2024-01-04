from flask import Flask, render_template, request, redirect
import logging
import sqlite3

app = Flask(__name__)

# Set up logging to print messages to the terminal
# usage - logging.info() 
logging.basicConfig(level=logging.DEBUG)

def db(query):
    # Connect to SQLite database
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Execute a simple SELECT query
    cursor.execute(query)

    # Commit the changes
    connection.commit()

    # Get data
    data = cursor.fetchall()
    # Close the database connection
    cursor.close()
    connection.close()
    
    return data

LIST = {}
SPORTS = ["football", "snooker", "boxing", "cycling"]

@app.route("/")
def registrants():
     registrants = db("SELECT * FROM registrants")
     return render_template("index.html", registrants = registrants)


@app.route("/add", methods = ["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("add.html", sports = SPORTS)
    elif request.method == "POST":
        name = request.form.get("name")
        sport = request.form.get("sport")
        if sport in SPORTS:
            LIST[name] = sport
            db("INSERT INTO registrants (name, sport) VALUES ('{}', '{}')".format(name, sport))
            return redirect("/")
        else:
            return render_template("failure.html")




@app.route("/delete", methods = ["POST"])
def delete():
    id = request.form.get("id")
    db("DELETE FROM registrants WHERE id = {}".format(id))
    return redirect("/")

@app.route("/edit", methods = ["POST"])
def edit():
     id = request.form.get("id")
     registrant = db("select * from registrants WHERE id = {}".format(id))
     return render_template("edit.html", registrant = registrant, sports = SPORTS)

@app.route("/update", methods = ["POST"])
def update():

     id = request.form.get("id")
     name = request.form.get("name")
     sport = request.form.get("sport")
     db("UPDATE registrants SET name='{}', sport='{}' WHERE id = {}".format(name, sport, id))
     return redirect("/")


if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0")

# request.args.get for GET
# request.form.get for POST
# host="0.0.0.0" runs app in --host mode
