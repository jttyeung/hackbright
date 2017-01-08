def delivery_results(filename):  # define a function delivery_results that takes a file as an argument
  the_file = open(filename)
  for line in the_file:  # for each line in the file
      line = line.rstrip()  # strip off /n for each line
      words = line.split('|')  # split each line into words by pipe delimitation

      melon = words[0]  # melon type will be the first word in the array of words
      count = words[1]  # count will be the second word in the array of words
      amount = words[2]  # amount will be the third word in the array of words

      print "Delivered {} {}s for total of ${}".format(
          count, melon, amount)  # print out the count, melon type, and amount for every line in the file
  the_file.close()  # close the file

for date in [20140519, 20140520, 20140521]:
  print date
  delivery_results("um-deliveries-{}.txt".format(date))

# print "Day 1"
# delivery_results(date) # use the delivery_results function to run on that day's deliveries

# print "Day 2"
# delivery_results(date)

# print "Day 3"
# delivery_results(date)
