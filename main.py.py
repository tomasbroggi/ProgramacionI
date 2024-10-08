import json
import random
import re
import tkinter as tk
from tkinter import messagebox, simpledialog

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

# Diccionario de Empleados
empleados = {
    4198078: {"Activo": True, "Apellido y Nombres": "Perez Joaquin", "Fecha de Nacimiento": "24/09/1998", "Fecha de Ingreso": "14/07/2022", "Celular": 1178964354, "Mail Corporativo": "JPerez@empresa.com", "IDProyectos": (1, 2), "IDRoles": 1}, 
    4198079: {"Activo": True, "Apellido y Nombres": "Garcia Maria", "Fecha de Nacimiento": "12/05/1995", "Fecha de Ingreso": "03/02/2020", "Celular": 1145678390, "Mail Corporativo": "MGarcia@empresa.com", "IDProyectos": (3, 4, 5), "IDRoles": 2}, 
    4198080: {"Activo": False, "Apellido y Nombres": "Lopez Ana", "Fecha de Nacimiento": "15/10/1990", "Fecha de Ingreso": "22/06/2018", "Celular": 1167895432, "Mail Corporativo": "ALopez@empresa.com", "IDProyectos": (6,), "IDRoles": 3}, 
    4198081: {"Activo": True, "Apellido y Nombres": "Rodriguez Juan", "Fecha de Nacimiento": "18/08/1988", "Fecha de Ingreso": "10/03/2019", "Celular": 1134567890, "Mail Corporativo": "JRodriguez@empresa.com", "IDProyectos": (7, 8, 9, 10), "IDRoles": 4}, 
    4198082: {"Activo": False, "Apellido y Nombres": "Fernandez Carla", "Fecha de Nacimiento": "03/04/1992", "Fecha de Ingreso": "28/11/2021", "Celular": 1156789345, "Mail Corporativo": "CFernandez@empresa.com", "IDProyectos": (11, 12), "IDRoles": 5}, 
    4198083: {"Activo": True, "Apellido y Nombres": "Sanchez Diego", "Fecha de Nacimiento": "11/02/1996", "Fecha de Ingreso": "06/09/2020", "Celular": 1123456789, "Mail Corporativo": "DSanchez@empresa.com", "IDProyectos": (13,), "IDRoles": 1}, 
    4198084: {"Activo": True, "Apellido y Nombres": "Martinez Laura", "Fecha de Nacimiento": "21/07/1997", "Fecha de Ingreso": "30/05/2021", "Celular": 1149876543, "Mail Corporativo": "LMartinez@empresa.com", "IDProyectos": (14, 15), "IDRoles": 2}, 
    4198085: {"Activo": True, "Apellido y Nombres": "Romero Pablo", "Fecha de Nacimiento": "05/09/1993", "Fecha de Ingreso": "07/12/2017", "Celular": 1165432987, "Mail Corporativo": "PRomero@empresa.com", "IDProyectos": (16,), "IDRoles": 3}, 
    4198086: {"Activo": False, "Apellido y Nombres": "Torres Monica", "Fecha de Nacimiento": "30/06/1989", "Fecha de Ingreso": "19/04/2022", "Celular": 1176543219, "Mail Corporativo": "MTorres@empresa.com", "IDProyectos": (17, 18), "IDRoles": 4}, 
    4198087: {"Activo": True, "Apellido y Nombres": "Alvarez Roberto", "Fecha de Nacimiento": "14/11/1986", "Fecha de Ingreso": "23/01/2019", "Celular": 1156789023, "Mail Corporativo": "RAlvarez@empresa.com", "IDProyectos": (19, 20), "IDRoles": 5}, 
    4198088: {"Activo": False, "Apellido y Nombres": "Gonzalez Isabel", "Fecha de Nacimiento": "07/07/1994", "Fecha de Ingreso": "11/10/2018", "Celular": 1187654321, "Mail Corporativo": "IGonzalez@empresa.com", "IDProyectos": (21,), "IDRoles": 1}, 
    4198089: {"Activo": True, "Apellido y Nombres": "Gomez Luis", "Fecha de Nacimiento": "19/11/1985", "Fecha de Ingreso": "20/08/2016", "Celular": 1143231123, "Mail Corporativo": "LGomez@empresa.com", "IDProyectos": (22, 23, 24), "IDRoles": 2}, 
    4198090: {"Activo": True, "Apellido y Nombres": "Morales Claudia", "Fecha de Nacimiento": "02/03/1989", "Fecha de Ingreso": "17/04/2018", "Celular": 1145672345, "Mail Corporativo": "CMorales@empresa.com", "IDProyectos": (25, 26), "IDRoles": 3}
}

# Diccionario de Roles
roles = {
    1: {"Nombre": "Project Lead", "Descripción": "Líder de Proyecto, responsable de la planificación y ejecución del proyecto."},
    2: {"Nombre": "Desarrollador", "Descripción": "Encargado de la implementación del software y solución de problemas técnicos."},
    3: {"Nombre": "Tester", "Descripción": "Responsable de las pruebas del software para asegurar su calidad."},
    4: {"Nombre": "Analista de Negocios", "Descripción": "Se encarga de analizar los requerimientos del cliente y traducirlos en especificaciones técnicas."},
    5: {"Nombre": "Diseñador UX/UI", "Descripción": "Responsable de la experiencia y la interfaz de usuario en el proyecto."},
}

# Diccionario de Proyectos
proyectos = {
    1: {"Nombre": "E-Commerce", "Descripción": "Desarrollo de E-Commerce para nuevo cliente", "Activo": False, "Fecha de Inicio": "01/11/2017", "Fecha de Fin": "01/03/2018"},
    2: {"Nombre": "Sistema de Gestión", "Descripción": "Implementación de sistema de gestión empresarial", "Activo": False, "Fecha de Inicio": "15/06/2020", "Fecha de Fin": "15/12/2021"},
    3: {"Nombre": "Portal Web", "Descripción": "Creación de un portal web informativo para ONG", "Activo": False, "Fecha de Inicio": "01/08/2019", "Fecha de Fin": "01/11/2019"},
    4: {"Nombre": "Plataforma Educativa", "Descripción": "Implementación de plataforma de educación en línea", "Activo": False, "Fecha de Inicio": "01/01/2020", "Fecha de Fin": "01/09/2021"},
    5: {"Nombre": "App Móvil", "Descripción": "Desarrollo de aplicación móvil para servicio de delivery", "Activo": True, "Fecha de Inicio": "01/05/2022", "Fecha de Fin": "01/11/2024"},
    6: {"Nombre": "Software de Contabilidad", "Descripción": "Desarrollo de software de contabilidad para pequeñas empresas", "Activo": True, "Fecha de Inicio": "01/10/2021", "Fecha de Fin": "01/04/2025"},
    7: {"Nombre": "Sistema de Reservas", "Descripción": "Creación de sistema de reservas para restaurantes", "Activo": False, "Fecha de Inicio": "01/03/2022", "Fecha de Fin": "01/06/2024"},
    8: {"Nombre": "Blog Corporativo", "Descripción": "Desarrollo de un blog corporativo para mejorar la comunicación", "Activo": True, "Fecha de Inicio": "01/09/2021", "Fecha de Fin": "01/12/2024"},
    9: {"Nombre": "Sistema de Inventario", "Descripción": "Implementación de un sistema de gestión de inventarios", "Activo": True, "Fecha de Inicio": "01/11/2023", "Fecha de Fin": "01/11/2025"},
    10: {"Nombre": "Rediseño de Marca", "Descripción": "Proyecto para el rediseño de la identidad corporativa", "Activo": False, "Fecha de Inicio": "01/08/2023", "Fecha de Fin": "01/09/2024"},
}

# Función para validar DNI
def validar_dni(dni):
    return re.match(r'^\d{7,8}$', str(dni)) is not None

# Función para agregar empleados
def agregar_empleado(dni, nombre, fecha_nacimiento, fecha_ingreso, celular, mail_corporativo, id_proyecto, id_rol):
    if validar_dni(dni):
        empleados[dni] = {
            "Activo": True,
            "Apellido y Nombres": nombre,
            "Fecha de Nacimiento": fecha_nacimiento,
            "Fecha de Ingreso": fecha_ingreso,
            "Celular": celular,
            "Mail Corporativo": mail_corporativo,
            "IDProyectos": id_proyecto,
            "IDRoles": id_rol
        }
        return f"Empleado con DNI {dni} agregado correctamente."
    return "DNI inválido."

# Función para obtener información de un empleado
def obtener_empleado(dni):
    empleado = empleados.get(dni)
    if empleado:
        return empleado
    return "Empleado no encontrado."

# Función para obtener proyectos activos
def obtener_proyectos_activos():
    return {id: info for id, info in proyectos.items() if info["Activo"]}

# Función para obtener roles
def obtener_roles():
    return roles

# Función para obtener información de un proyecto
def obtener_proyecto(id_proyecto):
    proyecto = proyectos.get(id_proyecto)
    if proyecto:
        return proyecto
    return "Proyecto no encontrado."

# Interfaz gráfica
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Empleados y Proyectos")
        self.root.geometry("500x500")

        self.label = tk.Label(root, text="Sistema de Gestión", font=("Arial", 20))
        self.label.pack(pady=10)

        self.boton_agregar = tk.Button(root, text="Agregar Empleado", command=self.agregar_empleado)
        self.boton_agregar.pack(pady=5)

        self.boton_obtener_empleado = tk.Button(root, text="Obtener Empleado", command=self.obtener_empleado)
        self.boton_obtener_empleado.pack(pady=5)

        self.boton_obtener_proyectos = tk.Button(root, text="Obtener Proyectos Activos", command=self.obtener_proyectos_activos)
        self.boton_obtener_proyectos.pack(pady=5)

        self.boton_obtener_roles = tk.Button(root, text="Obtener Roles", command=self.obtener_roles)
        self.boton_obtener_roles.pack(pady=5)

    def agregar_empleado(self):
        dni = simpledialog.askstring("DNI", "Ingrese el DNI del empleado:")
        nombre = simpledialog.askstring("Nombre", "Ingrese el nombre del empleado:")
        fecha_nacimiento = simpledialog.askstring("Fecha de Nacimiento", "Ingrese la fecha de nacimiento (dd/mm/yyyy):")
        fecha_ingreso = simpledialog.askstring("Fecha de Ingreso", "Ingrese la fecha de ingreso (dd/mm/yyyy):")
        celular = simpledialog.askstring("Celular", "Ingrese el celular del empleado:")
        mail_corporativo = simpledialog.askstring("Mail Corporativo", "Ingrese el mail corporativo del empleado:")
        id_proyecto = simpledialog.askinteger("ID Proyecto", "Ingrese el ID del proyecto:")
        id_rol = simpledialog.askinteger("ID Rol", "Ingrese el ID del rol:")

        mensaje = agregar_empleado(dni, nombre, fecha_nacimiento, fecha_ingreso, celular, mail_corporativo, id_proyecto, id_rol)
        messagebox.showinfo("Resultado", mensaje)

    def obtener_empleado(self):
        dni = simpledialog.askstring("DNI", "Ingrese el DNI del empleado:")
        empleado_info = obtener_empleado(dni)
        messagebox.showinfo("Información del Empleado", json.dumps(empleado_info, indent=4))

    def obtener_proyectos_activos(self):
        proyectos_activos = obtener_proyectos_activos()
        messagebox.showinfo("Proyectos Activos", json.dumps(proyectos_activos, indent=4))

    def obtener_roles(self):
        roles_info = obtener_roles()
        messagebox.showinfo("Roles", json.dumps(roles_info, indent=4))

# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
