class Account:
    """A bakn account that has a non-negtaive balance """
    _total_deposit=0
    interest=0.02
    def __init__(self,account_holder):
        self.balance=0
        self.holder=account_holder
    def __bool__(self):
        self.balance!=0
    def deposit(self,amount):
        '''Increase the account balance and return new balance'''
        self.balance+=amount
        Account._total_deposit+=amount
        return self.balance

    def withdraw(self,amount):
        '''Decrease the account balance and return new balance '''
        if amount>self.balance:
            return 'Insufficient funds'
        else :
            self.balance=self.balance-amount
            return self.balance
class checkingAccount(Account):
    withdraw_charge=1
    interest=0.01
    def withdraw(self,amount):
        return Account.withdraw(self,amount+self.withdraw_charge)
a=Account('Damy')
Account.__bool__=lambda self:self.balance!=0
print(a.balance)
print(a.holder)
b=Account("Spock")
b.balance=200
print([acc.balance for acc in (a,b)])
print(a is a )
print(not (a is b))
c=a
print(c is a )
print (c is not b)
print(getattr(b,"holder"))
print(type(Account.deposit))
print(type(b.deposit))
Account.deposit(b,20)
print(b.balance)
a.deposit(30)
print(a.balance)
print(getattr(Account,"deposit"))
print(a.interest)
print(b.interest)
a.interest=0.05
print(a.interest)
print(b.interest)
checking=checkingAccount('Sam')
checking.deposit(100)
print(checking.withdraw(99))
print(checking.interest)
class Polygon:
    def is_simple(self):
        '''True if I am simple (non-intersection)'''
        raise NotImplemented
    def area(self):
        '''caulcate the are of the this pologon'''
        raise NotImplemented
    def verticles(selfs):
        raise NotImplemented
    def bbox(self):
        V=self.verticles()
        xlow,ylow=xhigh,yhigh=V[0]
        for x,y in V[1:]:
            xlow,ylow=min(x,xlow),min(y,ylow)
            xhigh,yhigh-max(x,xhigh), max(y,yhigh)
        return xlow,ylow,xhigh,yhigh
    def num_slides(self):
        return len(self.verticles())
    def describe(self):
        return "A polygon with verticles {0}",format(self.verticles)
#abstract class就是未完全实现类中所有方法的类
class SimplePloygon(Polygon):
    def is_simple(self): return True
    def area(self):
        a=0.0
        V=self.verticles()
        for i in range(len[V]-1):
            a+=V[i][0] * V[i+1][1] - V[i+1][0]*V[i][1]
            return -0.5*a
class Square(SimplePloygon):
    def __init__(self,xll,yll,side):
        """A square with lower-left corner at (xll,yll) and
        given length on a side."""
        self._x = xll
        self._y = yll
        self._s = side
    def verticles(self):
        x0, y0, s = self._x, self._y, self._s
        return ((x0, y0), (x0, y0 + s), (x0 + s, y0 + s),
                (x0 + s, y0), (x0, y0))
    def desscribe(self):
        return "A {0}x{0} square with lower-left corner ({1},{2})" \
            .format(self._s, self._x, self._y)
    class Printable:
        def left_bracket(self):
            return type(self).__name__+"["
        def right_bracket(self):
            return "]"
        def __str__(self):
            result=self.left_bracket()
            for i in range(len(self)-1):
                result+=str(self[i])+","
            if(len(self)>0):
                result+=str(self[-1])
            result+=self.right_bracket()
    class Myseq(list,Printable):
        def print(self):
            print("end")
    a=Myseq()
    a=[1,2,3,5,6]
    print(a)
class Transformer():
    def magnify(self):
        print("manify in ",type(self).__name__)
class CountedTransformer(Transformer):
    _count=0
    def magnify(self):
        CountedTransformer._count +=1
        print(super.__name__)
        super().magnify()
        Transformer.magnify(self)
        print(super().__class__)
        print(Transformer.__name__)
        print(type(self).__name__)
    def count(self):
        return self._count
CTF=CountedTransformer()
print(bool(Account("Jack")))
print("Go_Bears".__getitem__(3))
CTF.magnify()
def make_adder(n):
    def adder(k):
        nonlocal n
        n=n+k
        return n
    return adder
adder=make_adder(29)
print(adder(30))
print(adder(40))
class adder(object  ):
    def __init__(self,n):
        self.n=n
    def __call__(self,k):
        return self.n+k
new_adder=adder(10)
print(new_adder(20))
print(new_adder(30))

def replace_all_deep (d,x,y):
    for key in d.keys():
        if type(d[key])==dict:
            replace_all_deep(d[key],x,y)
        else:
            if(d[key]==x):
                d[key]=y
d = {1: {2:{4: 4, 5: {4: 4, 5: 3}}, 3: 4}, 2: {4: 4, 5: 3},2:{1: {2:{4: 4, 5: {4: 4, 5: 3}}, 3: 4}, 2: {4: 4, 5: 3}}}
replace_all_deep(d, 3, 1)
print(d)
