from lab03 import *

# Q9
def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: _____
    while x > 0:
        x, y = _____, f()
    return y == n

# Q10
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """

    return pair_helper(n,1)*pair_helper(n,9)+pair_helper(n,2)*pair_helper(n,8)+pair_helper(n,3)*pair_helper(n,7)+pair_helper(n,4)*pair_helper(n,6)+((pair_helper(n,5)*(pair_helper(n,5)-1))//2)


    "*** YOUR CODE HERE ***"
def pair_helper(n,i):
        if(n<10 and n==i):
            return 1
        if(n<10 and n!=i):
            return 0
        else:
            if(n%10==i):
                return 1+pair_helper(n//10,i)
            else:
                return 0+pair_helper(n//10,i)

from doctest import run_docstring_examples

run_docstring_examples(ten_pairs,globals(),True)