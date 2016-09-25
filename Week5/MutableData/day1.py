chinese = ['coin', 'string', 'myriad']
suits = chinese
suits.pop()
suits.remove("coin")
suits = ['heart', 'diamond', 'spade', 'club']
nest = list(suits)
nest[0] = suits
suits.insert(2, "Joker")
joke = nest[0].pop(2)
print(suits)
print(joke)
test = suits is nest[0]
test2 = suits is ['heart', 'diamond', 'spade',
                  'club']
print(test)
print(test2)
test3 = suits == ['heart', 'diamond', 'spade',
                  'club']
print(test3)
from unicodedata import lookup

balance = 30


def make_withdraw(balance):
    balance2 = 30

    def withdraw(amout):
        nonlocal balance
        if balance < amout:
            print("balance is not enough")
            return
        else:
            balance = balance - amout
        return balance

    return withdraw


def getitem_link(s,i):
    #assert is_link(s), "s is not a link"
    assert i>=0,  "i is not valid"
    count=0
    cur_ele=s
    while(count<i):
        count,cur_ele=count+1,rest(cur_ele)
    return first(cur_ele)

withdraw = make_withdraw(200)
print(withdraw(20))
withdraw(190)
# 2016 7 21内容

empty = "empty"


def is_link(s):
    return s == empty or (len(s) == 2 and is_link(s[1]))


def link(first, rest):
    assert is_link(rest)
    return [first, rest]


def first(s):
    assert is_link(s)
    assert s[0] != empty
    return s[0]


def rest(s):
    assert is_link(s)
    assert s[0] != empty
    return s[1]


def len_link(s):
    len = 0
    while (s != empty):
        s = rest(s)
        len = len + 1
    return len


def mutable_link():
    contents = empty
    def dispatch(message, value=None):
        nonlocal contents
        if  message == "len":
            return len_link(contents)
        elif message == "get_item":
            assert value != None, "Wrong Index"
            return getitem_link(contents, value)
        elif message == "push_list":
            contents=link(value,contents)
            return contents
        elif message=="pop_list" :
            f=first(contents)
            contents=rest(contents)
            return f
        elif message=="str":
            return str(contents)
    return dispatch

def to_mutable_link(source):
    costume_list=mutable_link()
    for element in reversed(source):
        costume_list("push_list",element)
    return costume_list("get_item",1)
source=["fsdsfd","sfsfdfsdfsd"]
print(to_mutable_link(source))
list2=mutable_link()
for i in range(10):
    list2("push_list",i)
print(list2("str"))
def dictionary():
    contents=[]
    def get_item(key):
       results= [ result for result in contents if result[0]==key]
       if len(results)==1:
           return results[0][1]
    def set_item(key,value):
        nonlocal contents
        pair=[key,value]
        results=[result for result in contents if result[0]!= key]
        #下面是构建新result的方法
        results=results+[pair]
        contents=results
        return contents
    def dispatch(message,key=None,value=None):
         if(message=="get_item"):
             return get_item(key)
         if(message=="set_item"):
            return set_item(key,value)

    return dispatch
costume_dict=dictionary()
print(costume_dict("set_item","first","key"))
print(costume_dict("set_item",10,9))
print(costume_dict("get_item","first"))
def account(initial_balance):
    def deposit(amount):
         dispatch['balance']+=amount
    def withdraw(amount):
        assert (amount<dispatch['balance']),"balance is not enough"
        dispatch['balance']-=amount
    dispatch={'deposit':deposit,'withdraw':withdraw,'balance':initial_balance}
    return dispatch
def withdraw(account,amount):
    return account['withdraw'](amount)
def deposit(account,amount):
    return account['deposit'](amount)
def check_balance(account):
    return account['balance']
test_account=account(666)
withdraw(test_account,50)
print(check_balance(test_account))
deposit(test_account,70)
print(check_balance(test_account))



from operator import add,sub
#函数里面的函数和变量，对象作为返回值返回都是可行的，可以继续使用的。例如下面一个例子，返回dict后，如果将返回的dict赋值给一个引用，那么以后对这个引用的所有操作，都可以对返回的字典产生影响。
def converter(source,target):


def adder(a,b,c):
    return make_ternary_constraint(a,b,c,add,sub,sub)
def make_ternary_constraint(a,b,c,ab,ac,bc):
    va,vb,vc=[connector('has_val')for connector in(a,b,c)]
    if(va and vb):
        c['set_val'](constraints,ab(a,b))
    constraints={'value_set':value_set,}




def connector(Name=None):
    informant=None
    constraints=[]
    #根据源constraints查看舍否已经了值，没有设定值就设定一下。并且通知除了源constraints的其他constraints
    def set_values(source,value):
        nonlocal informant
        val=connector_dict['val']
        if val==False:
            informant,connector_dict['val']=source,value
            inform_excpet_souce(source, "value_set")
            if(Name!=None):
              print(Name,"=",value)
        else:
            if val!=value:
                print("A contraction between the ",val,value)
    def inform_excpet_souce(souce,message=None):
        for constraint in constraints:
            if(constraint!=source):
                constraint[message]()
    def forget_value(source):
        nonlocal informant
        if(informant==source):
            inforamant, connector_dict['val'] = None, None
            inform_excpet_souce(source,'forget_value')
            if(Name!=None):
                print(Name,"has forgotten its value")
    connector_dict={'val':None,'set_val':set_values,'forget':forget_value,'has_val':lambda:connector_dict['val']is not None,'connect': lambda source:constraints.append(source)}
    return connector_dict
def constant(connector,value):
    constraint_dict={}
    connector['set_val'](constraint_dict,value)
    return constraint_dict




