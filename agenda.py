# descargar las librerarías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#inputs
inputs = {
    'ruta_contactos': './data/contacts.csv'
}

#construcción de clase
class Directorio:

    def __init__(self,inputs):
        self.inputs = inputs
        self.datos = pd.read_csv(self.inputs['ruta_contactos'])

    #CRUD = Create Read Update Delete
    def create_contact(self):
        
        print('\n'+'--------------------'+'\n'+'CREAR NUEVO CONTACTO'+'\n'+'--------------------'+'\n')

        name = input('Nombre: ')
        last_name = input('Apellido: ')
        tel = input('Telefono: ')
        mail = input('Correo: ')

        nuevo_contacto = [name,last_name,tel,mail]

        n = len(self.datos)
        self.datos.loc[n] = nuevo_contacto

        #refresh the database
        self.datos.to_csv(self.inputs['ruta_contactos'],index=False)

    def read_contacts(self):
        print('\n'+'--------------------'+'\n'+'MIS CONTACTOS'+'\n'+'--------------------'+'\n')
        print(self.datos)

    def update_contact(self,contact):
        pass

    def delete_contact(self,contact):
        pass

#aplicación
dir = Directorio(inputs)
dir.read_contacts()
dir.create_contact()
dir.read_contacts()