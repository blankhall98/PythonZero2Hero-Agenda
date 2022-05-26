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
        print('Bienvenid@ a tu agenda virtual en Python!'+'\n')
        self.menu()

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
        print('\n')

    def update_contact(self,contact_name,contact_lastname):
        #condicion de que name y last name estan en base
        

        #busqueda
        target_contact = self.datos[(self.datos['Nombre']==contact_name)&(self.datos['Apellido']==contact_lastname)]
        print('\n'+'La información anterior es: ' + '\n')
        print(target_contact)
        print('\n')
        target_index = target_contact.index[0]
        
        #creación del contacto
        name = input('Nombre: ')
        last_name = input('Apellido: ')
        tel = input('Telefono: ')
        mail = input('Correo: ')

        nuevo_contacto = [name,last_name,tel,mail]

        self.datos.loc[target_index] = nuevo_contacto

        #refresh the database
        self.datos.to_csv(self.inputs['ruta_contactos'],index=False)

    def delete_contact(self,contact):
        pass

    def menu(self):

        repeat = True
        while repeat:
            #acción de interés
            print('\n')
            action = input('¿Que desdeas hacer?'+'\n'+'1 = crear contacto / 2 = ver contactos' +
             '\n' + '3 = actualizar contacto: ')
            print('\n')
            if action == '1':
                self.create_contact()
            elif action == '2':
                self.read_contacts()
            elif action == '3':
                target_name = input('name: ')
                target_lastname = input('lastname: ')
                self.update_contact(target_name,target_lastname)

            #condición de repetición
            repeat = input('¿Desea realizar otra accion? (s/n): ')
            if repeat == 's':
                repeat = True
            elif repeat == 'n':
                repeat = False
        print('\n'+'Hasta Luego!')

#aplicación
dir = Directorio(inputs)