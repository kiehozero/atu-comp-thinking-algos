# notepad for code runner assessments

def factorial_buzz(number):
    if number == 0:
        fac = 1
    elif number == 1:
        fac = 1
    else:
        fac = 1
        for n in range(1,number + 1):
            fac = n * fac
    if number % 3 == 0:
        ans = "Fizz! the factorial is " + str(fac)
    elif number % 5 == 0:
        ans = "Buzz! the factorial is " + str(fac)
    else:
        ans = fac
    return ans

print(factorial_buzz(10))