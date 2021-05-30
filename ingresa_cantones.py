from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Establecimiento, Parroquia, Canton, Provincia

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
canton = open("data/Listado-Instituciones-Educativas.csv", "r", encoding="utf8")
#Lectura del archivo
datos_canton = canton.readlines()[1:] #[1:0] nos permite omitar el encabezado a la hora de leer los datos

lista1 = []#Creacion de una lista que albergara los datos

#Obtención de datos unicos
for i in range(0,len(datos_canton),1):#Ciclo repetivio para recorrer los datos
        d=datos_canton[i].split("|") #Los datos se separan mediante split y su separador
		#Sacamos los atributos que necesitemos para la tabla cantones, en la posicion [4] se encuentra el codigo y en la [3] los nombres de los cantones
		#los almacenamos en una variable temporal 
        dat = d[4],d[5],d[2] #Se añade la posicion [2] donde se encuentra el codigo_pronvincia que es la llave foranea dentro de la tabla canton
        lista1.append(dat)#Con el append lo transformamos en lista enviandole la variable auxiliar 
		
        

lista1 = list(set(lista1))#Mediante la funcion set obtenemos los valores unicos del excel de una lista de listas.
#print(lista1)
for i in lista1: #Ciclo for para recorrer la lista
		datos_provincias = session.query(Provincia).filter_by(codigo_prov = i[2]).first() #first devuelve el primer valor de la columna seleccionada
		#se toman los datos de la entidad provincia y se filtran si el codigo de provincia es igual al codigo de provincia de la lista1
		#De esta manera podemos relacionar las tablas de canton y provincia
		#print(datos_provincias)
		p = Canton(codigo_canton=i[0], canton=i[1],provincia=datos_provincias) # Los valores dentro de lista1 cambian con respecto a dat 
		session.add(p) #Se añade a la tabla
		#print(p)
        
	
canton.close() #Cierre del archivo

session.commit() # se confirma las transacciones

