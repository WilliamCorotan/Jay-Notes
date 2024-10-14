#DRY - dont repeat yourself

# check if the day is a weekend
user_input = input('What day is it: ').lower()

print('the input is :', user_input)
# parameter or argument 

#scoping
#function definition
def check_day(input):
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    weekends = ['satruday', 'sunday']

    message = 'Error! Your input is not within the days of a week.'
    for day in weekdays:
        if(input == day): # 1 = 1  math
            message = 'today is a weekday!'
    for day in weekends:
        if(input == day):
            message = 'today is a weekend!'
    
    print(message)

try:
    check_day(user_input)
    print('im working well')
except: # this is executed when the program encounters an error
    print('i caused a bug')
finally: # this will always be executed
    print('i will always be executed')





































    print 