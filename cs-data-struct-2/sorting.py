#Sorting

def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """

    sorted_list = []

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst

    # i = 0, 1, 2, 3, 4, 5
    # i range = 0, 5
    # j = 0, 1, 2, 3, 4, 5; 0, 1, 2, 3, 4; 0, 1, 2, 3; 0, 1, 2; 0, 1
    # j range = 0, 5


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    merged_list = []

    while len(list1) > 0 or len(list2) > 0:
        if list1 == []:
            merged_list.append(list2.pop(0))
        elif list2 == []:
            merged_list.append(list1.pop(0))
        elif list1[0] <= list2[0]:
            merged_list.append(list1.pop(0))
        else:
            merged_list.append(list2.pop(0))


    return merged_list


    # range 0, 3
    # 1 < 4; [1]



##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    if len(lst) == 1:
        return lst

    half = int(len(lst)/2)
    list1 = merge_sort(lst[:half])
    list2 = merge_sort(lst[half:])

    return merge_lists(list1, list2)




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
