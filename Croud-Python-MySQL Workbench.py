import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database=""
)
cursor = conexion.cursor()

#Crear tabla si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS elementos
                  (id INT AUTO_INCREMENT PRIMARY KEY,
                   elemento VARCHAR(255))''')

def mostrar_menu():
    print("1. Crear")
    print("2. Leer")
    print("3. Actualizar")
    print("4. Eliminar")
    print("5. Salir")

def crear_elemento():
    elemento = input("Ingrese el elemento que desea crear: ")
    cursor.execute("INSERT INTO elementos (elemento) VALUES (%s)", (elemento,))
    conexion.commit()
    print("Elemento creado exitosamente")

def leer_elementos():
    cursor.execute("SELECT * FROM elementos")
    elementos = cursor.fetchall()
    if len(elementos) == 0:
        print("No hay elementos para mostrar")
    else:
        print("Elementos:")
        for elemento in elementos:
            print(elemento)

def actualizar_elemento():
    cursor.execute("SELECT * FROM elementos")
    elementos = cursor.fetchall()
    if len(elementos) == 0:
        print("No hay elementos para actualizar")
    else:
        indice = int(input("Ingrese el ID del elemento a actualizar: "))
        cursor.execute("SELECT * FROM elementos WHERE id=%s", (indice,))
        elemento = cursor.fetchone()
        if not elemento:
            print("ID inválido")
        else:
            nuevo_elemento = input("Ingrese la modificacion: ")
            cursor.execute("UPDATE elementos SET elemento=%s WHERE id=%s", (nuevo_elemento, indice))
            conexion.commit()
            print("Elemento actualizado exitosamente")

def eliminar_elemento():
    cursor.execute("SELECT * FROM elementos")
    elementos = cursor.fetchall()
    if len(elementos) == 0:
        print("No hay elementos para eliminar")
    else:
        indice = int(input("Ingrese el ID del elemento a eliminar: "))
        cursor.execute("SELECT * FROM elementos WHERE id=%s", (indice,))
        elemento = cursor.fetchone()
        if not elemento:
            print("ID inválido")
        else:
            cursor.execute("DELETE FROM elementos WHERE id=%s", (indice,))
            conexion.commit()
            print("Elemento eliminado exitosamente")

while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_elemento()
    elif opcion == "2":
        leer_elementos()
    elif opcion == "3":
        actualizar_elemento()
    elif opcion == "4":
        eliminar_elemento()
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

# Cerrar la conexión con la base de datos
conexion.close()
