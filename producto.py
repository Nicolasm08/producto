diccionario_de_contactos = {}

while True:
    print("Menu:")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Actualizar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = input("Digite una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono del contacto: ")
        diccionario_de_contactos[nombre] = telefono
        print(f"Contacto '{nombre}' agregado correctamente.")

    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto que desea buscar: ")
        telefono = diccionario_de_contactos.get(nombre, "No se encontró el contacto")
        print(f"Teléfono de '{nombre}': {telefono}")

    elif opcion == "3":
        nombre = input("Ingrese el nombre del contacto que desea actualizar: ")
        if nombre in diccionario_de_contactos:
            nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
            diccionario_de_contactos[nombre] = nuevo_telefono
            print(f"Teléfono de '{nombre}' actualizado correctamente.")
        else:
            print(f"'{nombre}' no se encontró en la lista de contactos.")

    elif opcion == "4":
        nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
        if nombre in diccionario_de_contactos:
            del diccionario_de_contactos[nombre]
            print(f"Contacto '{nombre}' eliminado correctamente.")
        else:
            print(f"'{nombre}' no se encontró en la lista de contactos.")

    elif opcion == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, elija una opción válida del menú.")