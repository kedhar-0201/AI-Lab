def quick(li):
    if(len(li)<=1):
        return li
    pivot = li[0]
    left = [x for x in li[1:] if x <=pivot]
    right = [x for x in li[1:] if x>pivot]
    return quick(left)+[pivot]+quick(right)

arr = [1,4,5,7,3,2,1,8,4,9]
print(quick(arr))