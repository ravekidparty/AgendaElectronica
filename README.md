# Agenda Electrónica

Sistema de gestión de contactos desarrollado en **Python**, utilizando **Tkinter** para la interfaz gráfica y **SQL Server** como sistema de gestión de bases de datos.

## Descripción

La Agenda Electrónica permite registrar y administrar información personal de contactos mediante una interfaz gráfica sencilla e intuitiva. El sistema facilita la organización de los datos y permite realizar operaciones de creación, consulta, actualización y eliminación (CRUD).

## Funcionalidades

- **Registrar contactos:** guardar nuevos contactos en la base de datos.
- **Consultar contactos:** visualizar los contactos registrados.
- **Buscar contactos:** localizar registros por nombre, apellido o correo electrónico.
- **Modificar contactos:** actualizar la información de un contacto existente.
- **Eliminar contactos:** borrar contactos registrados.
- **Limpiar formulario:** restablecer los campos para ingresar nuevos datos.

## Información de los contactos

El sistema permite almacenar los siguientes datos:

- Nombre
- Apellido
- Fecha de nacimiento
- Dirección
- Género
- Estado civil
- Móvil
- Teléfono
- Correo electrónico

## Tecnologías utilizadas

| Tecnología | Función |
|---|---|
| Python | Lenguaje de programación |
| Tkinter | Desarrollo de la interfaz gráfica |
| SQL Server Express | Gestión de la base de datos |
| pyodbc | Conexión entre Python y SQL Server |
| Visual Studio Code | Entorno de desarrollo |

## Estructura del proyecto

```text
AgendaElectronica/
│
├── main.py                 # Interfaz gráfica principal
├── conexion.py             # Conexión con SQL Server (archivo local)
├── conexion.example.py     # Plantilla de configuración
├── contactos.py            # Operaciones CRUD
├── prueba_conexion.py      # Prueba de conexión
├── .gitignore              # Archivos excluidos de Git
└── README.md               # Documentación del proyecto
```

## Requisitos

- Python 3 instalado.
- SQL Server Express.
- SQL Server Management Studio (SSMS).
- Microsoft ODBC Driver 17 for SQL Server.
- Biblioteca `pyodbc`.

## Instalación

**1. Clonar el repositorio**

```bash
git clone https://github.com/ravekidparty/AgendaElectronica
```

**2. Entrar en la carpeta**

```bash
cd AgendaElectronica
```

**3. Instalar la dependencia**

```bash
pip install pyodbc
```

**4. Crear la base de datos**

Ejecutar en SQL Server Management Studio el siguiente script:

```sql
CREATE DATABASE AgendaElectronica;
GO

USE AgendaElectronica;
GO

CREATE TABLE Contactos (
    IdContacto INT IDENTITY(1,1) PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Apellido VARCHAR(100) NOT NULL,
    FechaNacimiento DATE NOT NULL,
    Direccion VARCHAR(250),
    Genero VARCHAR(20) NOT NULL,
    EstadoCivil VARCHAR(20) NOT NULL,
    Movil VARCHAR(20),
    Telefono VARCHAR(20),
    CorreoElectronico VARCHAR(150) NOT NULL UNIQUE,

    CONSTRAINT CK_Genero
    CHECK (Genero IN ('Masculino', 'Femenino', 'Otro')),

    CONSTRAINT CK_EstadoCivil
    CHECK (EstadoCivil IN (
        'Soltero/a',
        'Casado/a',
        'Divorciado/a',
        'Viudo/a'
    ))
);
GO
```

**5. Configurar la conexión**

Crear el archivo local `conexion.py` a partir de `conexion.example.py` y colocar el nombre de la instancia de SQL Server correspondiente a tu equipo.

**6. Ejecutar el sistema**

```bash
python main.py
```

## Autora Fran

Desarrollado como proyecto académico para poner en práctica los conocimientos de programación en Python, bases de datos SQL Server y desarrollo de interfaces gráficas.

---

**Agenda Electrónica** — Organización y gestión de contactos.
