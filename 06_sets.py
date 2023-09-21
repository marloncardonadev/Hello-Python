
### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Marlon", "Cardona", 35}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("MarlonDev")

print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("MarlonDev") # Un set no admite repetidos

print(my_other_set)

print("Marlon" in my_other_set)
print("Orlando" in my_other_set)

my_other_set.remove("Marlon")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Marlon", "Cardona", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0]) # No es lo mas recomendado cambiar el set a list

my_other_set = {"C#", "Javascript", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.difference(my_set))
