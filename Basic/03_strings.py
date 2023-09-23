
### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulacion"
print(my_tab_string)

my_scape_string = "\tEste es un String \n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Marlon", "Cardona", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
languaje = "python"
a, b, c, d, e, f = languaje
print(a)
print(e)

# Division

languaje_slice = languaje[1:3]
print(languaje_slice)

languaje_slice = languaje[1:]
print(languaje_slice)

languaje_slice = languaje[-2]
print(languaje_slice)

languaje_slice = languaje[0:6:2]
print(languaje_slice)

# Reverse

languaje_reverse = languaje[::-1]
print(languaje_reverse)

# Funciones

print(languaje.capitalize())
print(languaje.upper())
print(languaje.count("t"))
print(languaje.isnumeric())
print("1".isnumeric())
print(languaje.lower())
print(languaje.upper().isupper())
print(languaje.startswith("py"))
