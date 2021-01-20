def migratoryBirds(arr):
    ids={}
    for i in arr:
        if i not in ids:
            ids[i]=1
        else:
            ids[i]+=1
    maximum= sorted(ids.keys(), key=lambda k: ids[k], reverse=True)
    max_type=ids[maximum[0]]
    equals=[]
    for i in maximum:
        if ids[i]==max_type:
            equals.append(i)
    return min(equals)



            





arr_count= int(input("Number of birds: "))

arr = list(map(int, input("Types: ").rstrip().split()))
print(migratoryBirds(arr))