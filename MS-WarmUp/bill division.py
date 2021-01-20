def bonAppetit(bill, k, b):
    total_bill=(sum(bill))-bill[k]
    total_bill/=2

    if total_bill==b:
        return "Bon Appetit"
    else:
        return int(bill[k]/2)








n = int(input('item: '))

k = int(input('Anna did not eat: '))

bill = list(map(int, input().rstrip().split()))

b = int(input('Bill: '))
print(bonAppetit(bill, k, b))