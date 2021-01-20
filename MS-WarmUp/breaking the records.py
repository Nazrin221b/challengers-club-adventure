def breakingRecords(scores):
    l=len(scores)
    best=scores[0]
    worst=scores[0]
    record=[0,0]
    for  i in range(l):
        if scores[i]>best:
            record[0]+=1
            best=scores[i]
        if scores[i]<worst:
            record[1]+=1
            worst=scores[i]

    return record


    
      




n=int(input('total game: '))
scores=list(map(int , input('score: ').split()))
print(breakingRecords(scores))