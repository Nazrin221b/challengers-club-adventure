def gradingStudents(grades):
    def rounding(score):
        first_digit=(score)//10
        second_digit=(score)-first_digit*10
        if second_digit<5:
            second_digit=5
        else:
            second_digit=0
            first_digit+=1
        new=first_digit*10+second_digit
        return new
    final=[]
    for i in grades:
        if i>37:
            if rounding(i)-i<3:
                final.append(rounding(i))
            else:
                final.append(i)
        else:
            final.append(i)

    
    return final




grades=[]
num=int(input('How many grades does he have ? '))
for i in range(num):
    grades.append(int(input('Score: ')))
print(gradingStudents(grades))

