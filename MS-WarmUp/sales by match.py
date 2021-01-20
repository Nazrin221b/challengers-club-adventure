def sockMerchant(n, ar):
    id_num=[]
    count=0
    for i in ar:
        if i not in id_num:
            id_num.append(i)

    for item in id_num:
        count+=ar.count(item)//2

    return count







n = int(input("Total: "))

ar = list(map(int, input('Color id: ').rstrip().split()))
print(sockMerchant(n, ar))