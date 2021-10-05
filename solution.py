"""
    Description:
        This function takes my_list, a list of integers, as input,
        sort it in ascending order,
        and returns the sorted list as output.

    Intuition:
        Let say we have an unsorted list of n elements.
        We find the minimum element in the list, we put it in front.
        Now we have a partially sorted list (list[0:1] is sorted, list[1:n] is not).

        We repeat the process in list[1:n].
        Find the minimum element in list[1:n], put it in front of list[1:n] (the unsorted part).
        Now list[0:1] is sorted.

        Repeat the process n-1 times, the whole list is sorted.
 
    Run through:
        my_list = [3, 2, 1]

        get minimum in my_list[0:3] ([3, 2, 1]), minimum = 1,
        put 1 in front of the unsorted part, my_list becomes [1, 3, 2]
        the sorted part is [1]

        get minimum in my_list[1:3] ([3, 2]), minimum = 2,
        put 2 in front of the unsorted part, my_list becomes [1, 2, 3]
        the sorted part is [1, 2]

        Since the remaining element must be the greatest element, we can skip it.

        The sorted list is [1, 2, 3].
"""
def sort_asc(my_list: list[int]) -> list[int]:

    for i in range(0, len(my_list)-1):  # we are doing it n-1 times, n == len(my_list

        # get minimum in the unsorted part, my_list[i:len(my_list)] is unsorted
        minimum = min(my_list[i:len(my_list)])

        # get the index of the minimum element
        min_index = my_list.index(minimum)

        # swap the minmum with the first element in the unsorted part
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

    return my_list


"""
    Good habbit to get a function to stores the code we run,
    not neccessary.
"""
def main():

    my_list = [5, 4, 3, 2, 1]   # works with a perfectly unsorted list
    print(sort_asc(my_list) == [1, 2, 3, 4, 5])     # see if our ouput is equal to our expectation 

    my_list = [1, 2, 3, 4, 5]   # works with a sorted list
    print(sort_asc(my_list) == [1, 2, 3, 4, 5])

    my_list = [1, 2, 3, 5, 4]   # works with a partially sorted list
    print(sort_asc(my_list) == [1, 2, 3, 4, 5])


# running our code
main()