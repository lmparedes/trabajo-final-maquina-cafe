ARCHIVO_PEDIDOS = "pedidos.txt"

def ver_historial():
    try:
        print("\nHistorial de pedidos")
        with open(ARCHIVO_PEDIDOS, "r", encoding="utf-8") as archivo:
            pedidos = archivo.readlines()

        if pedidos:
            for i, pedido in enumerate(pedidos, start=1):
                print(str(i) + ". " + pedido.strip())
        else:
            print("Aún no hay ningún pedido")

    except FileNotFoundError:
        print("\nTodavía no existe un historial de pedidos")