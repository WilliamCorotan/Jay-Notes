#List
#   [1,1,2,3,4,4]
#   it allows duplicate
#   is ordered
#   is mutable
#       mutable is the ability to change, add or remove values

#Tuple
#   (1,1,2,3,4,5)
#   it allows duplicate
#   is ordered
#   is immutable
#       immutable cannot change, add or remove values

#Set 
#   {1,1,2,3,4,4}
#   {"catcher in the rye", "john doe", "jane doe", "2024-12-25"}
#   it doesnt allow duplicates
#   is unordered
#   is mutable
#       mutable is the ability to change, add or remove values

#Dictionary
# are json objects
# {"title":"lord of the flies", "author":"john doe", "publisher":"jane doe", "publication_date":"2024-12-25"}
# contains a key valur pair separated with a colon (:)
#   is ordered (python 3.7 and above)
#   is mutable
#       mutable is the ability to change, add or remove values

_list = [1,1,2,3,4,5]
_tuple = (1,1,2,3,4,5)

_set = set(_tuple) 

# print(_tuple)
# print(_set)

another_set = set(_list)

# print(another_set)

book = {"title":"lord of the flies", "author":"john doe", "publisher":"jane doe", "publication_date":"2024-12-25"}

# book.items()
# [
#     ('title', 'lord of the flies'), 
#     ('author', 'john doe'), 
#     ('publisher', 'jane doe'), 
#     ('publication_date', '2024-12-25')
# ]

print(book.items())
for key, value  in book.items():
    print(key, value)