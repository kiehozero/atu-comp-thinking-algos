# write an algorithm that calculates the nth number in the Fibonacci sequence. Assume the sequence begins 0,1,1,2...
# solution from https://www.programiz.com/python-programming/examples/fibonacci-recursion

def recur_fibo(n):
    # base case
    if n <= 1:
        return n
    # recursion
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
    
print(recur_fibo(9))