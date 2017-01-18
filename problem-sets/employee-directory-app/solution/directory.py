from flask import Flask, request, render_template, redirect, flash
from model import employee_directory

app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'


@app.route("/")
def home():
    """This is the employee directory home page"""
    # give the user the home page, which has a search form:
    return render_template("home.html")


@app.route("/employee_search")
def get_employee_details():
    """this is the 'action' we use for our searches. It returns the employee details page """

    # get the employee name from the search form (which is passed in the request object):
    name = request.args.get("employee_name")

    # if the user doesn't type in anything:
    if not name:
        flash("please type in a first name")

    # if the name isn't in our directory:
    elif name.lower() not in employee_directory:
        # 'flash' a message to the user so they see it once.
        flash("%s not found." % name)

    # we have a name, its in our directory, so let's return that info:
    else:
        employee_info = employee_directory.get(name.lower())
        return render_template("employee_details.html", details=employee_info)

    # if we didn't return the employee details page, send them back to the page
    # they were on before:
    return(redirect(request.referrer))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
