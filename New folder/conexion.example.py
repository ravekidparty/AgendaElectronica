import pyodbc

def conectar():
    conexion = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=TU_SERVIDOR\\SQLEXPRESS;"
        "DATABASE=AgendaElectronica;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
    return conexion