def linear(arra,target):
    for i in range(len(arra)):
        if(arra[i]==target):
            return i
        else:
            return 0
arra = [1,2,3,4,5]
target = 2
index = linear(arra,target)
print(index)
