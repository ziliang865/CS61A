def make_instance(cls):
    attributes={}
    def get_value(name):
        '''return the value of the name'''
        if name in attributes:
            return attributes[name]
        else:
            value= cls['get'](name)
            assert value is not None,'cannot find the name in the instance'
            return bind_method(instance,value)
    #下面的设置method函数的目的是传递参数，然后调用value.将self参数设置为instance
    def bind_method(instance,value):
        if(callable(value)):
            def method(*args):
                return value(instance,*args)
            return method
        else:
            return value

    def set_value(name,value):
        attributes[name]=value

    instance = {'get': get_value, 'set': set_value}


    """
    def set_value(name,value):
       if get_value(name) is not None:
           attributes['name']=value
           return
       elif cls['get]'(name) is not None:
           cls['set'](name,value)
           return
       else:
           attributes['name']=value
    """
    return instance

#
def make_class(attributes,base_class=None):
    def get_value(name):
        if name in attributes:
            return attributes[name]
        elif base_class is not None:
            return base_class['get'](name)
    def set_value(name,value):
            attributes[name]=value
    def make_new(*args):
        return init_instance(cls,*args)
    def init_instance(cls,*args):
        instance=make_instance(cls)
        init=get_value("__init__")
        if(init):
            init(instance,*args)
        return instance
    cls={'get':get_value,'set':set_value,'new':make_new}
    return cls
def make_account_class():
    intrest=0.02
    def __init__(self,account_holder):
        self['set']('balance',0)
        self['set']('account_holder',account_holder)
    def withdraw(self,amount):
        balance=self['get']('balance')
        if amount>balance :
            return 'insufficient balance'
        balance=balance-amount
        self['set']('balance',balance)
        return balance
    def deposit(self,amount):
        balance = self['get']('balance')
        balance = balance + amount
        self['set']('balance', balance)
        return balance
    return make_class(locals())
Account=make_account_class()
Account1=Account['new']("Deams")
print(Account1['get']('account_holder'))
deposit=Account1['get']('deposit')
deposit(20)
print(Account1['get']('balance'))
