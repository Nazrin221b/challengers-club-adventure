def countApplesAndOranges(s, t, a, b, apples, oranges):
    fruit=[0,0]

    for d in apples:
        d+=a
        if d>=s and d<=t:
            fruit[0]+=1
    for i in oranges:
        i+=b
        if i>= s and i<=t:
            fruit[1]+=1

    print(fruit[0])
    print(fruit[1])




    




s, t =map(int, input('Range of house: ').split())
a,b= map(int, input('Positions of apple and orange: ').split())
apples = list(map(int, input('distance: ').split()))
oranges = list(map(int, input('distance: ').split()))

print(countApplesAndOranges(s, t, a, b, apples, oranges))
