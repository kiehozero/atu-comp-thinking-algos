# Given a string return true if the first instance of ’x’ in the string is followed by another x.

testStr = "speakerboxxx/the love below"

def xfind(xString):
    lng = len(xString) - 2
    i = 0
    while i < lng:
        if xString[i] == "x":
            j = i + 1
            if xString[j] == "x":
                print("True")
            break
        i += 1

xfind(testStr)