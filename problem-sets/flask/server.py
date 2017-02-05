from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route('/')
def homepage():
    """Show homepage"""
    return render_template('index.html')

@app.route('/application-form')
def application_form():
    """Show application form"""
    positions = ["Software Engineer", "QA Engineer", "Product Manager", "Kitteh Master", "Furball Remover"]
    return render_template('application-form.html', positions=positions)

@app.route('/application-success', methods=['POST'])
def application_success():
    """Show application submit success"""
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    position = request.form.get('position')
    salaryrequirement = int(request.form.get('salaryreq'))
    return render_template('application-response.html', firstname=firstname, lastname=lastname, jobtitle=position, salaryrequirement=salaryrequirement)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
