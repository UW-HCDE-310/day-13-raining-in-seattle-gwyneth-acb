from flask import Flask, render_template
import urllib.request

app = Flask(__name__)

@app.route("/")
def index():

    with urllib.request.urlopen('https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
        is_it_raining_in_seattle = response.read().decode()

    if is_it_raining_in_seattle == "true":
        raining = "Yes!"
    else:
        raining = "NO!"
    return render_template("index.html", raining=raining)
