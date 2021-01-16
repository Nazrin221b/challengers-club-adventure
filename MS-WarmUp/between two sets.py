a=[2,3,6 ]
b=[42,84]
def getTotalX(a, b):
    def gcd(x, y):
        while(y):
            x, y = y, x % y
        return x

    def lcm(x, y):
        lcm = (x*y)//gcd(x,y)
        return lcm

    def find_lcm(num1, num2): 
        if(num1>num2): 
            num = num1 
            den = num2 
        else: 
            num = num2 
            den = num1 
        rem = num % den 
        while(rem != 0): 
            num = den 
            den = rem 
            rem = num % den 
        g = den 
        lcm = int(int(num1 * num2)/int(g)) 
        return lcm 

    if len(a)>2:
        a1 = a[0] 
        a2 = a[1] 
        first = find_lcm(a1,a2) 
  
        for i in range(2, len(a)): 
            first = find_lcm(first, a[i]) 
    else:

        first=lcm(a[0], a[-1])

    if len(b)>2:
        b1=b[0] 
        b2=b[1] 
        last=gcd(b1,b2) 
        for i in range(2,len(b)): 
            last=gcd(last,b[i])
    else:
        last=gcd(b[0], b[-1]) 

    l=[]
    while first<last+1:
        if last%first==0 and first%a[-1]==0:
            l.append(first)
        first+=1
    print (l, len(l))
      

a=[2,3,6 ]
b=[42,84]
getTotalX(a, b)