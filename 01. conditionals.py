age = 18

# passing 70 
# max 100
# if student's grade >= 70 and <= 100, print great job, 
# if student's grade < 70 and >= 0, print dont give up, 
# if student's grade > 100, print error, exceeding the max grade
# else print not possible

# and or
# or - a or b = a or b is true, this return true, both return false, return false
# and - strictly a and b, both should be true to return true, 

# AND operator
# true and true = true
# true and false = false
# false and true = false
# false and false = false

# OR operator
# true and true = true
# true and false = true
# false and true = true
# false and false = false

#it executes the first true statement
grade = -1
if(grade >= 70 and grade <= 100): 
    print('great job')
elif(grade < 70 and grade >= 0 ): 
    print('dont give up')
elif(grade > 100): 
    print('error, exceeding the max grade')
else:
    print('not possible')