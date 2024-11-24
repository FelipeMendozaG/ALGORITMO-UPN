#En esta parte del sistema se importan las listas necesarias
#para la ejecucion del sistema
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime

# Declaramos las listas principal para almacenar 
# los datos registrados en cada lista
pacientes = []
medicos = []
internamientos = []
visitas = []
altas = []

# En esta parte de la estructura, se realizara la funcion
# de registro de pacientes
def registrar_paciente():
    def guardar_paciente():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        telefono = entry_telefono.get()
        fecha_nacimiento = entry_fecha_nacimiento.get()
        direccion = entry_direccion.get()
        distrito = entry_distrito.get()
        provincia = entry_provincia.get()
        departamento = entry_departamento.get()
        codigo_postal = entry_codigo_postal.get()

        paciente = {
            "id": len(pacientes) + 1,
            "nombre": nombre,
            "apellido": apellido,
            "telefono": telefono,
            "fecha_nacimiento": fecha_nacimiento,
            "direccion": direccion,
            "distrito": distrito,
            "provincia": provincia,
            "departamento": departamento,
            "codigo_postal": codigo_postal
        }
        pacientes.append(paciente)
        messagebox.showinfo("Registro exitoso", "Paciente registrado exitosamente")
        registro_paciente_window.destroy()

    #En esta parte del codigo se hace llamado a la libreria tkinter
    #se creara un boton de registro de paciente en modi grafico para el usuarios
    #done el usuario al hacer clic, le permitira ingresar a traves del teclado 
    #los datos del paciente que posteriormente se almacenaran en la lista paciente
    registro_paciente_window = tk.Toplevel(window)
    registro_paciente_window.title("Registrar Paciente")

    tk.Label(registro_paciente_window, text="Nombre").grid(row=0, column=0)
    entry_nombre = tk.Entry(registro_paciente_window)
    entry_nombre.grid(row=0, column=1)

    tk.Label(registro_paciente_window, text="Apellido").grid(row=1, column=0)
    entry_apellido = tk.Entry(registro_paciente_window)
    entry_apellido.grid(row=1, column=1)

    tk.Label(registro_paciente_window, text="Telefono").grid(row=2, column=0)
    entry_telefono = tk.Entry(registro_paciente_window)
    entry_telefono.grid(row=2, column=1)

    tk.Label(registro_paciente_window, text="Fecha de Nacimiento").grid(row=3, column=0)
    entry_fecha_nacimiento = tk.Entry(registro_paciente_window)
    entry_fecha_nacimiento.grid(row=3, column=1)

    tk.Label(registro_paciente_window, text="Direccion").grid(row=4, column=0)
    entry_direccion = tk.Entry(registro_paciente_window)
    entry_direccion.grid(row=4, column=1)

    tk.Label(registro_paciente_window, text="Distrito").grid(row=5, column=0)
    entry_distrito = tk.Entry(registro_paciente_window)
    entry_distrito.grid(row=5, column=1)

    tk.Label(registro_paciente_window, text="Provincia").grid(row=6, column=0)
    entry_provincia = tk.Entry(registro_paciente_window)
    entry_provincia.grid(row=6, column=1)

    tk.Label(registro_paciente_window, text="Departamento").grid(row=7, column=0)
    entry_departamento = tk.Entry(registro_paciente_window)
    entry_departamento.grid(row=7, column=1)

    tk.Label(registro_paciente_window, text="Codigo Postal").grid(row=8, column=0)
    entry_codigo_postal = tk.Entry(registro_paciente_window)
    entry_codigo_postal.grid(row=8, column=1)

    tk.Button(registro_paciente_window, text="Registrar", command=guardar_paciente).grid(row=9, columnspan=2)

#Una vez registrado el paciente, este se alamcenara en la lista paciente
#creando un ID de paciente automaticamente, que se podra mostrar a traves de
# este codigo
def mostrar_pacientes():
    pacientes_window = tk.Toplevel(window)
    pacientes_window.title("Pacientes Registrados")
    
    tree = ttk.Treeview(pacientes_window, columns=("ID", "Nombre", "Apellido", "Teléfono"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Apellido", text="Apellido")
    tree.heading("Teléfono", text="Teléfono")
    
    for paciente in pacientes:
        tree.insert("", "end", values=(paciente["id"], paciente["nombre"], paciente["apellido"], paciente["telefono"]))

    tree.pack(fill=tk.BOTH, expand=True)

# En esta parte de la estructura, se realizara la funcion
# de registro de medicos
def registrar_medico():
    def guardar_medico():
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        telefono = entry_telefono.get()
        especialidad = entry_especialidad.get()

        medico = {
            "id": len(medicos) + 1,
            "nombre": nombre,
            "apellido": apellido,
            "telefono": telefono,
            "especialidad": especialidad
        }
        medicos.append(medico)
        messagebox.showinfo("Registro exitoso", "Médico registrado exitosamente")
        registro_medico_window.destroy()

    #En esta parte del codigo se hace llamado a la libreria tkinter
    #se creara un boton de registro de paciente en modo grafico para el usuarios
    #done el usuario al hacer clic, le permitira ingresar a traves del teclado 
    #los datos del medico que posteriormente se almacenaran en la lista medico
    registro_medico_window = tk.Toplevel(window)
    registro_medico_window.title("Registrar Médico")

    tk.Label(registro_medico_window, text="Nombre").grid(row=0, column=0)
    entry_nombre = tk.Entry(registro_medico_window)
    entry_nombre.grid(row=0, column=1)

    tk.Label(registro_medico_window, text="Apellido").grid(row=1, column=0)
    entry_apellido = tk.Entry(registro_medico_window)
    entry_apellido.grid(row=1, column=1)

    tk.Label(registro_medico_window, text="Telefono").grid(row=2, column=0)
    entry_telefono = tk.Entry(registro_medico_window)
    entry_telefono.grid(row=2, column=1)

    tk.Label(registro_medico_window, text="Especialidad").grid(row=3, column=0)
    entry_especialidad = tk.Entry(registro_medico_window)
    entry_especialidad.grid(row=3, column=1)

    tk.Button(registro_medico_window, text="Registrar", command=guardar_medico).grid(row=4, columnspan=2)

#Una vez registrado el paciente, este se alamcenara en la lista medicos
#creando un ID de medico automaticamente, que se podra mostrar a traves de
# este codigo
def mostrar_medicos():
    medicos_window = tk.Toplevel(window)
    medicos_window.title("Médicos Registrados")

    tree = ttk.Treeview(medicos_window, columns=("ID", "Nombre", "Apellido", "Teléfono", "Especialidad"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Apellido", text="Apellido")
    tree.heading("Teléfono", text="Teléfono")
    tree.heading("Especialidad", text="Especialidad")

    for medico in medicos:
        tree.insert("", "end", values=(medico["id"], medico["nombre"], medico["apellido"], medico["telefono"], medico["especialidad"]))

    tree.pack(fill=tk.BOTH, expand=True)

# En esta parte de la estructura, se realizara la funcion
# de registro de internamiento
def registrar_internamiento():
    def guardar_internamiento():
        id_paciente = int(entry_id_paciente.get())  
        id_medico = int(entry_id_medico.get())  
        numero_sala = entry_numero_sala.get()
        numero_cama = entry_numero_cama.get()
        fecha_internamiento = datetime.datetime.now()

        internamiento = {
            "id": len(internamientos) + 1,
            "id_paciente": id_paciente,
            "id_medico": id_medico,
            "numero_sala": numero_sala,
            "numero_cama": numero_cama,
            "fecha_internamiento": fecha_internamiento,
            "hora_internamiento": fecha_internamiento.strftime("%H:%M:%S")
        }
        internamientos.append(internamiento)
        messagebox.showinfo("Internamiento exitoso", "Internamiento registrado exitosamente")
        registro_internamiento_window.destroy()

    #En esta parte del codigo se hace llamado a la libreria tkinter
    #se creara un boton de registro de internamiento en modo grafico para el usuarios
    #done el usuario al hacer clic, le permitira ingresar a traves del teclado 
    #los datos del medico que posteriormente se almacenaran en la lista internamiento
    registro_internamiento_window = tk.Toplevel(window)
    registro_internamiento_window.title("Registrar Internamiento")

    tk.Label(registro_internamiento_window, text="ID Paciente").grid(row=0, column=0)
    entry_id_paciente = tk.Entry(registro_internamiento_window)
    entry_id_paciente.grid(row=0, column=1)

    tk.Label(registro_internamiento_window, text="ID Médico").grid(row=1, column=0)
    entry_id_medico = tk.Entry(registro_internamiento_window)
    entry_id_medico.grid(row=1, column=1)

    tk.Label(registro_internamiento_window, text="Número de Sala").grid(row=2, column=0)
    entry_numero_sala = tk.Entry(registro_internamiento_window)
    entry_numero_sala.grid(row=2, column=1)

    tk.Label(registro_internamiento_window, text="Número de Cama").grid(row=3, column=0)
    entry_numero_cama = tk.Entry(registro_internamiento_window)
    entry_numero_cama.grid(row=3, column=1)

    tk.Button(registro_internamiento_window, text="Registrar", command=guardar_internamiento).grid(row=4, columnspan=2)

#Una vez registrado el internamiento, este se alamcenara en la lista internamiento
#creando un ID de medico automaticamente, que se podra mostrar a traves de
# este codigo
def mostrar_internamientos():
    internamientos_window = tk.Toplevel(window)
    internamientos_window.title("Internamientos Registrados")

    tree = ttk.Treeview(internamientos_window, columns=("ID", "Paciente", "Médico", "Número de Sala", "Número de Cama", "Fecha Internamiento", "Hora Internamiento"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Paciente", text="Paciente")
    tree.heading("Médico", text="Médico")
    tree.heading("Número de Sala", text="Número de Sala")
    tree.heading("Número de Cama", text="Número de Cama")
    tree.heading("Fecha Internamiento", text="Fecha Internamiento")
    tree.heading("Hora Internamiento", text="Hora Internamiento")

    for internamiento in internamientos:
        paciente = next(p for p in pacientes if p["id"] == internamiento["id_paciente"])
        medico = next(m for m in medicos if m["id"] == internamiento["id_medico"])
        tree.insert("", "end", values=(internamiento["id"], f"{paciente['nombre']} {paciente['apellido']}", f"{medico['nombre']} {medico['apellido']}", internamiento["numero_sala"], internamiento["numero_cama"], internamiento["fecha_internamiento"].strftime("%Y-%m-%d"), internamiento["hora_internamiento"]))

    tree.pack(fill=tk.BOTH, expand=True)

# Registro de visitas 
def registrar_visita():
    def guardar_visita():
        id_paciente = int(entry_id_paciente.get())
        id_medico = int(entry_id_medico.get())
        nota_visita = entry_nota_visita.get()
        fecha_visita = datetime.datetime.now()

        visita = {
            "id": len(visitas) + 1,
            "id_paciente": id_paciente,
            "id_medico": id_medico,
            "nota_visita": nota_visita,
            "fecha_visita": fecha_visita,
            "hora_visita": fecha_visita.strftime("%H:%M:%S")
        }
        visitas.append(visita)
        messagebox.showinfo("Visita registrada", "Visita registrada exitosamente")
        registro_visita_window.destroy()

    registro_visita_window = tk.Toplevel(window)
    registro_visita_window.title("Registrar Visita")

    tk.Label(registro_visita_window, text="ID Paciente").grid(row=0, column=0)
    entry_id_paciente = tk.Entry(registro_visita_window)
    entry_id_paciente.grid(row=0, column=1)

    tk.Label(registro_visita_window, text="ID Médico").grid(row=1, column=0)
    entry_id_medico = tk.Entry(registro_visita_window)
    entry_id_medico.grid(row=1, column=1)

    tk.Label(registro_visita_window, text="Nota Visita").grid(row=2, column=0)
    entry_nota_visita = tk.Entry(registro_visita_window)
    entry_nota_visita.grid(row=2, column=1)

    tk.Button(registro_visita_window, text="Registrar", command=guardar_visita).grid(row=3, columnspan=2)

# Mostrar visitas
def mostrar_visitas():
    visitas_window = tk.Toplevel(window)
    visitas_window.title("Visitas Registradas")

    tree = ttk.Treeview(visitas_window, columns=("ID", "Paciente", "Médico", "Nota Visita", "Fecha Visita", "Hora Visita"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Paciente", text="Paciente")
    tree.heading("Médico", text="Médico")
    tree.heading("Nota Visita", text="Nota Visita")
    tree.heading("Fecha Visita", text="Fecha Visita")
    tree.heading("Hora Visita", text="Hora Visita")

    for visita in visitas:
        paciente = next(p for p in pacientes if p["id"] == visita["id_paciente"])
        medico = next(m for m in medicos if m["id"] == visita["id_medico"])
        tree.insert("", "end", values=(visita["id"], f"{paciente['nombre']} {paciente['apellido']}", f"{medico['nombre']} {medico['apellido']}", visita["nota_visita"], visita["fecha_visita"].strftime("%Y-%m-%d"), visita["hora_visita"]))

    tree.pack(fill=tk.BOTH, expand=True)

# Registrar alta (ahora con médico que autoriza y motivo de la alta)
def registrar_alta():
    def guardar_alta():
        id_paciente = int(entry_id_paciente.get())
        id_medico = int(entry_id_medico.get())
        motivo_alta = entry_motivo_alta.get()
        fecha_alta = datetime.datetime.now()

        alta = {
            "id": len(altas) + 1,
            "id_paciente": id_paciente,
            "id_medico": id_medico,
            "motivo_alta": motivo_alta,
            "fecha_alta": fecha_alta,
            "hora_alta": fecha_alta.strftime("%H:%M:%S")
        }
        altas.append(alta)
        messagebox.showinfo("Alta registrada", "Alta registrada exitosamente")
        registro_alta_window.destroy()

    registro_alta_window = tk.Toplevel(window)
    registro_alta_window.title("Registrar Alta")

    tk.Label(registro_alta_window, text="ID Paciente").grid(row=0, column=0)
    entry_id_paciente = tk.Entry(registro_alta_window)
    entry_id_paciente.grid(row=0, column=1)

    tk.Label(registro_alta_window, text="ID Médico (Autoriza)").grid(row=1, column=0)
    entry_id_medico = tk.Entry(registro_alta_window)
    entry_id_medico.grid(row=1, column=1)

    tk.Label(registro_alta_window, text="Motivo de Alta").grid(row=2, column=0)
    entry_motivo_alta = tk.Entry(registro_alta_window)
    entry_motivo_alta.grid(row=2, column=1)

    tk.Button(registro_alta_window, text="Registrar", command=guardar_alta).grid(row=3, columnspan=2)

# Mostrar altas
def mostrar_altas():
    altas_window = tk.Toplevel(window)
    altas_window.title("Altas Registradas")

    tree = ttk.Treeview(altas_window, columns=("ID", "Paciente", "Médico", "Motivo Alta", "Fecha Alta", "Hora Alta"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Paciente", text="Paciente")
    tree.heading("Médico", text="Médico")
    tree.heading("Motivo Alta", text="Motivo Alta")
    tree.heading("Fecha Alta", text="Fecha Alta")
    tree.heading("Hora Alta", text="Hora Alta")

    for alta in altas:
        paciente = next(p for p in pacientes if p["id"] == alta["id_paciente"])
        medico = next(m for m in medicos if m["id"] == alta["id_medico"])
        tree.insert("", "end", values=(alta["id"], f"{paciente['nombre']} {paciente['apellido']}", f"{medico['nombre']} {medico['apellido']}", alta["motivo_alta"], alta["fecha_alta"].strftime("%Y-%m-%d"), alta["hora_alta"]))

    tree.pack(fill=tk.BOTH, expand=True)

#Para darle una estructura grafica de facil uso al sistema 
#Crearemos una ventana de opciones que el usuario seleccionara
#para realizar una funcion
window = tk.Tk()
window.title("Hospital Management System")

# Agregar título "CLINICA SANTO TOMAS"
tk.Label(window, text="CLINICA SANTO TOMAS", font=("Helvetica", 16, "bold")).pack(pady=10)

# Botones
tk.Button(window, text="Registrar Paciente", command=registrar_paciente).pack(fill=tk.X)
tk.Button(window, text="Mostrar Pacientes", command=mostrar_pacientes).pack(fill=tk.X)
tk.Button(window, text="Registrar Médico", command=registrar_medico).pack(fill=tk.X)
tk.Button(window, text="Mostrar Médicos", command=mostrar_medicos).pack(fill=tk.X)
tk.Button(window, text="Registrar Internamiento", command=registrar_internamiento).pack(fill=tk.X)
tk.Button(window, text="Mostrar Internamientos", command=mostrar_internamientos).pack(fill=tk.X)
tk.Button(window, text="Registrar Visita", command=registrar_visita).pack(fill=tk.X)
tk.Button(window, text="Mostrar Visitas", command=mostrar_visitas).pack(fill=tk.X)
tk.Button(window, text="Registrar Alta", command=registrar_alta).pack(fill=tk.X)
tk.Button(window, text="Mostrar Altas", command=mostrar_altas).pack(fill=tk.X)

# Botón para salir
tk.Button(window, text="Salir", command=window.quit).pack(fill=tk.X)

window.mainloop()
