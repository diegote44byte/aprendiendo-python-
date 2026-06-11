import random 
import pandas as pd

def generar_contrasena():
    pd.read_csv("contrasenas.csv") # Para leer un archivo csv, aunque no es necesario para generar la contraseña, pero se puede usar para guardar las contraseñas generadas

    mayusculas = ['A','B','C','D','E','F','G']
    minusculas = ['a','b','c','d','e','f','g']
    simbolos = ['!','#','$','/']
    numeros = ['1','2','3','4','5','6','7','8','9','0']

    caracteres = mayusculas + minusculas + simbolos + numeros 
    contrasena = []
    
    for i in range(15):
        caracter_random = random.choice(caracteres)
        # El random choice para escoger de manera aleatoria
        contrasena.append(caracter_random)

    # Otra manera de ponerlo en string
    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print("Tu nueva contrasena es: " + contrasena)


if __name__ == "__main__":
    run()
