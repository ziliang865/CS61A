###########
# Objects #
###########

# Q1

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"

    def __init__(self, item, price):
        self.sale_item = item
        self.item_price = price
        self.item_stock = 0
        self.balance = 0

    def vend(self):
        if self.item_stock == 0:
            print("\'Machine is out of stock.\'")
            return
        if (self.balance < self.item_price):
            money_deficiency = self.item_price - self.balance
            print('\'You must deposit ${0}{1}'.format(money_deficiency, " more.\'"))
            return
        else:
            change = self.balance - self.item_price
            if (change > 0):
                print("\'Here is your {0} and ${1} change.\'".format(self.sale_item, self.balance - self.item_price))
            else:
                print("\'Here is your {0}.\'".format(self.sale_item))
            self.balance = 0
            self.item_stock -= 1;
            return

    def restock(self, item_num):
        self.item_stock += item_num
        print("\'Current", self.sale_item, "stock: {0}\'".format(self.item_stock))
        return

    def deposit(self, money_amount):
        if (self.item_stock == 0):
            print("\'Machine is out of stock. Here is your ${0}.\'".format(money_amount))
            return
        else:
            self.balance += money_amount
            print("\'Current balance: ${0}\'".format(self.balance))


# Q2

class interval:
    """A range of floating-point values.

    >>> a = interval(1, 4)
    >>> a
    interval(1, 4)
    >>> print(a)
    (1, 4)
    >>> a.low
    1
    >>> a.high
    4
    >>> a.low = 3    # .low and .high are read-only
    AttributeError
    >>> a.width
    3
    >>> a.width = 4
    AttributeError
    >>> b = interval(2, -2)  # Order doesn't matter
    >>> print(b, b.low, b.high)
    (-2, 2) -2 2
    >>> a + b
    interval(-1, 6)
    >>> a - b
    interval(-1, 6)
    >>> a * b
    interval(-8, 8)
    >>> b / a
    interval(-2.0, 2.0)
    >>> a / b
    ValueError
    >>> -a
    interval(-4, -1)
    """
    "*** YOUR CODE HERE ***"

    def __init__(self, low_num, high_num):
        num_list = [low_num, high_num]
        self.low = min(num_list)
        self.high = max(num_list)
        self.width = 3

    def __str__(self):
        return "({0}, {1})".format(self.low, self.high)

    def __add__(self, other):
        return interval(self.low + other.low, self.high + other.high)

    def __sub__(self, other):
        return self.__add__(-other)

    def __mul__(self, other):
        # options is the mutual result of low and high value of self and other
        options = [self.low * other.low, self.low * other.high, self.high * other.high, self.high * other.low]
        return interval(min(options), max(options))

    def __neg__(self):
        return interval(-self.high, -self.low)

    def __repr__(self):
        return "interval({0}, {1})".format(self.low, self.high)

    def __setattr__(self, key, value):
        if self.__dict__.__contains__(key):
            print("AttributeError")
            return
        else:
            object.__setattr__(self, key, value)

    def __truediv__(self, other):
        if (abs(self.low) == 1 or abs(self.high == 1)):
            print("ValueError")
            return
        else:
            options = [self.low / other.low / 1.0, self.low / other.high / 1.0, self.high / other.high / 1.0,
                       self.high / other.low / 1.0]
            return interval(min(options), max(options))

    def __floordiv__(self, other):
        if (abs(self.low) == 1 or abs(self.high == 1)):
            print("ValueError")
            return
        else:
            options = [self.low / other.low / 1.0, self.low / other.high / 1.0, self.high / other.high / 1.0,
                       self.high / other.low / 1.0]
            return interval(min(options), max(options))


# Q3

class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'
    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """

    def __init__(self, object_called):
        self.calling_object = object_called

    def ask(self, asking_words, *args):
        if "please" not in asking_words:
            print("\'You must learn to say please first.\'")
            return
        else:
            words = asking_words.split(" ", 1)
            if len(words) == 1:
                print("please give me an order")
                return
            else:
                order = words[1]
                order_func = getattr(self.calling_object, order,
                                     'Thanks for asking, but I know not how to {0}.'.format(order))
                if (callable(order_func)):
                    return order_func(*args)
                else:
                    return order_func

    "*** YOUR CODE HERE ***"


# Q4, Q5, and Q6

class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    >>> len(s)
    3
    >>> s[2]
    3
    >>> s = Link.empty
    >>> len(s)
    0
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __len__(self):
        """ Return the number of items in the linked list.

        >>> s = Link(1, Link(2, Link(3)))
        >>> len(s)
        3
        >>> s = Link.empty
        >>> len(s)
        0
        >>> len(ints_list(100000)) # Check for iterative solution
        100000
        """
        if self == Link.empty:
            return 0
        if self.rest == Link.empty:
            return 1
        iterator = self.rest
        length = 1
        while iterator != Link.empty:
            length = length + 1
            iterator = iterator.rest
        return length

        "*** YOUR CODE HERE ***"

    # The following method may be useful for implementation of the
    # __getitem__ and insert methods.
    def _get_link(self, i):
        """An internal utility method that returns the Ith Link after
        self (I == 0 returns self, I == 1 returns self.rest, etc.).  Returns
        empty if I is len(self).  Raises IndexError unless 0 <= I <= len(self).
        >>> L = Link(1, Link(2, Link(3)))
        >>> L._get_link(0)
        Link(1, Link(2, Link(3)))
        >>> L._get_link(1)
        Link(2, Link(3))
        >>> L._get_link(2)
        Link(3)
        >>> L._get_link(3)
        ()
        >>> L._get_link(4)
        Traceback (most recent call last):
           ...
        IndexError: list index out of range
        >>> L._get_link(-1)
        Traceback (most recent call last):
           ...
        IndexError: list index out of range
        >>> (ints_list(100000))._get_link(1).first
        2
        """
        if i < 0:
            raise IndexError("list index out of range")
        if i > len(self):
            raise IndexError("list index out of range")
        iterator = self
        while i > 0:
            iterator = iterator.rest
            i = i - 1
        return iterator

        "*** YOUR CODE HERE ***"

    def __getitem__(self, i):
        """Returns the element found at index I.

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1]
        2
        >>> s[2]
        3
        >>> (ints_list(100000))[1]  # Check for iterative solution
        2
        """
        assert i <= len(self) - 1 and i >= -len(self), 'the index is out of bound'
        if i < 0:
            i = len(self) + i
        while (i):
            self = self.rest
            i = i - 1
        return self.first

        "*** YOUR CODE HERE ***"

    def __add__(self, lst):
        """Returns the result of non-destructively appending LST to the
        end of the sequence starting with self.
        """
        if self == Link.empty:
            return lst
        "*** YOUR CODE HERE ***"
        if (lst == Link.empty):
            return self
        new_link = result = Link(self.first)
        iterator = self.rest
        while (iterator != Link.empty):
            new_link.rest = Link(iterator.first)
            new_link = new_link.rest
            iterator = iterator.rest
        new_link.rest = lst
        return result

    def insert(self, k, val):
        """Destructively insert VAL into the list headed by SELF at index
        K, moving the previous item K and later items right.  Returns the
        resulting linked list.  Assumes 0 <= K <= len(self).
        """
        if k < 0:
            raise IndexError("the index must be larger or equal to zero")
        else:
            if k == 0:
                return Link(val) + self
            else:
                if k > len(self):
                    print("IndexError")
                    return
                new_link = Link(self.first)
                iterator_new_link = new_link
                # iterate through original link to transfer it element into the new_link
                iterator_link = self
                while k > 1:
                    iterator_link = iterator_link.rest
                    iterator_new_link.rest = Link(iterator_link.first)
                    iterator_new_link = iterator_new_link.rest
                    k = k - 1
                # the rest of the iterator_new_link would be link of  which the first the val, the rest is and the rest of  iterator_link
                iterator_new_link.rest = Link(val, iterator_link.rest)
                self.first = new_link.first
                self.rest = new_link.rest
                return self

        "*** YOUR CODE HERE ***"


# ints_list is used to test that a method does not use recursion by making
# sure that a very long list does not cause a large recursion depth.
def ints_list(k):
    """A linked list containing the numbers 1 to K."""
    if k < 1:
        return Link.empty
    p = result = Link(1)
    for i in range(2, k + 1):
        p.rest = Link(i)
        p = p.rest
    return result


def add(L0, L1):
    """Return the list formed by non-destructively appending the items in L1
    to the end of those in L0.

    >>> s = Link(1, Link(2))
    >>> s + Link.empty
    Link(1, Link(2))
    >>> s + Link(3, Link(4))
    Link(1, Link(2, Link(3, Link(4))))
    >>> s   # Non-destructive
    Link(1, Link(2))
    >>> add(Link.empty, s)
    Link(1, Link(2))
    >>> s = ints_list(100000) + Link(100001)  # Check for iterative solution
    """
    if L0 is Link.empty:
        return L1
    else:
        return L0 + L1


def insert(L, k, val):
    """Destructively insert VAL into L at position K, returning the
    resulting list.  Assumes 0 <= K <= len(L).

    >>> L = Link(1, Link(2, Link(3)))
    >>> L.insert(1, 5)
    Link(1, Link(5, Link(2, Link(3))))
    >>> L
    Link(1, Link(5, Link(2, Link(3))))
    >>> L.insert(4, 6)  # Insert off the end.
    Link(1, Link(5, Link(2, Link(3, Link(6)))))
    >>> L.insert(0, 7)  # Insert at front
    Link(7, Link(1, Link(5, Link(2, Link(3, Link(6))))))
    >>> L  # New element is "left of" L
    Link(1, Link(5, Link(2, Link(3, Link(6)))))
    >>> L.insert(6, 8)
    IndexError
    >>> insert((), 0, 3)
    Link(3)
    """
    if L == Link.empty:
        if k != 0:
            print("IndexError")
            return
        else:
            return Link(val)
    else:
        return L.insert(k, val)


class Tree:
    def __init__(self, label, children=()):
        self.label = label
        for branch in children:
            assert isinstance(branch, Tree)
        self.children = children

    def __repr__(self):
        if self.children:
            children_str = ', ' + repr(self.children)
        else:
            children_str = ''
        return 'Tree({0}{1})'.format(self.label, children_str)

    def is_leaf(self):
        return not self.children


# Q7


def same_shape(t1, t2):
    """Returns whether two Trees t1, t2 have the same shape. Two trees have the
    same shape iff they have the same number of children and each pair
    of corresponding children have the same shape.

    >>> t, s = Tree(1), Tree(3)
    >>> same_shape(t, t)
    True
    >>> same_shape(t, s)
    True
    >>> t = Tree(1, [Tree(2), Tree(3)])
    >>> same_shape(t, s)
    False
    >>> s = Tree(4, [Tree(3, [Tree(2, [Tree(1)])])])
    >>> same_shape(t, s)
    False
    """
    if not isinstance(t1, Tree) or not isinstance(t2, Tree):
        return False
    if len(t1.children) != len(t2.children):
        return False
    else:
        n = len(t1.children) - 1
        while n >= 0:
            if not same_shape(t1.children[n], t2.children[n]):
                return False
            n = n - 1
        return True
    "*** YOUR CODE HERE ***"


class Tree:
    def __init__(self, label, children=()):
        self.label = label
        for branch in children:
            assert isinstance(branch, Tree)
        self.children = list(children)

    def __repr__(self):
        if self.children:
            children_str = ', ' + repr(self.children)
        else:
            children_str = ''
        return 'Tree({0}{1})'.format(self.label, children_str)

    def is_leaf(self):
        return not self.children

    def tree_length(self):
        if self.is_leaf():
            return 0
        else:
            max_child_length = 0
            for child in self.children:
                assert isinstance(child, Tree)
                length = child.tree_length()
                if length > max_child_length:
                    max_child_length = length
            return max_child_length + 1


# Q8

def long_paths(tree, n):
    """Return a list all paths in tree with length at least n.

    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12)])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    Link(0, Link(1, Link(2)))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(5))))
    Link(0, Link(6, Link(7, Link(8))))
    Link(0, Link(6, Link(9)))
    Link(0, Link(11, Link(12)))
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(4))))
    Link(0, Link(1, Link(3, Link(5))))
    Link(0, Link(6, Link(7, Link(8))))
    >>> long_paths(whole, 4)
    []
    """
    "*** YOUR CODE HERE ***"
    assert isinstance(tree, Tree)
    if tree.is_leaf():
        if n > 0:
            return []
        else:
            return [Link(tree.label)]
    if tree.tree_length() < n:
        return []
    else:
        path_list = []
        for child in tree.children:
            child_long_paths = long_paths(child, n - 1)
            for child_long_path in child_long_paths:
                if child_long_path.__len__() > n - 1:
                    path_list.append(Link(tree.label, child_long_path))
        return path_list
