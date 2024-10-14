# intro to object orientated programming (oop)
# classes have properties, methods
# properties are nouns
# methods are verbs
# variable in a class is called a property
# function in a class is called a method
# self is a reserved keyword referencing to the current class
# dot (.) access operator 
class human:
    name = ""
    role = ""
    age = ""
    x = 0
    y = 0

    # this is executed on creation of the object
    def __init__(self, name, role):
        self.name = name
        self.role = role
        print('i am initialized')
    # the first argument is the reference to the object itself
    def move_right(self):
        self.x = self.x+1
        print(self.x)

    # you can define a default value for a argument by using the asignment operator
    def greet(self, greeting, another = ""):
        print(f"{greeting}. {another}")

x = human("lesley", "healer")
x.move_right() # 1
x.move_right() # 2
x.move_right() # 3
x.move_right() # 4
x.move_right() # 5
x.move_right() # 6
x.move_right() # 7
x.greet("hello there")

print(x.name)

x.name = "becca"

print(x.name)