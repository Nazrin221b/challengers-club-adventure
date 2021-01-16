


def diagonalDifference(arr):
    
    left=[]
    right=[]
    index_left=0  
    index_right=len(arr)-1
    for row in arr:
        left.append(row[index_left])
        right.append(row[index_right])
        index_left+=1
        index_right-=1
    diagonal_dif=abs(sum(left)-sum(right))
    return diagonal_dif

matrix=[]
m_m=int(input('mxm: '))
for i in range(m_m):
    matrix.append(list(map(int, input().split())))

print(diagonalDifference(matrix))