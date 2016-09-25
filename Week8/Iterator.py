class Range:
    """A range of integers
    >>>for p in Range(1,3):print p
    1
    2
    """
    class _RangeIterator:
        def __init__(self,aRange):
            self._i,self._high=aRange.low,aRange.high
        def __next__(self):
            if self._i>=self._high:
                raise StopIteration
            else:
                self._i+=1
                return self._i-1
    def __init__(self,low,high):
        self._low,self._high=low,high
    def __iter__(self):
        return Range._RangeIterator(self)


