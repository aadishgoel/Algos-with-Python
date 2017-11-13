def fact_iterative(n):
    ans=1
    for i in range(1,n):
        ans*=i
    return ans

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1)+fib(n-2)
