import pandas as pd
from Carga.conexion import ConexionMySQL
from Parametros.configstg import host, user, password, database

def persistir(datos, tabla):
    try:
        # Crear una instancia de la clase ConexionMySQL 
        conexion_destino = ConexionMySQL(host, user, password, database)
        # Llamar al método conectar para establecer la conexión
        connection = conexion_destino.conectar()
        # Insertar los datos en la tabla 'ext_actor'
        datos.to_sql('ext_'+tabla, connection, if_exists='replace', index=False)
        print("Datos insertados en "+tabla+" de manera exitosa")

    except:
        print("Error")
    finally:
        conexion_destino.cerrar()