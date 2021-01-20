def simpleArraySum(ar):
    sum=0
    for i in ar:
        sum+=i
    return sum

# or simple
def simpleArraySum_func(ar):
    return sum(ar)


ar_count = int(input('length: '))

ar = list(map(int, input('array: ').rstrip().split()))
print(simpleArraySum(ar))