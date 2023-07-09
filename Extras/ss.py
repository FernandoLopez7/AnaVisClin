import MySQLdb

def obtener_tablas():
    try:
        host = '192.168.0.198'
        user = 'Gabriel'
        password = 'gabely1234'
        database = 'AnaVisClin'

        # Establecer la conexión a la base de datos 
        connection = MySQLdb.connect(
            host=host,
            user=user,
            passwd=password,
            db=database
        )

        # Obtener un cursor
        cursor = connection.cursor()

        # Ejecutar la consulta para obtener las tablas
        cursor.execute("SHOW TABLES")

        # Recuperar los nombres de las tablas
        tables = cursor.fetchall()

        # Imprimir las tablas
        print("Tablas en la base de datos:")
        for table in tables:
            print(table[0])

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error: {e}")

obtener_tablas()
