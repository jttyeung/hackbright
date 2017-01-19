import random

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    return render_template("compliment.html", person=player)


@app.route('/game')
def show_madlib_form():
    """Display madlib form"""

    choice = request.args.get("play_game")
    print choice

    if choice == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():

    verbing = request.args.get("verbing")
    place = request.args.get("place")
    holiday_song = request.args.get("holiday_song")
    adjective1 = request.args.get("adjective1")
    adjective2 = request.args.get("adjective2")
    name1 = request.args.get("name1")
    verbed1 = request.args.get("verbed1")
    verbed2 = request.args.get("verbed2")
    amount_of_time1 = request.args.get("amount_of_time1")
    verb = request.args.get("verb")
    plural_noun = request.args.get("plural_noun")
    name2 = request.args.get("name2")
    number = request.args.get("number")
    food = request.args.get("food")
    verbed3 = request.args.get("verbed3")
    noun = request.args.get("noun")
    singer = request.args.get("singer")
    adjective3 = request.args.get("adjective3")
    name3 = request.args.get("name3")
    messy_food = request.args.get("messy_food")
    body_part = request.args.get("body_part")
    amount_of_time2 = request.args.get("amount_of_time2")
    holiday_food = request.args.get("holiday_food")

    print request.args

    return render_template("madlib.html",
                           verbing=verbing,
                           place=place,
                           holiday_song=holiday_song,
                           adjective1=adjective1,
                           adjective2=adjective2,
                           name1=name1,
                           verbed1=verbed1,
                           verbed2=verbed2,
                           amount_of_time1=amount_of_time1,
                           verb=verb,
                           plural_noun=plural_noun,
                           name2=name2,
                           number=number,
                           food=food,
                           verbed3=verbed3,
                           noun=noun,
                           singer=singer,
                           adjective3=adjective3,
                           name3=name3,
                           messy_food=messy_food,
                           body_part=body_part,
                           amount_of_time2=amount_of_time2,
                           holiday_food=holiday_food,
                           )


@app.route("/sample")
def show_sample():
    return render_template("sample_madlib.html")


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
