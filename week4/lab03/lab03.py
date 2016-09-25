from utils import *

# Q1
from math import sqrt
from operator import mul
from doctest import run_docstring_examples
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    >>> distance(city3,city4)+distance(city3,city4)
    10.0
    """
    #计算lat_dist_squa和lon_dist_squa并在后面用sqrt求平方根
    lat_dist_squa=mul(get_lat(city1)-get_lat(city2),get_lat(city1)-get_lat(city2))
    lon_dist_squa=mul(get_lon(city1)-get_lon(city2),get_lon(city1)-get_lon(city2))
    return sqrt(lat_dist_squa+lon_dist_squa)
    "*** YOUR CODE HERE ***"
run_docstring_examples(distance,globals(),True)
# Q2
def closer_city(lat, lon, city1, city2):
    """ Returns the name of either city1 or city2, whichever is closest
        to coordinate (lat, lon).

        >>> berkeley = make_city('Berkeley', 37.87, 112.26)
        >>> stanford = make_city('Stanford', 34.05, 118.25)
        >>> closer_city(38.33, 121.44, berkeley, stanford)
        'Stanford'
        >>> bucharest = make_city('Bucharest', 44.43, 26.10)
        >>> vienna = make_city('Vienna', 48.20, 16.37)
        >>> closer_city(41.29, 174.78, bucharest, vienna)
        'Bucharest'
    """
    location_unname=make_city("location_unname",lat,lon)
    return get_name(city1) if distance(city1,location_unname)<distance(city2,location_unname) else get_name(city2)
    "*** YOUR CODE HERE ***"
run_docstring_examples(closer_city,globals(),True)

# Q3
def ab_plus_c(a, b, c):
    """Computes a * b + c.

    >>> ab_plus_c(2, 4, 3)  # 2 * 4 + 3
    11
    >>> ab_plus_c(5,10,15)
    65
    >>> ab_plus_c(0, 3, 2)  # 0 * 3 + 2
    2
    >>> ab_plus_c(3, 0, 2)  # 3 * 0 + 2
    2
    """
    "*** YOUR CODE HERE ***"
    if(a==0 or b==0):
        return c
    else :
        return b+ab_plus_c(a-1,b,c)
run_docstring_examples(ab_plus_c, globals(), True)
# Q4
def rise_testnumber(i):
     i=i+1
     return i
def test_number(i,n):
    if(i>sqrt(n)):
        return True
    else:
        if(n%i==0):
            return False
        else:
            return test_number(i+1,n)
def is_prime(n):
    """Returns True if n is a prime number and False otherwise. 

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    i=2
    return  test_number(i,n)

    "*** YOUR CODE HERE ***"

run_docstring_examples(is_prime, globals(), True)
# Q5
def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> # 1 + 2^2 + 3 + 4^2 + 5
    ... interleaved_sum(5, lambda x: x, lambda x: x*x)
    29
    """
    i=1
    measure_choice=0
    return calculate(n,i,measure_choice,odd_term,even_term)


    "*** YOUR CODE HERE ***"
#设置一个选择计算方法的状态量，每次递归时，该状态量从0,1之间来回变换
def calculate(n,i,measure_choice,odd_term,even_term):
    if(measure_choice==0):
        compute_way=odd_term
    if(measure_choice==1):
        compute_way=even_term
    if(n==i):
        return compute_way(i)
    else:
        temp_result=compute_way(i)
        return temp_result+calculate(n,i+1,1-measure_choice,odd_term,even_term)

run_docstring_examples(interleaved_sum, globals(), True)
you = 'fly'
yo, da = lambda do: you, lambda can: True
yo = yo('jedi')
da = False or ' you shall'
print(da)
print(yo+da)

def go(bears):
    gob = 3
    print(gob)
    return lambda ears: bears(gob)
gob = 4
bears = go(lambda ears: gob)
