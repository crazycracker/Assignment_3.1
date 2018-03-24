#returns the list of items from the sequence which satisfy the function func()
def myfilter(func, seq):
    return [x for x in seq if func(x) == True]
