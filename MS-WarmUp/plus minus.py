def plusMinus(arr):
    neg=0
    pos=0
    zero=0
    for i in arr:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
        else:
            zero+=1
    print("{0:.6f}".format(pos/len(arr)))
    print("{0:.6f}".format(neg/len(arr)))
    print("{0:.6f}".format(zero/len(arr)))



    
arr = list(map(int, input("Array: ").rstrip().split()))
plusMinus(arr)