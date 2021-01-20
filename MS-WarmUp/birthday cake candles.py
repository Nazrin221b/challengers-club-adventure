def birthdayCakeCandles(candles):
    tallest=max(candles)
    count=0
    for i in candles:
        if i==tallest:
            count+=1
    return count





number=int(input('How many candles? '))
candles=list(map(int, input('lenghts: ').split()))
print(birthdayCakeCandles(candles))