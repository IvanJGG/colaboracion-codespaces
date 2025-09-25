# saludo.py
def pedir_nombre():
    while True:
        nombre = input("Ingresa tu nombre: ").strip()
        if nombre:
            return nombre
        print("⚠️ Por favor ingresa un nombre válido.")

def main():
    nombre = pedir_nombre()
    print(f"¡Hola {nombre}, bienvenido al repositorio colaborativo!")

if __name__ == "__main__":
    main()
