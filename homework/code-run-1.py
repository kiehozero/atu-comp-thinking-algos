# notepad for code runner assessments

def in_trouble(cat_talking, time):
    if cat_talking == True:
        if time < 6:
            return True
        elif time > 21:
            return True
        else:
            return False
    else:
        return False

print(in_trouble(False, 23))