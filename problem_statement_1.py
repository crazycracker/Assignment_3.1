#returns the single valued result by passing the result of previous iteration
# into the next iteration as an argument
def myreduce(func, seq):
    total = seq[0]
    for next in seq[1:]:
        total = func(total, next)
    return total

