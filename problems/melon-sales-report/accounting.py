"""
* Counts the amounts of each type of melon that were sold
* Calculates the revenue from those melon tallies
* Separates sales into online sales and phone sales
* Produces fancy report to summarize the info for our CEO
"""

melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}  # counts types of melons
melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }
total_revenue = 0
sales = [0, 0]


def parse_file(filename):
    """
    Takes a filename and parses file data.
    """
    f = open(filename)
    for line in f:
        data = line.split("|")
        if filename == "orders-by-type.txt":  # parses data of orders by type of melon
            melon_type = data[1]
            melon_count = int(data[2])
            melon_tallies[melon_type] += melon_count
        if filename == "orders-with-sales.txt":  # parses data by salesperson type
            if data[1] == "0":
                sales[0] += float(data[3])
            else:
                sales[1] += float(data[3])
    f.close()


print "TOTAL REVENUE"
parse_file("orders-by-type.txt")

for melon_type in melon_tallies:  # calculates total revenue per melon type
    price = melon_prices[melon_type]
    revenue = price * melon_tallies[melon_type]
    total_revenue += revenue
    print "We sold {} {} melons at ${:.2f} each for a total of ${:,.2f}".format(melon_tallies[melon_type], melon_type, price, revenue)

print

print "SALES DATA"
parse_file("orders-with-sales.txt")

print "Salespeople generated ${:,.2f} in revenue.".format(sales[1])
print "Internet sales generated ${:,.2f} in revenue.".format(sales[0])

if sales[1] > sales[0]:  # compare salespeople sales to online sales
    print "Guess there's some value to those salespeople after all."
else:
    print "Time to fire the sales team! Online sales rule all!"
