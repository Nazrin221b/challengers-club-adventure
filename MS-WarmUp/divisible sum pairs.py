def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        j = i+1
        while j < n:
            num=ar[i]+ar[j]
            if num % k==0:
                count += 1
            j += 1
    return count
            








len_arr=int(input('lenght: '))
arr=list(map(int, input('array: ').split()))
k=int(input('k: '))

print(divisibleSumPairs(len_arr, k, arr))