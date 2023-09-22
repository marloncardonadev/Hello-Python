
### Functions ###

def my_function():
    print("Esto es una función")

my_function()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(45865, 75546)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    print(my_sum)

my_result = sum_two_values_with_return(10, 5)

print(my_result)
print(sum_two_values_with_return(10, 5))

def print_name(name, surname):
    print(f"{name} {surname}")

print_name("Marlon", "Cardona")

def print_name_with_default(name, surname, alias):
    print(f"{name} {surname} {alias}")

print_name_with_default("Marlon", "Cardona", "MarlonDev")

def print_texts(*texts):
    for text in texts:
        print(text.upper())

print_texts("Hola", "Python", "Marlon")
print_texts("Hola")
