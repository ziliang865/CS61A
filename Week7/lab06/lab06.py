## Lab 6: OOP and Nonlocal ##

# Question 1
def vending_machine(snacks):
    """Cycles through list of snacks.
    
    >>> vender = vending_machine(['chips', 'chocolate', 'popcorn'])
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(['brownie'])
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    i=0
    def snack():
        nonlocal i
        i=i+1
        return snacks[(i-1)%len(snacks)]
    return snack
    "*** YOUR CODE HERE ***"
