import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
apellido: Ledezma
nombre: Juan Pablo

Enunciado:


A)  Al presionar el botón 'Agregar' se deberan cargar tantos vehiculos como el usuario desee. 
    Los datos a cargar de cada vehiculo son: marca (ford, volvo, fiat), tipo de vehiculo (auto, camioneta, moto) y kilometros*.

* Todos los autos son usados.

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar se deberan listar todos los vehiculos ingresados con su correspondiente kilometraje y su posicion en la lista.
Ejemplo: 1 - Ford - Auto - 1000 km
         2 - Fiat - Camioneta - 2000 km
         etc..

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al presionar el boton Informar 
    0- El mayor kilometraje y su tipo de vehiculo.
    1- El menor kilometraje y su tipo de vehiculo de marca 'Ford'.
    2- Kilometraje promedio de los autos por cada marca.
    -3- Precio promedios de todos los servicios por marca.
    4- Informar los kilometrajes que superan el promedio (total) por tipo.
    5- Informar los kilometrajes que NO superan el promedio (total) por marca.
    -6- Informar la cantidad de tipos por marca.
    7- Informar el precio promedio de los servicios cuyo kilometraje es mayor a 10000 kms de marca 'Volvo'.
    8- Indicar el mayor de los promedios de kilometros por tipo de vehiculo.
    9- Informar el monto promedio de los servicios de marca 'Ford'.


Los montos de los servicios son:
    - Auto: $15000
    - Camioneta: $25000
    - Moto: $10000
    
    *Si la marca es volvo tiene un recargo del 10%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EXAMEN INGRESO")
        
        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_tipo_vehiculo = []
        self.lista_marca_vehiculo = []
        self.lista_kms_vehiculos = []

    def btn_agregar_on_click(self):
        
        continuar = True

        while continuar:
            marca_vehiculo = prompt("Ingreso marca", "Ingrese la marca del vehículo")
            while marca_vehiculo == None or not(marca_vehiculo.lower() == "ford" or marca_vehiculo.lower() == "volvo" or marca_vehiculo.lower() == "fiat"):
                marca_vehiculo = prompt("Error", "La marca debe ser volvo, ford o fiat")

            tipo_vehiculo = prompt("Ingreso tipo", "Ingrese el tipo del vehículo")
            while tipo_vehiculo == None or not(tipo_vehiculo.lower() == "auto" or tipo_vehiculo.lower() == "camioneta" or tipo_vehiculo.lower() == "moto"):
                tipo_vehiculo = prompt("Error", "El tipo del vehiculo debe ser auto, camioneta o moto")
            
            km_vehiculo = prompt("Ingreso Kilometros", "Ingrese los kilometros del vehiculo")
            while km_vehiculo == None or float(km_vehiculo) <= 0:
                km_vehiculo = prompt("Error", "Los kilometros deben ser mayores a 0")

            self.lista_kms_vehiculos.append(float(km_vehiculo))
            self.lista_marca_vehiculo.append(marca_vehiculo.lower())
            self.lista_tipo_vehiculo.append(tipo_vehiculo.lower())

            continuar = question("Continuar", "¿Desea continuar?")

    
    def btn_mostrar_on_click(self):

        muestra = ""
        total_vehiculos = len(self.lista_tipo_vehiculo)

        for i in range (0, total_vehiculos):
            muestra += str(i) + ". - " + self.lista_marca_vehiculo[i]
            muestra += " - " + self.lista_tipo_vehiculo[i] + " - "
            muestra += str(self.lista_kms_vehiculos[i]) + " km\n"

        alert("Muestra", muestra)


    def btn_informar_on_click(self):
        
        cantidad_vehiculos = len(self.lista_marca_vehiculo)
        total_servicios_ford = 0
        total_servicios_fiat = 0
        total_servicios_volvo = 0

        for i in range (0, cantidad_vehiculos):
            marca_vehiculo = self.lista_marca_vehiculo[i]
            tipo_vehiculo = self.lista_tipo_vehiculo[i]

            match marca_vehiculo:
                case "ford":
                    match tipo_vehiculo:
                        case "auto":
                            total_servicios_ford += 15000
                        case "camioneta":
                            total_servicios_ford += 25000
                        case "moto":
                            total_servicios_ford += 10000


    
if __name__ == "__main__":
    app = App()
    app.geometry("200x400")
    app.mainloop()

