def findDigits(n):
    count=0
    for i in str(n):
        if i!='0' and  int(n)%int(i)==0:
            count+=1
        else:
            pass
    return count





n=int(input('n: '))
print( findDigits(n))