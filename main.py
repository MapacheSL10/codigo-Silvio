import os, time

Lista = [["lámpara", 5500, 0.90, 0], ["estuche", 2000, 1, 0], ["alcancía", 3000, 0.90, 0]]

def menu():
    os.system("cls")
    print("Bienvenido a la bodega\n")
    print("[0] salir")
    print("[1] lámpara")
    print("[2] estuche")
    print("[3] alcancía")
    try:
        seleccion = int(input("seleccione una opcion: "))
        match(seleccion):
            case 0:
                print("hasta pronto:)")
                return
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
    except Exception as e:
        print(f"[!] ocurrió un error: {e} ")
        time.sleep(3)
        menu()

if __name__ == "__main__":
    print(Lista[0])