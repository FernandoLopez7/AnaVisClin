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

        sql_ext_category = "SELECT idPaciente, tipoIdendificacion, numeroIdentificacion, nombre, apellido, ciudad, direccion, fechaNacimiento, alergia, sexo, grupoSanguineo FROM ext_paciente"
        df_ext_category = pd.read_sql(sql_ext_category, ses_db_stg)
        
        sql_sentence = """
            INSERT INTO dim_paciente (idPaciente, tipoIdendificacion, numeroIdentificacion, nombre, apellido, ciudad, direccion, fechaNacimiento, alergia, sexo, grupoSanguineo)
            SELECT ext_pa.idPaciente, ext_pa.tipoIdendificacion, ext_pa.numeroIdentificacion, ext_pa.nombre, ext_pa.apellido, ext_pa.ciudad, ext_pa.direccion, ext_pa.fechaNacimiento, ext_pa.alergia, ext_pa.sexo, ext_pa.grupoSanguineo
            FROM temporal AS ext_pa
            ON DUPLICATE KEY UPDATE
            tipoIdendificacion = ext_pa.tipoIdendificacion,
            numeroIdentificacion = ext_pa.numeroIdentificacion,
            nombre = ext_pa.nombre,
            apellido = ext_pa.apellido,
            ciudad = ext_pa.ciudad,
            direccion = ext_pa.direccion,
            fechaNacimiento = ext_pa.fechaNacimiento,
            alergia = ext_pa.alergia,
            sexo = ext_pa.sexo,
            grupoSanguineo = ext_pa.grupoSanguineo;
        """

        with ses_db_sor.begin() as conn:
            df_ext_category.to_sql('temporal', con=ses_db_sor, if_exists='replace', index=False)
            conn.exec_driver_sql(sql_sentence)
            conn.exec_driver_sql("DROP TABLE temporal")

    except:
        print("Error")
    finally:
        con_db_stg.cerrar()
        con_db_sor.cerrar()