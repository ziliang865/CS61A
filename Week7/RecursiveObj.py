from Week6.Efficiency import memo


class Link():
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            assert self.rest != Link.empty, 'The index is out of bound'
            return self.rest[i - 1]

    def __len__(self):
        return 1 + len(self.rest)

    def link_expression(self):
        if self.rest is Link.empty:
            rest = ''
        else:
            rest = ',' + self.rest.link_expression()
        return "Link({0}{1})".format(self.first, rest)

    def __repr__(self):
        return self.link_expression()

    def __str__(self):
        return self.__repr__()

    class _iterator:
        def __init__(self,start):
            self._next_item=start
        def __next__(self):
            if self._next_item==Link.empty:
                raise StopIteration
            else:
                ele=self._next_item.first
                self._next_item=self._next_item.rest
                return ele
    def __iter__(self):
        return Link._iterator(self)
for i in Link(3,Link(4,Link(5,Link(10)))):
    print(i)

lst = Link(Link(3, Link(5)), Link(6))
print(lst.link_expression())


def extend_link(s, t):
    if s == Link.empty:
        return t
    else:
        return Link(s.first, extend_link(s.rest, t))


Link.__add__ = extend_link
tuple = extend_link
lst2 = Link(3, Link(4))
print(extend_link(Link(3), Link.empty))
print(extend_link(lst, lst2))


def map_link(f, l):
    if l == Link.empty:
        return l
    else:
        return Link(f(l.first), map_link(f, l.rest))


lst3 = Link(1, Link(4, Link(5)))
square = lambda x: x * x
print(map_link(square, lst3))


def filter_map(f, l):
    if l == Link.empty:
        return l
    else:
        filtered = filter_map(f, l.rest)
        if (f(l.first)):
            return Link(l.first, filtered)
        else:
            return filtered


filter_func = lambda x: x % 2 == 0
print(filter_map(filter_func, lst3))


def join_link(seperator, lst):
    if lst == Link.empty:
        return ""
    if lst.rest is Link.empty:
        return str(lst.first)
    else:
        return str(lst.first) + seperator + join_link(seperator, lst.rest)


print(join_link(",", lst3))


def partition(n, m):
    if n == 0:
        return Link(Link.empty)
    elif n < 0 or m == 0:
        return Link.empty
    else:
        using_m = partition(n - m, m)
        with_m = map_link(lambda s: Link(m, s), using_m)
        without_m = partition(n, m - 1)
        if with_m == Link.empty:
            return without_m
        else:
            return with_m + without_m


def print_partitions(n, m):
    lists = partition(n, m)
    strings = map_link(lambda s: join_link("+", s), lists)
    print(join_link("\n", strings))


print_partitions(7, 7)


class Tree:
    def __init__(self, entry, branches=()):
        self.entry = entry
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.entry, repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.entry))

    def is_leaf(self):
        return not self.branches


def fib_tree(n):
    if n == 1:
        return Tree(0)
    if n == 2:
        return Tree(1)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        return Tree(left.entry + right.entry, (left, right))


def sum_entries(t):
    return t.entry + sum([sum_entries(branch) for branch in t.branches])


print(sum_entries(fib_tree(5)))
fib_tree = memo(fib_tree)
big_fib_tree = fib_tree(35)
print(big_fib_tree.entry)
print(big_fib_tree.branches[0] is big_fib_tree.branches[1].branches[1])
sum_entries = memo(sum_entries)
print(sum_entries(big_fib_tree))
s = {3, 2, 1, 4, 4}
print(s)
print(3 in s)
len(s)
print(s.union({5, 6}))
print(s.intersection({3, 5, 6, 4, 3}))


def empty(s):
    return s is Link.empty


def set_contains(s, v):
    if empty(s):
        return False
    if s.first == v:
        return True
    else:
        return set_contains(s.rest, v)


def adjoin_set(s, v):
    if set_contains(s, v):
        return s
    else:
        return Link(v, s)


s = Link(3, Link(4))
print(set_contains(s, 4))
print(adjoin_set(s, 5))


def keep_if_link(s, f):
    if s == Link.empty:
        return s
    else:
        if (f(s.first)):
            return Link(s.first, keep_if_link(s.rest, f))
        else:
            return keep_if_link(s.rest, f)


def intersect_set(set1, set2):
    return keep_if_link(set1, lambda v: set_contains(set2, v))


s2 = Link(3, Link(5))
print(intersect_set(s, s2))


def union_set(set1, set2):
    uni_set = keep_if_link(set1, lambda v: not set_contains(set2, v))
    return extend_link(uni_set, set2)


print(union_set(s, s2))


def set_contains_seq(s1, v):
    if s1 == Link.empty or v < s1.first:
        return False
    if v == s1.first:
        return True
    else:
        return set_contains_seq(s1.rest, v)


u = Link(1, Link(4, Link(5)))
print(set_contains_seq(u, 0))


def interact_set_seq(s1, s2):
    if s1 == Link.empty or s2 == Link.empty:
        return Link.empty
    e1 = s1.first
    e2 = s2.first
    if e1 == e2:
        return Link(e1, interact_set_seq(s1.rest, s2.rest))
    if e1 < e2:
        return interact_set_seq(s1.rest, s2)
    if e1 > e2:
        return interact_set_seq(s1, s2.rest)


def union_set_seq(s1, s2):
    if s2 == Link.empty or s1 == Link.empty:
        if s2 == Link.empty:
            return s1
        else:
            return s2
    e1 = s1.first
    e2 = s2.first
    if e1 == e2:
        return union_set_seq(s1, s2.rest)
    if e1 < e2:
        return Link(e1, union_set_seq(s1.rest, s2))
    if e1 > e2:
        return Link(e2, union_set_seq(s1, s2.rest))



v = Link(1, Link(5, Link(6)))
print(interact_set_seq(u, v))
print(union_set_seq(u, v))
