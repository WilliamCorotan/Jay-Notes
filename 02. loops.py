#Loops 
# Do some tasks for a given limit or a given condition

i = 1
while i <= 10: # false
    print("i: ", i)
    i = i + 1 # important to increment the value, infinite loop
    print("updated i: ", i)
    print("------------------")
print('hi, im i: ', i)

# range(start, end, step)
# for (let x = 0; x < 2; x++)
for number in range(1, 10, 3):
    print(i, end = " ")

# find the sum of the first 100 numbers starting from 1

# variable starting_point = 1, total = 0
# condition starting_point <= 100