"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

salespeople = []
melons_sold = []

f = open("sales-report.txt")  # opens file / recommend renaming 'f' to 'file'
for line in f:  # iterats over file
    line = line.rstrip()  # strips off newline elements
    entries = line.split("|")  # splits data by pipe delimiter
    salesperson = entries[0]  # assign var salesperson the first entry
    melons = int(entries[2])  # assign int var melons as entry at 2nd index

    if salesperson in salespeople:  # if the person is already in the list of salespeople
        position = salespeople.index(salesperson)  # get index of salesperson
        melons_sold[position] += melons  # apply the number of melons sold to the melons_sold
        #  list at the same index position of the salesperson in the salespeople list
    else:
        salespeople.append(salesperson)  # otherwise append the salesperson to end of salespeople list
        melons_sold.append(melons)  # and append the melons sold to the end of the melons list


for i in range(len(salespeople)):  # for every person in the salespeople list /
# recommend using 'salesperson' instead of 'i'
    print "{} sold {} melons".format(salespeople[i], melons_sold[i])
    # print the person and how many melons they sold


# recommendation: re-write function to use a dictionary instead of two lists

# melons_sold_per_salesperson = {}

# file = open("sales-report.txt")
# for line in file:
#     line = line.rstrip()
#     entries = line.split("|")
#     salesperson = entries[0]
#     melons = int(entries[2])

#     melons_sold_per_salesperson[salesperson] = (
#         melons_sold_per_salesperson.get(salesperson, melons) + melons)
#         # increment nuber of melons sold per salesperson


# for salesperson in melons_sold_per_salesperson:
#     print "{} sold {} melons".format(salesperson, melons_sold_per_salesperson[salesperson])
