# Important: this syntax will create a empty dictionary and not an empty set
a = {}
print(type(a))

# An empty set can be created by using the below syntax
b = set()
print(type(b))

b.add(34)
b.add(56)
b.add((4, 5, 7))
# b.add({4:5}) #cannot add list or dictionary to sets
print(b)