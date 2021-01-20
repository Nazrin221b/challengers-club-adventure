def beautifulDays(i, j, k):
    days=list(range(i, j+1))
    A=[]
    for day in days:
        day_re=int(str(day)[::-1])
        if (day_re-day)%k==0:
            A.append(day)
    return len(A)










i=int(input('start: '))
j=int(input('end: '))
k=int(input('rate: '))
print(beautifulDays(i, j, k))