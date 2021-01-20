def pickingNumbers(a):
    maxim=0
    for i in a:
        dif_0=a.count(i)
        dif_1=a.count(i+1)
        total=dif_1+dif_0
        if total>maxim:
            maxim=total

        dif_2=a.count(i-1)
        total2=dif_0+dif_2
        if total2>maxim:
            maxim=total2
    return maxim

        









n = int(input('length: ').strip())

a = list(map(int, input('array: ').rstrip().split()))
print(pickingNumbers(a))