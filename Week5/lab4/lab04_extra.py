from lab04 import *

# Q7
def reverse_iter(lst):
    """Returns the reverse of the given list.

    >>> reverse_iter([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse_iter([5,6,7,8])
    [8, 7, 6, 5]
    """
    revers_list=[]
    i=1
    while i<=list.__len__(lst):
        revers_list.append(lst[-i])
        i=i+1
    return revers_list
from doctest import run_docstring_examples
run_docstring_examples(reverse_iter, globals(), True)
"*** YOUR CODE HERE ***"

# Q8
def list_to_link(lst):
    """Converts a list to a linked list.

    >>> lst = [1, 2, 3, 4]
    >>> r = list_to_link(lst)
    >>> first(r)
    1
    >>> first(rest(rest(r)))
    3
    >>> r = list_to_link([])
    >>> r is empty
    True
    """
    if(lst==[]):
        return empty
    elif(list.__len__(lst)==1):
        return [lst[0],empty]
    else:
        return link(lst[0],list_to_link(lst[1:]))


run_docstring_examples(list_to_link, globals(), True)
"*** YOUR CODE HERE ***"

# Q9
def has_prefix(s, prefix):
    """Returns whether prefix appears at the beginning of linked list s.

    >>> x = link(3, link(4, link(6, link(6))))
    >>> print_link(x)
    3 4 6 6
    >>> has_prefix(x, empty)
    True
    >>> has_prefix(x, link(3))
    True
    >>> has_prefix(x, link(4))
    False
    >>> has_prefix(x, link(3, link(4)))
    True
    >>> has_prefix(x, link(3, link(3)))
    False
    >>> has_prefix(x, x)
    True
    >>> has_prefix(link(2), link(2, link(3)))
    False
    """
    if prefix==empty :
        return True
    while(prefix!=empty):
        if(s==empty):
            return False
        s_ele_test,prefix_ele_test=first(s),first(prefix)
        if(s_ele_test!=prefix_ele_test):
            return False
        s=rest(s)
        prefix=rest(prefix)
    return True
    "*** YOUR CODE HERE ***"
run_docstring_examples(has_prefix, globals(), True)
def has_sublist(s, sublist):
    """Returns whether sublist appears somewhere within linked list s.

    >>> has_sublist(empty, empty)
    True
    >>> aca = link('A', link('C', link('A')))
    >>> x = link('G', link('A', link('T', link('T', aca))))
    >>> print_link(x)
    G A T T A C A
    >>> has_sublist(x, empty)
    True
    >>> has_sublist(x, link(2, link(3)))
    False
    >>> has_sublist(x, link('G', link('T')))
    False
    >>> has_sublist(x, link('A', link('T', link('T'))))
    True
    >>> has_sublist(link(1, link(2, link(3))), link(2))
    True
    >>> has_sublist(x, link('A', x))
    False
    """
    if(s==empty):
        if(sublist==empty):
            return True
        return False
    while(s!=empty):
        if has_prefix(s,sublist):
            return True
        s=rest(s)
    return False
run_docstring_examples(has_sublist, globals(), True)
"*** YOUR CODE HERE ***"

def has_61A_gene(dna):
    """Returns whether linked list dna contains the CATCAT gene.

    >>> dna = link('C', link('A', link('T')))
    >>> dna = link('C', link('A', link('T', link('G', dna))))
    >>> print_link(dna)
    C A T G C A T
    >>> has_61A_gene(dna)
    False
    >>> end = link('T', link('C', link('A', link('T', link('G')))))
    >>> dna = link('G', link('T', link('A', link('C', link('A', end)))))
    >>> print_link(dna)
    G T A C A T C A T G
    >>> has_61A_gene(dna)
    True
    >>> has_61A_gene(end)
    False
    """
    CS_61A_DNA=link('C', link('A', link('T', link('C', link('A',link('T'))))))
    return has_sublist(dna,CS_61A_DNA)
    "*** YOUR CODE HERE ***"
