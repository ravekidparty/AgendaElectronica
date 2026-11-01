from conexion import conectar

conexion = conectar()

if conexion:
    print("¡Conexión exitosa con SQL Server!")
    conexion.close()
else:
    print("No se pudo establecer la conexión.")
