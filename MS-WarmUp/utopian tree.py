def utopianTree(n):
    l=1
    i=0
    while i<n:
        i+=1
        if i%2==1:
            l*=2
        else:
            l+=1
            print(l)
    return l 





t=int(input('Test cases: '))
for  i in range(t):
    n=int(input('cycles: '))
    print(utopianTree(n))
