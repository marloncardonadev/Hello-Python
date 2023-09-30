
### File Handling ###

import os

# .txt file

txt_file = open("Intermediate/my_file.txt", "r+") # Leer y Escribir

txt_file.write("Mi nombre es Marlon\nMi apellido es Cardona\n35 anos\nY mi lenguaje preferido es Python")

print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
#print(txt_file.readlines())

for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque tambien me gusta C#")

txt_file.close()

#with open("Intermediate/my_file.txt", "a") as my_other_file:
  #  my_other_file.write("\nY Node")

#os.remove("Intermediate/my_file.txt")

# .json file

import json

json_file = open("Intermediate/my_file.json", "w+")

json_test = {
    "name":"Marlon",
    "surname":"Cardona", 
    "age":35,
    "languaje":["Python","JavaScript","C#"],
    "website":"https://moure.dev"}

json.dump(json_test, json_file, indent = 2)

json_file.close()

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file

import csv

csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "languaje", "website"])
csv_writer.writerow(["Marlon", "Cardona", 35, "Python", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file

#import xlsx

# .xml file

import xml