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
parroquia = open("data/Listado-Instituciones-Educativas.csv", "r", encoding="utf8")
#Lectura del archivo
datos_parroquia = parroquia.readlines()[1:] #[1:0] nos permite omitar el encabezado a la hora de leer los datos

lista1 = [] #Creacion de una lista que albergara los datos

#Obtención de datos unicos 
for i in range(0,len(datos_parroquia),1):#Ciclo repetivio para recorrer los datos
        d=datos_parroquia[i].split("|") #Los datos se separan mediante split y su separador
		#Sacamos los atributos que necesitemos del excel, en la posicion [6] se encuentra el codigo y en la [7] los nombres de los parroquias
        dat = d[6],d[7],d[4] #Se añade la posicion [4] donde se encuentra el codigo_canton que es la llave foranea dentro de la tabla parroquia
        lista1.append(dat) #Con el append lo transformamos en lista enviandole la variable auxiliar
		
        

lista1 = list(set(lista1)) #Mediante la funcion set obtenemos los valores unicos del excel de una lista de listas.
#print(lista1)
for i in lista1:
	#se toman los datos de la entidad Canton y se filtran si el codigo_canton es igual al codigo de canton de la lista1
	datos_cantones = session.query(Canton).filter_by(codigo_canton = i[2]).first() #first devuelve el primer valor de la columna seleccionada
	#De esta manera podemos relacionar las tablas de parroquia y canton 
	#print(datos_cantones)
	p = Parroquia(codigo_parroquia=i[0],parroquia=i[1],canton=datos_cantones)# Los valores dentro de lista1 cambian con respecto a dat 
	session.add(p)#Se añade a la tabla
	#print(p)
        
	
parroquia.close()#Cierre del archivo

session.commit()# se confirma las transacciones



