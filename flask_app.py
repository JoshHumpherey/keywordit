from flask import Flask, render_template, request, flash, session
import os

app = Flask(__name__)
secret_key = str(os.urandom(24))
app.secret_key = secret_key

@app.route("/")
def hello():
    return render_template('mainpage.html')

if __name__ == "__main__":
    app.run()
