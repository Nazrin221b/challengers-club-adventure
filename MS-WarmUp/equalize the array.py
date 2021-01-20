def equalizeArray(arr):
    val=[]
    for i in arr:
        val.append(arr.count(i))
    return len(arr)-max(val)








arr = list(map(int, input().rstrip().split()))
print( equalizeArray(arr))