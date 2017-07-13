# uses python3
fib_table={} #memoization table to store previous terms

def fib_num(n):
    if (n<=1):
        return n
    
    if n not in fib_table:
        fib_table[n]= fib_num(n-1) + fib_num(n-2)
        
    return fib_table[n]

n=int(input("enter nth term of fibonacci\n"))
print( "The fibonacci number for ", n, "is ", fib_num(n))
