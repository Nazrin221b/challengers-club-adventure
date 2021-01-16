x1, v1=map(int, input("First : ").split())
x2, v2=map(int, input("Second : ").split())

def kangaroo (x1,v1,x2,v2):
   
    if ((x1 < x2) and (v1 < v2)) or ((x1>x2) and (v1 > v2)): 
        return 'NO'
    elif ((x1 !=x2) and (v1==v2)) or ((x1==x2) and (v1!=v2)):
        return "NO"
    elif abs(x2-x1)% abs(v1-v2)==0:
        return 'YES'
    else:
        return 'NO'
        

print(kangaroo(x1,v1,x2,v2))


# firstly , if one's both parameters are small   from  other , there is no way to catch up
# then , if speeds or initial values are same , still one can not catch up other
# the last thing,  we have equation to solve  x1+ m(distance) * v1 = x2+ m*v2