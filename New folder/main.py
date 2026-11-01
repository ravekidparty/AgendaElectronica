import tkinter as tk
from tkinter import ttk, messagebox
from contactos import (
    insertar_contacto,
    listar_contactos,
    buscar_contactos,
    modificar_contacto,
    eliminar_contacto
)


class AgendaElectronica:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Agenda Electrónica")
        self.ventana.geometry("1150x700")
        self.ventana.configure(bg="#eef2f7")

        self.id_seleccionado = None
        self.campos = {}

        self.crear_interfaz()
        self.mostrar_contactos()

    def crear_interfaz(self):

        titulo = tk.Label(
            self.ventana,
            text="AGENDA ELECTRÓNICA",
            font=("Arial", 22, "bold"),
            bg="#eef2f7",
            fg="#243b53"
        )
        titulo.pack(pady=15)

        formulario = tk.LabelFrame(
            self.ventana,
            text="Información del contacto",
            font=("Arial", 12, "bold"),
            bg="white",
            padx=15,
            pady=15
        )
        formulario.pack(fill="x", padx=20, pady=10)

        campos = [
            ("Nombre", "nombre"),
            ("Apellido", "apellido"),
            ("Fecha de nacimiento (AAAA-MM-DD)", "fecha"),
            ("Dirección", "direccion"),
            ("Género", "genero"),
            ("Estado civil", "estado"),
            ("Móvil", "movil"),
            ("Teléfono", "telefono"),
            ("Correo electrónico", "correo")
        ]

        for i, (etiqueta, clave) in enumerate(campos):
            fila = i // 3
            columna = (i % 3) * 2

            tk.Label(
                formulario,
                text=etiqueta,
                bg="white",
                font=("Arial", 10)
            ).grid(row=fila, column=columna, sticky="w", padx=5, pady=8)

            if clave == "genero":
                entrada = ttk.Combobox(
                    formulario,
                    values=["Masculino", "Femenino", "Otro"],
                    state="readonly",
                    width=25
                )
            elif clave == "estado":
                entrada = ttk.Combobox(
                    formulario,
                    values=[
                        "Soltero/a",
                        "Casado/a",
                        "Divorciado/a",
                        "Viudo/a"
                    ],
                    state="readonly",
                    width=25
                )
            else:
                entrada = ttk.Entry(formulario, width=28)

            entrada.grid(
                row=fila,
                column=columna + 1,
                padx=5,
                pady=8
            )

            self.campos[clave] = entrada

        botones = tk.Frame(self.ventana, bg="#eef2f7")
        botones.pack(pady=10)

        tk.Button(
            botones, text="Guardar",
            command=self.guardar,
            bg="#198754", fg="white", width=14
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            botones, text="Modificar",
            command=self.modificar,
            bg="#0d6efd", fg="white", width=14
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            botones, text="Eliminar",
            command=self.eliminar,
            bg="#dc3545", fg="white", width=14
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            botones, text="Limpiar",
            command=self.limpiar,
            bg="#6c757d", fg="white", width=14
        ).grid(row=0, column=3, padx=5)

        busqueda = tk.Frame(self.ventana, bg="#eef2f7")
        busqueda.pack(fill="x", padx=20, pady=10)

        tk.Label(
            busqueda,
            text="Buscar por nombre, apellido o correo:",
            bg="#eef2f7"
        ).pack(side="left", padx=5)

        self.entrada_busqueda = ttk.Entry(busqueda, width=35)
        self.entrada_busqueda.pack(side="left", padx=5)

        tk.Button(
            busqueda,
            text="Buscar",
            command=self.buscar,
            bg="#243b53",
            fg="white"
        ).pack(side="left", padx=5)

        tk.Button(
            busqueda,
            text="Mostrar todos",
            command=self.mostrar_contactos
        ).pack(side="left", padx=5)

        tabla_frame = tk.Frame(self.ventana)
        tabla_frame.pack(fill="both", expand=True, padx=20, pady=10)

        columnas = (
            "ID", "Nombre", "Apellido", "Nacimiento",
            "Dirección", "Género", "Estado civil",
            "Móvil", "Teléfono", "Correo"
        )

        self.tabla = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        for columna in columnas:
            self.tabla.heading(columna, text=columna)
            self.tabla.column(columna, width=110, anchor="center")

        self.tabla.column("ID", width=45)
        self.tabla.column("Dirección", width=150)
        self.tabla.column("Correo", width=170)

        scroll_y = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tabla.yview
        )

        scroll_x = ttk.Scrollbar(
            tabla_frame,
            orient="horizontal",
            command=self.tabla.xview
        )

        self.tabla.configure(
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        self.tabla.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")
        scroll_x.grid(row=1, column=0, sticky="ew")

        tabla_frame.grid_rowconfigure(0, weight=1)
        tabla_frame.grid_columnconfigure(0, weight=1)

        self.tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_contacto
        )

    def obtener_datos(self):

        datos = [
            self.campos["nombre"].get().strip(),
            self.campos["apellido"].get().strip(),
            self.campos["fecha"].get().strip(),
            self.campos["direccion"].get().strip(),
            self.campos["genero"].get().strip(),
            self.campos["estado"].get().strip(),
            self.campos["movil"].get().strip(),
            self.campos["telefono"].get().strip(),
            self.campos["correo"].get().strip()
        ]

        if not all([
            datos[0], datos[1], datos[2],
            datos[4], datos[5], datos[8]
        ]):
            messagebox.showwarning(
                "Campos obligatorios",
                "Completa nombre, apellido, fecha, género, estado civil y correo."
            )
            return None

        return datos

    def guardar(self):

        datos = self.obtener_datos()

        if datos is None:
            return

        if insertar_contacto(datos):
            messagebox.showinfo(
                "Éxito",
                "Contacto guardado correctamente."
            )
            self.limpiar()
            self.mostrar_contactos()
        else:
            messagebox.showerror(
                "Error",
                "No se pudo guardar el contacto. Verifica los datos."
            )

    def mostrar_contactos(self):

        for elemento in self.tabla.get_children():
            self.tabla.delete(elemento)

        for contacto in listar_contactos():
            self.tabla.insert("", "end", values=contacto)

    def buscar(self):

        texto = self.entrada_busqueda.get().strip()

        for elemento in self.tabla.get_children():
            self.tabla.delete(elemento)

        for contacto in buscar_contactos(texto):
            self.tabla.insert("", "end", values=contacto)

    def seleccionar_contacto(self, evento):

        seleccion = self.tabla.selection()

        if not seleccion:
            return

        contacto = self.tabla.item(seleccion[0], "values")

        self.id_seleccionado = contacto[0]

        claves = [
            "nombre", "apellido", "fecha", "direccion",
            "genero", "estado", "movil", "telefono", "correo"
        ]

        for clave, valor in zip(claves, contacto[1:]):
            campo = self.campos[clave]
            campo.delete(0, tk.END)
            campo.insert(0, str(valor))

    def modificar(self):

        if self.id_seleccionado is None:
            messagebox.showwarning(
                "Selecciona un contacto",
                "Primero selecciona un contacto de la tabla."
            )
            return

        datos = self.obtener_datos()

        if datos is None:
            return

        if modificar_contacto(self.id_seleccionado, datos):
            messagebox.showinfo(
                "Éxito",
                "Contacto modificado correctamente."
            )
            self.limpiar()
            self.mostrar_contactos()
        else:
            messagebox.showerror(
                "Error",
                "No se pudo modificar el contacto."
            )

    def eliminar(self):

        if self.id_seleccionado is None:
            messagebox.showwarning(
                "Selecciona un contacto",
                "Primero selecciona un contacto de la tabla."
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Estás segura de que deseas eliminar este contacto?"
        )

        if confirmar:
            if eliminar_contacto(self.id_seleccionado):
                messagebox.showinfo(
                    "Éxito",
                    "Contacto eliminado correctamente."
                )
                self.limpiar()
                self.mostrar_contactos()
            else:
                messagebox.showerror(
                    "Error",
                    "No se pudo eliminar el contacto."
                )

    def limpiar(self):

        for campo in self.campos.values():
            campo.delete(0, tk.END)

        self.id_seleccionado = None

        for elemento in self.tabla.selection():
            self.tabla.selection_remove(elemento)


if __name__ == "__main__":
    ventana = tk.Tk()
    aplicacion = AgendaElectronica(ventana)
    ventana.mainloop()
