# Write an algorithm that checks whether an element occurs in an array, assume unsorted

def linear_search(arr,target,index):
    # base cases
    if arr[index] == target:
        return True
    elif index == 0:
        return False
    # recursion, works backwards from end of range
    else:
        return linear_search(arr,target,index-1)
    
def search(arr,target):
    return linear_search(arr,target,len(arr)-1)

# stop when I have checked all indexes or find element
# make progress by moving index

print(search([1,2,3,4],4))
print(search([1,2,3,4],5))
print(search([1,2,3,4],1))