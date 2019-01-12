from flask import Flask, render_template, url_for, session, redirect, escape, request, abort
from utils.rules_reader import read_config
from utils.generate_file import bashfile
from utils.ip_update import update_config

from secure.auth import available_tokens

import os
import hashlib

app = Flask(__name__)
app.secret_key = os.urandom(16)

accepted_passphrase = available_tokens["admin"]


@app.route("/", methods=["POST", "GET"])
def index(store=None, error=None, success=None):
    error = request.args.get("error")
    success = request.args.get("success")
    if "token" in session and session["token"] == accepted_passphrase:
        if request.method == "POST":
            srcproto = request.form["srcproto"]
            srcip = request.form["srcip"]
            srcport = request.form["srcport"]
            dproto = request.form["dproto"]
            dip = request.form["dip"]
            dport = request.form["dport"]
            new_config = read_config()
            new_config.append((srcproto, srcip, srcport, dproto, dip, dport))
            new_file = bashfile(new_config)
            if new_file[0]:
                new_file_location = new_file[1]
                command = update_config(new_file_location)
                if command[0]:
                    success = "Done"
                    store = read_config()
                else:
                    error = "Error in in performing iptables update"
            else:
                error = "Error in creating new file with updated rules"
        else:
            store = read_config()
        return render_template("index.html", store=store, error=error, success=success)
    return redirect(url_for("login"))


@app.route("/login", methods=["POST", "GET"])
def login():
    error = None
    if request.method == "POST":
        passphrase = request.form["password"]
        sha256digest = hashlib.sha256(passphrase.encode()).hexdigest()
        if sha256digest == accepted_passphrase:
            session["token"] = sha256digest
            return redirect(url_for("index"))
        else:
            error = "Invalid passphrase"
    if "token" in session and session["token"] == accepted_passphrase:
        return redirect(url_for("index"))
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template("login.html", error=error)


@app.route('/delete/<id_no>')
def delete_record(id_no):
    error = None
    success = None
    if "token" in session and session["token"] == accepted_passphrase:
        store = read_config()
        updated_store = [record for record in store if id_no not in record]
        new_file = bashfile(updated_store)
        if new_file[0]:
            new_file_location = new_file[1]
            command = update_config(new_file_location)
            if command[0]:
                success = "Done"
            else:
                error = "Error in in performing iptables update"
        else:
            error = "Error in creating new file with updated rules"
    return redirect(url_for("index", error=error, success=success))


@app.route("/logout")
def logout():
    # remove the username from the session if it"s there
    session.pop("token", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5501)
