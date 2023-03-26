# 1. Given a list of numbers, return a new list with only the elements of the first list that have a value greater than 1000

def fourDigits(listOfNumbers):
    greaterThan = []

    for i in listOfNumbers:
        if i > 1000:
            greaterThan.append(i)
    
    return greaterThan

testArr = [24, 233545, 1, 35, 366, 2320, 1992]

print(fourDigits(testArr))