

# this is bad way that I got runtime error
def saveThePrisoner_r(n, m, s):
    i=0
    table=[]  
    while i<m:
        table.append(s)
        if s==n:
            s=1
        else:
            s+=1
        i+=1
    return table[-1] , table
        

# after math operations I found :
def saveThePrisoner(n, m, s):
    rev= s+m-1
    if rev %n!=0:
        return rev %n
    else:
        return n




n=int(input('Prisoners: '))
m=int(input('Sweets: '))
s=int(input('chair: '))
print(saveThePrisoner(n, m, s))