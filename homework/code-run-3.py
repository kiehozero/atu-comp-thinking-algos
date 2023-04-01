# notepad for code runner assessments

def party(tea, candy):
    if tea < 5:
        return "bad"
    elif candy < 5:
        return "bad"
    elif (tea * 2) < candy:
        return "great"
    elif (candy * 2) < tea:
        return "great"
    elif tea > 5:
        return "good"
    elif candy > 5:
        return "good"
    
print(party(6,8))
print(party(3,8))
print(party(20,6))
print(party(10,4))