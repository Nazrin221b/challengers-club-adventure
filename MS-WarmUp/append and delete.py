def appendAndDelete(s, t, k):
    i=0
    same=0
    try:
        while i< len(s):
            if s[i]==t[i]:
                same+=1
            else: 
                break
            i+=1
    except :
        pass

    answer=len(s)-same+len(t)-same
    if answer<=k:
        return 'Yes'
    else:
        return 'No'






s = input('the initial string: ')

t = input('the desired string: ')

k = int(input('Num of operations: '))
print(appendAndDelete(s, t, k))