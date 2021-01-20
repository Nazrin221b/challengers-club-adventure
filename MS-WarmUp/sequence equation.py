def permutationEquation(p):
    y=[]
    for i in range(1, len(p)+1):
        v=p.index(i)+1
        y.append(p.index(v)+1)
    print(y)
    
p=list(map(int, input().split()))
permutationEquation(p)