def prof(condition, students):
    pos=0
    for i in students:
        if i>0:
            pass
        else:
            pos+=1
    if pos<condition:
        return("YES")
    else:
        return ("NO")


for i in range(int(input('Test Case: '))):
    num=int(input('num of students: ')) 
    k=int(input('at least: '))
    students=list(map(int, input().split()))
    print('----------')
    print(prof(k,students))
    print('----------')

    
