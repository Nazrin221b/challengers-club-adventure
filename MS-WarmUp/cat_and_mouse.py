queries=int(input('q: '))

def winner(x,y,z):
    if abs(x-z)<abs(y-z):
        return 'Cat A'
    elif abs(x-z)>abs(y-z):
        return 'Cat B'
    else:
        return 'Mouse C'

for i in range(queries):
    x,y,z=map(int, input().split())
    print(winner(x,y,z))