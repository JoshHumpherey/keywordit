from flask import Flask, render_template, request, flash, session
import os
from parser import *

app = Flask(__name__)
secret_key = str(os.urandom(24))
app.secret_key = secret_key

@app.route("/")
def hello():
    return render_template('mainpage.html')

@app.route('/', methods=['POST'])
def my_form_post():
    url = request.form['Reddit URL']
    search_term = request.form['Keyword']
    return parser.find_relevant_comments(url, search_term)

if __name__ == "__main__":
    app.run()
