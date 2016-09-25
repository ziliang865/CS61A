def frequency(L):
    result={}
    for word in L:
        if not (word in result):
            result[word]=1
        else:
            result[word]+=1
    return result
print(frequency(['the', 'name', 'of', 'the', 'name', 'of', 'the', 'song']))
def is_duplicate(L):
    items={}
    for x in L:
        if(x in items):
            return True
        items[x]=True
    return False
print(is_duplicate(['the', 'name', 'of', 'the', 'name', 'of', 'the', 'song']))
items={}
items["add"]=1
list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
String1="the"
String2="the"
Tuple1=(1,2,3)
Tuple2=(1,2,3)
print(String1==String1)
print(String1 is String2)
print(Tuple1==Tuple2)
print(Tuple1 is Tuple2)
