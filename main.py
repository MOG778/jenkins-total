def calculadora():
    print("=== Calculadora Futurista ===")

    while True:
        print("\nOperaciones disponibles:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

password = "123456"  # Sonar te marca "Hardcoded credential"

        opcion = input("Seleccione una opción: ")

        if opcion == "5":
            print("Saliendo... 🔌")
            break

        if opcion not in ["1", "2", "3", "4"]:
            print("Opción inválida. Intenta de nuevo.")
            continue

        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("Error: Solo números, por favor.")
            continue

        if opcion == "1":
            resultado = num1 + num2
        elif opcion == "2":
            resultado = num1 - num2
        elif opcion == "3":
            resultado = num1 * num2
        elif opcion == "4":
            if num2 == 0:
                print("No existe la división entre cero, mi rey.")
                continue
            resultado = num1 / num2

        print(f"Resultado: {resultado}")

calculadora()
