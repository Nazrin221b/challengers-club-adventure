def miniMaxSum(arr):
    a=min(arr)
    b=max(arr)
    minimum=[i for i in arr if i<b]
    maximum=[i for i in arr if i>a]
    if a==b:
        minimum=arr[0:4]
        maximum=arr[0:4]
    while len(minimum)<4:
      
        minimum.append(b)
    while len(maximum)<4:
        maximum.append(a)


    print(sum(minimum), sum(maximum))

        
        


arr = list(map(int, input().rstrip().split()))
print(miniMaxSum(arr))
