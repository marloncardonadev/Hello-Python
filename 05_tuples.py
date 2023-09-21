
### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.88, "Marlon", "Cardona", "Marlon")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Marlon"))
print(my_tuple.index("Cardona"))
print(my_tuple.index("Marlon"))

# my_tuple[5] = 1.90 'tuple' object does not support item assignament
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "MarlonDev"
my_tuple.insert(1, "Verde")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))