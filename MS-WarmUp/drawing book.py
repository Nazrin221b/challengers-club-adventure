def pageCount(n, p):
    left=(n-p)//2
    right=p//2
    if left>=right:
        return right

    else:
        if n-p==1 and n%2==0:
            return 1
        else:
           return left







n=int(input('lenght of book: '))
p=int(input('page: '))