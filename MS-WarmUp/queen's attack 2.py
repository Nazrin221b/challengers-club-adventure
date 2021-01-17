
def queensAttack(n, k, r_q, c_q, obstacles):
    no, s, w, e, nw , ne, sw,se = 0,0,0,0,0,0,0, 0 
    north=r_q
    while north<n:
        no+=1
        north+=1
    south=r_q
    while south>1:
        s+=1
        south-=1
    west=c_q
    while west>1:
        w+=1
        west-=1
    east=c_q
    while east <n:
        e+=1
        east+=1

    n_east1=r_q 
    n_east2=c_q
    while n_east1 < n and n_east2 < n:
        ne+=1
        n_east1+=1
        n_east2+=1

    n_west1=r_q
    n_west2=c_q
    while n_west1<n and n_west2>1:
        nw+=1
        n_west1+=1
        n_west2-=1

    s_west1=r_q
    s_west2=c_q 
    while s_west1>1 and s_west2>1:
        sw+=1
        s_west1-=1
        s_west2-=1

    s_east1=r_q
    s_east2=c_q
    while s_east1>1 and s_east2 <n:
        se+=1
        s_east1-=1
        s_east2+=1


    return s+no + w + e + ne+ nw + se+sw




# size of chess board & num of obstacles
n ,k = map (int, input().split())
r_q , c_q = map(int, input('position of queen: ').split())
obstacles=[]
for i in range(k):
    r_o , c_o =map (int, input('position of obstacle: ').split())
    obstacles.append((r_o, c_o))

print(queensAttack(n, k, r_q, c_q, obstacles))

