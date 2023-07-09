import pandas as pd
from Carga.conexion import ConexionMySQL
from Parametros.configLinux import host, user, password, database

def extraer(table):
    try:
        # Crear una instancia de la clase ConexionMySQL
        conexion_origen = ConexionMySQL(host, user, password, database)
        # Llamar al método conectar para establecer la conexión 
        engine = conexion_origen.conectar()

        # Consulta para extraer los datos
        consulta = "SELECT * FROM "+table

        # Utilizar el objeto de conexión de SQLAlchemy con pd.read_sql()
        datos = pd.read_sql(consulta, engine)
        print(datos.head())
        
        return datos

    except:
        print("Error")
    finally:
        # Cerrar la conexión
        conexion_origen.cerrar()