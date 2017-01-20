from flask import Flask, request, render_template, redirect, flash
from model import melons, states
from shipping import calculate_shipping

app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'

@app.route("/")
def home():
    """Display the Ubermelon homepage."""
    return render_template("home.html")


@app.route("/order_melons")
def display_order_form():
    """Display a form for ordering melons."""

    # a list comprehension to get a sorted list of melon ids and names 
    sorted_melons = [ (melon_id, melons[melon_id]['name']) 
                        for melon_id in sorted(melons.keys()) ]

    return render_template("order.html", 
                           sorted_melons=sorted_melons,
                           states=states)


@app.route("/process_order", methods=['POST'])
def process_order():
    """Process an order submitted from the '/order_melons' route."""

    # gather form data
    melon_id = request.form.get('melon_id')
    quantity = int(request.form.get('qty'))

    # get info for this melon
    melon_info = melons[melon_id]

    # get the shipping cost
    state = request.form.get('state')
    shipping = calculate_shipping(state)

    # calculate the total
    price = melon_info['price']
    total = quantity * price + shipping

    # flash a message 
    confirm = "You have ordered {} {}. ".format(quantity, melon_info['name'])
    confirm += "Your order total comes to ${0:.2f}".format(total)
    flash(confirm)

    # send them back to the home page
    return redirect('/melons')


@app.route("/melons")
def display_melons():
    """Display all of the melons."""

    # here, it makes more sense to pass a sorted list of keys, as we will
    # be using all parts of the value dictionaries in the template
    sorted_melon_ids = sorted(melons.keys())

    return render_template("melons.html", 
                           sorted_melon_ids=sorted_melon_ids,
                           melons=melons)


@app.route("/melon/<melon_id>")
def display_melon(melon_id):
    """Display info for an individual melon."""

    melon_info = melons[melon_id]
    return render_template("melon_detail.html", 
                           melon_info=melon_info)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")
