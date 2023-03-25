''' 2. Write a method which produces a new string which is the merge of both strings. For example the strings
“dmnc” and “oii” would merge to become “dominic”. The basic step is to combine the current character from
the first and second strings together in that order, so first that would be 'd' and 'o', then 'm' and 'i'.
The second string will always be shorter and when we are finished with it the remainder of the first string
will be the last part of our new string. '''

# my solution

testStr1 = "dlhfnyooain"
testStr2 = "eteukhmspe"

def merge(str1,str2):
    merged = ""
    i = 0
    listed = [len(str1),len(str2)]
    minlen = min(listed)

    while minlen > i:
        merged = merged + str1[i] + str2[i]
        i += 1
    merged = merged + str1[i]

    print(merged)

merge(testStr1,testStr2)
