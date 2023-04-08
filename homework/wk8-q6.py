# Write an algorithm that checks whether a string is a palindrome

def palin(str):
    # base case, a string with length 1 is the same forwards and backwards
    if len(str) < 2:
        return True
    # recursion, evauluates both parts of return as a boolean value, then passes the 
    # string, minus the first and last characters, to the next recursion of palin()
    else:
        return str[0] == str[-1] and palin(str[1:-1])

print(palin("sales"))
print(palin("seles"))