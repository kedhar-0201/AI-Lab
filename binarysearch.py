def binary(arr,tar):
    low = 0
    high = len(arr)-1
    while(low<=high):
        mid = (low+high)//2
        if(arr[mid]==tar):
            return mid
        elif(arr[mid]<target):
            left = mid+1
        else:
            right = mid-1
    return 0

arr = [1,2,3,4,5,6]
tar = 3
index = binary(arr,tar)
print(index)
