
# wrote this for the programming language.
def fibonacci(f):
    if(f <= 1):
        return f
    fib = fibonacci(f - 1) + fibonacci(f - 2)
    # print(fib)
    return fib

# implementing fibonacci with memoization
def fibonaccimemo(i, memo):
    if(i <= 1):
        return i
    
    if(memo[i] == 0):
        memo[i] = fibonaccimemo(i-1, memo) + fibonaccimemo(i-2, memo)
        # print(i)
    
    # print(memo)
    return memo[i]


print(fibonacci(20))

memo = []
n = 20
for i in range(n+1):
    memo.append(0)
print(fibonaccimemo(n, memo))

