def compareTriplets(a, b):
    rating=[0,0]
    for i in range(len(a)):
        if a[i]>b[i]:
            rating[0]+=1
        elif a[i]<b[i]:
            rating[1]+=1
        else:
            pass
    return rating



    
    
a = list(map(int, input("A: ").rstrip().split()))

b = list(map(int, input("B: ").rstrip().split()))
print(compareTriplets(a, b))