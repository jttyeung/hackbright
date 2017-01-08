log_file = open("um-server-01.txt")


def sales_reports(log_file):
    """ Prints sales info for Monday """
    
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        
        # Below is the only substantial change to
        # this file. You're looking for the variable
        # called "day" and changing what the program
        # looks for to print.

        if day == "Mon":
            print line


sales_reports(log_file)
