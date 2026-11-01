import pyodbc

def conectar():
    try:
        conexion = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=Francheska\\SQLEXPRESS;"
            "DATABASE=AgendaElectronica;"
            "Trusted_Connection=yes;"
            "TrustServerCertificate=yes;"
        )
        return conexion

    except pyodbc.Error as error:
        print("Error al conectar con SQL Server:", error)
        return None



if __name__ == "__main__":
    conexion = conectar()

    if conexion:
        conexion.close()
        print("Conexión cerrada correctamente.")

    input("Presiona ENTER para salir...")