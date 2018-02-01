# --------- #
# Recursion #
# --------- #

# 1. Write a function that uses recursion to print each item in a list.
def print_item(my_list, i=0):
    """Prints each item in a list recursively.

        >>> print_item([1, 2, 3])
        1
        2
        3

    """
    if len(my_list) < 1:
        return

    print my_list[i]
    print_item(my_list[1:])


# len = 3; i = 0; print 1
# len = 2; i = 0; print 2
# len = 1; i = 0; print 3
# len = 0; return


# 2. Write a function that uses recursion to print each node in a tree.

def print_all_tree_data(tree):
    """Prints all of the nodes in a tree.


        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> print_all_tree_data(one)
        1
        2
        3

    """

    print tree.data

    if tree.children == []:
        return

    for child in tree.children:
        print_all_tree_data(child)


# tree = one; tree.data = 1, tree.children = [two, three]
# tree.children[0].data
# tree.pop(0)
# tree.children[0].data


# 3. Write a function that uses recursion to find the length of a list.


def list_length(my_list, count=0):
    """Returns the length of list recursively.
        >>> list_length([1, 2, 3, 4])
        4

    """

    if my_list == []:
        return count

    return list_length(my_list[1:], count + 1)


    # count = 0; my_list = [1, 2, 3, 4]
    # count = 1; my_list = [2, 3, 4]
    # count = 2; my_list = [3, 4]
    # count = 3; my_list = [4]
    # count = 4; my_list = []


# 4. Write a function that uses recursion to count how many nodes are in a tree.

def num_nodes(tree, num=0):
    """Counts the number of nodes.

        >>> class Node(object):
        ...     def __init__(self, data):
        ...             self.data=data
        ...             self.children = []
        ...     def add_child(self, obj):
        ...             self.children.append(obj)
        ...
        >>> one = Node(1)
        >>> two = Node(2)
        >>> three = Node(3)
        >>> one.add_child(two)
        >>> one.add_child(three)
        >>> num_nodes(one)
        3
        >>> four = Node(4)
        >>> five = Node(5)
        >>> two.add_child(four)
        >>> two.add_child(five)
        >>> num_nodes(one)
        5
        >>> six = Node(6)
        >>> three.add_child(six)
        >>> num_nodes(one)
        6
    """

    # if tree.children == []:
    #     return num

    # for child in tree.children:
    #     num += 1
    #     return num_nodes(child, num + 1)

    # if not tree.children:
    #     return num

    # for child in tree.children:
    #     return num_nodes(child, num+1)


    if not tree:
        return 0

    count = 1

    for child in tree.children:
        count += num_nodes(child)

    return count


    # 1 for the one, 2 for one + two, 3 for one + two + three
    # need 4, 5, 6
    # tree.children: 2, 3
    # tree.children (two): 4, 5
    # tree.children (three): 6
    # tree.children (four): []
    # tree.children (five): []
    # tree.children (six): []



#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
