# your code goes here
restaurant_ratings_file = open ("scores.txt")
restaurant_ratings_dict = {}

def make_ratings_dict(restaurant_ratings_file):
    for line in restaurant_ratings_file:
        line = line.rstrip()
        restaurant_name, restaurant_rating  = line.split(":")
        restaurant_ratings_dict[restaurant_name] = restaurant_rating

def print_ratings_dict(restaurant_ratings_dict):
    for restaurant, rating in sorted(restaurant_ratings_dict.items()):
        #print " %s is rated  %s." % (restaurant,  rating)
        return (restaurant, rating)
#make_ratings_dict(restaurant_ratings_file)
#print_ratings_dict(restaurant_ratings_dict)




def review_add_newname_rating():


    user_choice = raw_input("Please input \"1\" for all the ratings in alphabatical order:  \
    Please input \"2\" to add new restaurant and rating \
    Enter Q to quit: ")


    while user_choice != "Q":
        if user_choice == "1":
            make_ratings_dict(restaurant_ratings_file)
            print make_ratings_dict  
            #return print_ratings_dict(restaurant_ratings_dict)
            print_ratings_dict(restaurant_ratings_dict)
        elif user_choice == "2":
            new_restaurant_name = raw_input("Please input restaurant name")
            new_restaurant_rating = raw_input("Please input restaurant rating")
            restaurant_ratings_dict[new_restaurant_name] = new_restaurant_rating
        elif user_choice == "Q":
            return














