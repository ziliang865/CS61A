def fib(n):
    if n==1:
       return 0
    if n==2:
        return 1
    return fib(n-2)+fib(n-1)



def count(f):
    def counted(*args):
        counted.call_count+=1
        return f(*args)
    counted.call_count=0
    return counted
def count_frame(f):
    def counted(*args):
        counted.openframe+=1
        counted.maxopenframe=max(counted.maxopenframe,counted.openframe)
        result=f(*args)
        counted.openframe-=1
        return result
    counted.openframe=0
    counted.maxopenframe=0
    return counted


def memo(f):
    cache={}
    def memorized(n):
        if n not in cache:
            cache[n]=f(n)
        return cache[n]
    return memorized
counted=count(fib)
fib=memo(counted)
print(fib(4))










