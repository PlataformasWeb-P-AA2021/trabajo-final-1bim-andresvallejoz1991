from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv


# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#Apertura del Archivo
provincia = open("data/Listado-Instituciones-Educativas.csv", "r", encoding="utf8")
#Lectura del archivo
datos_provincia = provincia.readlines()[1:] #[1:0] nos permite omitar el encabezado a la hora de leer los datos

lista1 = [] #Creacion de una lista que albergara los datos
#Obtención de datos unicos
for i in range(0,len(datos_provincia),1):#Ciclo repetivio para recorrer los datos
        d=datos_provincia[i].split("|") #Los datos se separan mediante split y su separador
        #Sacamos los atributos que necesitemos para la tabla provincia, en la posicion [2] se encuentra el codigo y en la [3] los nombres
        dat = d[2],d[3] #los almacenamos en una variable temporal 
        lista1.append(dat) #Con el append lo transformamos en lista enviandole la variable auxiliar 

lista1 = list(set(lista1)) #Mediante la funcion set obtenemos los valores unicos del excel de una lista de listas.
for i in lista1: #Ciclo for para recorrer la lista
        p = Provincia(codigo_prov=i[0], provincia=i[1]) #Se añaden los codigos de provincia que se encuentra en la posicon [0] de lista1 a la tabla
        #Se añade los nombres de las provincias que se encuentran en la posicion [] de lista1 a la tabla
        session.add(p) #add para añadirlos a la tabla

#Cierre del archivo

provincia.close()

# se confirma las transacciones
session.commit()

