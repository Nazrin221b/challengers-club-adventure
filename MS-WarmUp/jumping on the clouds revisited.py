def jumpingOnClouds(c, k):
    energy=100
    point=0
    n=len(c)
    while True:
        point=(point+k)%n
        if c[point]==1:
            energy-=3
        else:
            energy-=1
        
        if point==0:
            break
        print(point , energy)
    return energy





n=int(input("length: "))
k=int(input("range: "))
c = list(map(int, input('array: ').rstrip().split()))
print(jumpingOnClouds(c, k))