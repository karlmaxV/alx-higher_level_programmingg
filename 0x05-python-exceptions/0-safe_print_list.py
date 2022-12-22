#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """print x elements of a list.
	Args: 
		my_list (list): the list to print elemtnets from x (int): the number of elements of my_list to print.
	Returns: the number of elements printed."""
	countt = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            continue
    print("")
    return count
