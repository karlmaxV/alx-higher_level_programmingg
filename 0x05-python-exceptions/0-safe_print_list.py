#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
   """print X elecments of a list.
   Args:
        my_list (list): the lis to print elements from.
        X (int): the number of elements of my-list to print.
    Returns:
        The number of elements printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret +=1
        except IndexError:
            break
    print("")
    return (ret)
