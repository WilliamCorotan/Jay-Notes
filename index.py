i = 1
while i <= 10:
    # print(i, end = " ")
    i = i + 1

for i in range(1, 10, 3):
    # print(i, end = " ")
    x = 1


# name = "william"
# address = "Philippines"

# message = "Hi! I'm " + name + ", I'm from the " + address

# f_message = f"Hi! I'm {name}, I'm from the {address}"

# print(message)
# print(f_message)

try:
    uinput = int(input("enter a number: "))
    print(type(uinput))
except:
    print("please enter a valid number")