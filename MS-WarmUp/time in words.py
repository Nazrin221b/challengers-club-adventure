#h , m =map(int , input().split())
h=7
m=00
def convert(h,m):
    words=["o' clock", "one", "two", "three", "four","five", "six","seven", "eight", "nine","ten", "eleven","twelve","thirteen","fourteen","quarter","sixteen","seventeen","eighteen","nineteen","twenty","twenty one", "twenty two", "twenty three", "twenty four", "twenty five","twenty six","twenty seven","twenty eight", "twenty nine", 'half']
    if m==00:
        minutes=''
        add=''
        print(words[h], words[m])
    else:
        if m>30:
            m=60-m
            add='to '
            h=h+1
        elif m<31:
            add='past '
        if m==1:
            minutes='minute'
        elif m==15:
            minutes=''
        elif m==30:
            minutes=''

        else:
            minutes='minutes'
 
        print(words[m], minutes, add, words[h])


    convert(h,m)
