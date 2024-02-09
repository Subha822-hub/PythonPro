from flask import Flask
import random

app = Flask(__name__)


randomnumber = random.randrange(1,10)

@app.route("/<int:number>")
def number(number):
    if randomnumber<number:
        return f"<h1 style='color:red;'>Too High,Try Again</h1>" \
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' >" 
    elif randomnumber>number:
        return f"<h1 style='color:violet;'>Too Low,Try Again</h1>" \
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' >" 
    
    else:
        return f"<h1 style='color:green;'>You Found Me!</h1>" \
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' >" 

@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' >" 

@app.route("/bye")
def bye():
    return "<p>Bye!</p>"


@app.route("/<name>/<int:id>")
def username(name,id):
    return f"My Name is {name}!. My Age  is {id}."

if __name__ == "__main__":
    app.run(debug=True)


