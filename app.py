from flask import Flask, render_template, url_for, session, redirect, escape, request, abort
from rules_reader import read_rules
from generate_file import gen_sh

import os
import hashlib

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route("/", methods=["POST", "GET"])
def index(store=None):
    if "token" in session and session["token"] == "d513315ece7c256ee277c88ce6d70a60":
        if request.method == "GET":
            store = read_rules()
            return render_template("index.html", store=store)
    return redirect(url_for("login"))


@app.route("/login", methods=["POST", "GET"])
def login():
    error = None
    if request.method == "POST":
        passphrase = request.form["password"]
        sha256digest = hashlib.md5(passphrase.encode()).hexdigest()
        # hardcoded passcode bc i"m very lazy
        if sha256digest == "d513315ece7c256ee277c88ce6d70a60":
            session["token"] = sha256digest
            redirect(url_for("index"))
        else:
            error = "Invalid passphrase"
    if "token" in session:
        if session["token"] == "d513315ece7c256ee277c88ce6d70a60":
            return redirect(url_for("index"))
        else:
            error = "Expired auth session, log in again"
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    # remove the username from the session if it"s there
    session.pop("token", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)