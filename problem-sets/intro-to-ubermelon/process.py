log_file = open("um-server-01.txt")
# opens a file named um-server-01.txt

def sales_reports(log_file):
# create a function called sales_reports, that takes a log_file as an argument
    for line in log_file:
    # for each line in the file
        line = line.rstrip()
        # each line is a line with  the newline element removed
        day = line[0:3]
        # each day is defined by the first 3 characters of the line
        if day == "Mon":
        # if that day is tuesday
            print line
            # print the line out


sales_reports(log_file)
# call the function sales_reports and this will print out the log file day
