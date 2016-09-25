from ucb import trace
def memorized_count_change(amount,coins=(50,25,10,5,1)):
    memo_table={}
    def count_change(amount,coins):
        if (amount,coins) not in memo_table:
           memo_table[(amount,coins)]=full_count_change(amount,coins)
        return memo_table[amount,coins]
    def full_count_change(amount,coins):
        if amount==0:
            return 1
        if amount<0 or len(coins)==0:
            return 0
        elif amount>=coins[0]:
            return count_change(amount-coins[0],coins)+\
                count_change(amount,coins[1:])
        else:
             return count_change(amount,coins[1:])
    return count_change(amount,coins)

    #with full_count_change being traced
def traced_count_change(amount,coins = (50, 25, 10, 5, 1)):
    memo_table={}
    def count_change(amount,coins):
        if (amount, coins) not in memo_table:
            memo_table[(amount, coins)] = full_count_change(amount, coins)
        return memo_table[amount, coins]
    @trace
    def full_count_change(amount,coins):
            if amount == 0:
                return 1
            if amount < 0 or len(coins) == 0:
                return 0
            elif amount < coins[0]:
                return count_change(amount, coins[1:])
            else:
                return count_change(amount - coins[0], coins) + \
                       count_change(amount, coins[1:])
    return count_change(amount, coins)
    #dynamic programming version of count_change
def count_change(amount,coins = (50, 25, 10, 5, 1)):
        #initialed_memo_table
        memo_table = [[-1]*(len(coins)+1) for i in range(amount+1)]
        def count_change(amount,coins):
            if memo_table[amount][len(coins)]==-1:
                raise RuntimeError("unfilled memo: {0}, {1}".format(amount,len(coins)))
            else:
                return full_count_change(amount,coins)
        def full_count_change(amount,coins):
            if amount == 0:
                return 1
            elif  len(coins)==0 or amount<0:
                return 0
            elif amount<coins[0]:
                return count_change(amount,coins[1:])
            else:
                return count_change(amount - coins[0], coins) + \
                       count_change(amount, coins[1:])
        for a in range(0,amount+1):
            memo_table [a][0]=full_count_change(a,())
        for k in range(1,len(coins)+1):
            for a in range(0, amount + 1):
                memo_table[a][k]=full_count_change(a,coins[-k:])
        return count_change(amount,coins)

print(count_change(10))
print(traced_count_change(10))