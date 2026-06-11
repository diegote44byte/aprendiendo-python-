def es_primo(numero):
    contador = 0 

    for i in range(1,numero + 1):
        if i == 1 or i == numero:
            continue
        # Quiere decir : que si i es igual a 1 o igual a numero nos saltamos la linea 
        if numero % 2 == 0:
        # Quiere decir : Si numero tiene resto 0 
            contador+= 1
    if contador == 0:
        return True 
    else:
        return False



def run():
    numero = int(input("Escribe un numero: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == '__main__':
    run()