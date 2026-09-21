def heapify(arr,n,i):
    lar = i
    left = 2*i+1
    right = 2*i+2
    if left<n and arr[left]>arr[lar]:
        lar = left
    if right<n and arr[right]> arr[lar]:
        lar = right
    if lar!=i:
        arr[i],arr[lar] = arr[lar],arr[i]
        heapify(arr,n,lar)

def heap(arr):
    n = len(arr)
    for i in range(len(arr)//2,-1,-1):
        heapify(arr,n,i)
    for i in range(len(arr)-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)
    return arr

a = [1,5,4,2,7,8,4]
print(heap(a))