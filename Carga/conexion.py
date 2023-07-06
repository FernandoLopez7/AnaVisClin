from sqlalchemy import create_engine

class ConexionMySQL:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.engine = None

    def conectar(self):
        try:
            # Crear la cadena de conexión utilizando SQLAlchemy
            db_uri = f"mysql://{self.user}:{self.password}@{self.host}/{self.database}"
            self.engine = create_engine(db_uri)
            print("Conexión exitosa a la base de datos MySQL")
            return self.engine
        except Exception as error:
            print(f"Error al conectar a la base de datos: {error}")
            return None

    def cerrar(self):
        if self.engine:
            self.engine.dispose()
            print("Conexión cerrada")