import pandas as pd
from Carga.conexion import ConexionMySQL
from Parametros.configstg import host, user, password, database
from Parametros.configsor import hosts, users, passwords, databases
from Parametros.merge import sql_sentence, temporal
def trans():
    try:
        # Conexión a la base de datos de origen (stg) 
        con_db_stg = ConexionMySQL(host, user, password, database)
        ses_db_stg = con_db_stg.conectar()
        
        # Conexión a la base de datos de destino (sor)
        con_db_sor = ConexionMySQL(hosts, users, passwords, databases)
        ses_db_sor = con_db_sor.conectar()

        for transform, temp in zip(sql_sentence, temporal):
            sql_ext_category = temp
            df_ext_category = pd.read_sql(sql_ext_category, ses_db_stg)
            print(temp)
            sentences = transform
            with ses_db_sor.begin() as conn:
                df_ext_category.to_sql('temporal', con=ses_db_sor, if_exists='replace', index=False)
                conn.exec_driver_sql(sentences)
                conn.exec_driver_sql("DROP TABLE temporal")

    except:
        print("Error")
    finally:
        con_db_stg.cerrar()
        con_db_sor.cerrar()