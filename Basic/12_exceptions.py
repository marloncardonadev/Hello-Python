
### Exception Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")


# try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally: # Opcional
    # Se ejecuta siembre
    print("La ejecución continúa")


# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    print("Se ha producido un TypeError")
except ValueError:
    print("Se ha producido un ValueError")


# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except Exception as error_exception:
    print("Error:", error_exception)