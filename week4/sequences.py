from operator import mul
pairs=[[2,2],[2,2],[2,3],[4,4]]

same_count=0
for x in pairs:
    for y in pairs:
        print(x,y)
        if x==y:
          same_count=same_count+1

print(same_count)
print(list(range(1,10)))
value=list(range(1,10))
print(value)
print(range(4,9))
for _ in range(4,10):
    print(_)
    print("Go bears")
odds=[1,3,5,7,9]
mylists=[x+1 for x in odds]
print(mylists)
def devisors(n):
    return [x for x in range(1,n) if n%x==0]
print(devisors(20))
#sum 函数不需要import 可以直接使用 range 和 list comprehension也是
a=[ n for n in range(1,1000) if sum(devisors(n))==n ]
print(a)
def width(area,height):
    assert area%height==0
    return area//height
def perimeter(width,height):
    return 2*width+2*height
def minimum_perimeter(area):
    devisors(area)
    perimeters=[perimeter(width(area,h),h) for h in devisors(area)]
    return min(perimeters)
area=80
print(width(area,5 ))
print(perimeter(16,5))
print(minimum_perimeter(area))
print([minimum_perimeter(n) for n in range(2,10)])
def apply_to_all(map_fn,s):
    return [map_fn(x) for x in s]
def keep_if(filter_fn,s):
    return [x for x in s if filter_fn(x)]
def reduce(redunce_fn,s,initial):
    reduced=initial
    for x in s :
        reduced=redunce_fn(reduced,x)
    return reduced
print(reduce(mul,[2,4,8],1))
#list 可以和 list相加
def divisors_of(n):
        divides_n=lambda x:n%x==0
        return [1]+keep_if(divides_n,range(2,n))
print(divisors_of(12))
from operator import add
def sum_of_divisors(n):return reduce(add,divisors_of(n),0)
print(sum_of_divisors(12))
def perfect(n):
    return sum_of_divisors(n)==n
print(keep_if(perfect,range(1,1000)))
from functools import reduce
s=[1,2,3,5,6]
print(reduce(mul,s))
def is_leaf(tree):
    return isinstance(tree,int)
def right_binarize(tree):
    if is_leaf(tree):
        return tree
    else :
        if (len(tree))>2 or len(tree)==2:
            tree=[tree[0],tree[1:]]
            return [right_binarize(b) for b in tree]
print(right_binarize([1,2,3,4,5,6,7,8,9,10]))
def branches(tree):
    return tree[1:]
def root(tree):
    return tree[0]
def is_tree(tree):
    if type(tree)!=list or len(tree)<1 :
        return  False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
def is_leaf(tree):
    return not branches(tree)
def tree(root,branches=[]):
    for branch in branches:
        assert is_tree(branch),  'branch must be trees'
    return [root]+list(branches)
t=tree(3,[[1],[2]])
print(t)
def fib_tree(n):
    if n==1 or n==0 :
        return tree(n)
    else:
        left,right=fib_tree(n-2),fib_tree(n-1)
        fib_n=root(left)+root(right)
    return tree(fib_n,[left,right])
print(fib_tree(5))
def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else :
        leaves_counts=[count_leaves(branch) for branch in branches(tree)]
        return sum(leaves_counts)
print(count_leaves(fib_tree(5)))


#2016  7 11 完成的内容
empty= "empty"
def is_link(s):
    return s==empty or(len(s)==2 and is_link(s[1]))
def link(first,rest):
    assert  is_link(rest)
    return  [first,rest]

def first(s):
    assert is_link(s)
    assert s[0]!=empty
    return s[0]

def rest(s):
    assert is_link(s)
    assert s[0] != empty
    return s[1]

def len_link(s):
    len=0
    while(s!=empty):
        s=rest(s)
        len=len+1
    return len



def getitem_link(s,i):
    #assert is_link(s), "s is not a link"
    assert i>=0,  "i is not valid"
    count=0
    cur_ele=s
    while(count<i):
        count,cur_ele=count+1,rest(cur_ele)
    return first(cur_ele)

four=link(1,link(2,link(3,link(4,empty))))
print(four)
print(first(four))
print(rest(four))
print(len_link(four))
print(getitem_link(four,4))
def len_link_recursive(s):
    assert is_link(s),"s is not a link"
    if(s==empty):
        return 0
    else :
        return 1+len_link_recursive(rest(s))
def getitem_link_recursive(s,i):
    assert is_link(s), "s is not a link"
    if(i==0):
        return first(s)
    if(s==empty ):
        print("i is not valid")
        return
    else :
        return getitem_link_recursive(rest(s),i-1)
print(getitem_link_recursive(four,4))

