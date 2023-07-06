import pandas as pd
from Carga.conexion import ConexionMySQL
from Parametros.configstg import host, user, password, database
from Parametros.configsor import hosts, users, passwords, databases

def trans():
    try:
        # Conexión a la base de datos de origen (stg)
        con_db_stg = ConexionMySQL(host, user, password, database)
        ses_db_stg = con_db_stg.conectar()
        
        # Conexión a la base de datos de destino (sor)
        con_db_sor = ConexionMySQL(hosts, users, passwords, databases)
        ses_db_sor = con_db_sor.conectar()

        # # Consulta para extraer los datos
        # consulta = "SELECT * FROM ext_codigocie10"

        # # Utilizar el objeto de conexión de SQLAlchemy con pd.read_sql()
        # datos = pd.read_sql(consulta, ses_db_stg)
        # print(datos.head())

        sql_ext_category = "SELECT idPaciente, tipoIdendificacion, numeroIdentificacion, nombre, apellido, ciudad, direccion, fechaNacimiento, alergia, sexo, grupoSanguineo FROM ext_paciente"
        df_ext_category = pd.read_sql(sql_ext_category, ses_db_stg)
        
        sql_sentence = "MERGE INTO public.dim_categoria AS car_ca USING (SELECT category_id, nombre FROM public.temporal_category) AS ext_ca ON car_ca.cat_bus_id = ext_ca.category_id WHEN MATCHED THEN UPDATE SET nombre = ext_ca.nombre WHEN NOT MATCHED THEN INSERT (cat_bus_id, nombre) VALUES (ext_ca.category_id, ext_ca.nombre)"

        with ses_db_sor.begin() as conn:
            df_ext_category.to_sql('temporal', con=ses_db_sor, if_exists='replace', index=False)
            conn.execute(sql_sentence)
            conn.execute("DROP TABLE temporal")

    except:
        print("Error")
    finally:
        con_db_stg.cerrar()
        con_db_sor.cerrar()