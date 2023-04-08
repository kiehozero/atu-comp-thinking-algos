# Write an algorithm that returns the reverse of a given string

def reverse(str):
    # base case, a string with length 1 is the same forwards and backwards
    if str == "" or len(str) == 1:
        return str
    # recursion
    else:
        return reverse(str[1:]) + str[0]

print(reverse("Stuart"))
