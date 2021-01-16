from math import sqrt

def squares(a, b):
    begin=int(sqrt(a))
    last=int(sqrt(b))
    count=last-begin
    if begin==sqrt(a):
        count+=1
    
    return count

for i in range(int(input('test cases: '))):
    a,b=map(int, input().split())
    print(squares(a,b))



