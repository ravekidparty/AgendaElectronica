from conexion import conectar


def insertar_contacto(datos):
    conexion = conectar()
    if conexion is None:
        return False

    try:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO Contactos (
                Nombre, Apellido, FechaNacimiento, Direccion,
                Genero, EstadoCivil, Movil, Telefono, CorreoElectronico
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, datos)

        conexion.commit()
        return True

    except Exception as error:
        print("Error al insertar:", error)
        conexion.rollback()
        return False

    finally:
        conexion.close()


def listar_contactos():
    conexion = conectar()
    if conexion is None:
        return []

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Contactos ORDER BY IdContacto DESC")
        return cursor.fetchall()

    except Exception as error:
        print("Error al consultar:", error)
        return []

    finally:
        conexion.close()


def buscar_contactos(texto):
    conexion = conectar()
    if conexion is None:
        return []

    try:
        cursor = conexion.cursor()
        patron = f"%{texto}%"

        cursor.execute("""
            SELECT * FROM Contactos
            WHERE Nombre LIKE ?
            OR Apellido LIKE ?
            OR CorreoElectronico LIKE ?
        """, (patron, patron, patron))

        return cursor.fetchall()

    except Exception as error:
        print("Error al buscar:", error)
        return []

    finally:
        conexion.close()


def modificar_contacto(id_contacto, datos):
    conexion = conectar()
    if conexion is None:
        return False

    try:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE Contactos SET
                Nombre = ?,
                Apellido = ?,
                FechaNacimiento = ?,
                Direccion = ?,
                Genero = ?,
                EstadoCivil = ?,
                Movil = ?,
                Telefono = ?,
                CorreoElectronico = ?
            WHERE IdContacto = ?
        """, (*datos, id_contacto))

        if cursor.rowcount == 0:
            return False

        conexion.commit()
        return True

    except Exception as error:
        print("Error al modificar:", error)
        conexion.rollback()
        return False

    finally:
        conexion.close()


def eliminar_contacto(id_contacto):
    conexion = conectar()
    if conexion is None:
        return False

    try:
        cursor = conexion.cursor()
        cursor.execute(
            "DELETE FROM Contactos WHERE IdContacto = ?",
            (id_contacto,)
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()
        return True

    except Exception as error:
        print("Error al eliminar:", error)
        conexion.rollback()
        return False

    finally:
        conexion.close()