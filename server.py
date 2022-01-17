from flask import Flask, render_template, request, redirect, session # imports functions

app = Flask(__name__) # creates object
app.secret_key = "keep it secret, keep it safe" # creates a secret key

@app.route('/') # creates route for the home page
def home(): # default function
    return render_template("index.html") # displays index.html

@app.route('/count', methods=['POST']) # route that gathers input information
def count(): # post function
    print("POST INFO") # print on the terminal
    print(request.form) # print the input information
    session["submit"]= request.form['submit'] # puts the input in session
    return redirect("/display") # redirects to display route NEVER RENDER ON POST

@app.route('/display') # display route
def display(): # display function
    print("GET INFO") # prints on the terminal
    print(session) # prints all the information on session
    return render_template( # returns the following
        "display.html", # renders display.html
        count = session["submit"], # gets input info from session
        )

if __name__ == "__main__": # runs python
    app.run(debug=True)

