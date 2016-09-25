from lab06 import *

## Extra Nonlocal Questions ##

# Question 9
def count_calls(f):
    """A function that returns a version of f that counts calls to f and can
    report that count to how_many_calls.


    >>> from operator import add
    >>> counted_add, add_count = count_calls(add)
    >>> add_count()
    0
    >>> counted_add(1, 2)
    3
    >>> add_count()
    1
    >>> add(3, 4)  # Doesn't count
    7
    >>> add_count()
    1
    >>> counted_add(5, 6)
    11
    >>> add_count()
    2
    """
    from operator import add
    call_time=0
    #define a counted version of add,everytime it was called, the coun_time plus 1
    def add_counted(*args):
        nonlocal call_time
        call_time+=1
        return add(*args)
    #return the call_time
    def add_count():
        return call_time
    return add_counted,add_count
    "*** YOUR CODE HERE ***"
