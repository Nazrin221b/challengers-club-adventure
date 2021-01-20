def hurdleRace(k, height):
    if k>max(height):
        return 0
    else:
        return max(height)-k



 

n = int(input('Number of hurdles: '))
k = int(input('Jump: '))
height = list(map(int, input().rstrip().split()))
print( hurdleRace(k, height))