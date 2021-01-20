def getMoneySpent(keyboards, drives, b):
    count = []
    i=0
    while i<len(keyboards):
        j = 0
        while j < len(drives):
            sum_OF=keyboards[i]+drives[j]
            count.append((sum_OF))
            j += 1
        i+=1
    A=[i for i in count if i<=b]
    if len(A)<1:
        return -1
    else:
        return max(A)

          







b=int(input('Budget: '))
n, m =map(int, input('Number of models: ').split())
k=list(map(int, input('keyboards: ').split()))
d=list(map(int, input('drivers: ').split()))

print(getMoneySpent(k, d, b))