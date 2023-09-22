
### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 3
else: # Es opcional
    print("Mi condición es mayor o igual que 10")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break
    print(my_condition)

print("la ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1.88, "Marlon", "Cardona", "Marlon")

for element in my_tuple:
    print(element)

my_set = {"Marlon", "Cardona", 35}

for element in my_set:
    print(element)

my_dict = {"Nombre":"Marlon", "Apellido":"Cardona", "Edad":35, 1:"Python"}

for element in my_dict.values():
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")


for element in my_dict.values():
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")