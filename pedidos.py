ARCHIVO_PEDIDOS = "pedidos.txt"

def pedir_cafe():
    cafes = {"1": "expreso", "2": "capuchino", "3": "latte", "4": "americano"}
    opcion = input("Elige un café que prefieras: ")

    if opcion in cafes:  # valida contra las keys
        cafe_elegido = cafes[opcion]
        print("Has pedido un " + cafe_elegido + ". Preparando tu café")
        # escritura en modo append con UTF-8
        with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(cafe_elegido + "\n")
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")