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
establecimiento = open("data/Listado-Instituciones-Educativas.csv", "r", encoding="utf8")
#Lectura del archivo
datos_establecimiento = establecimiento.readlines()[1:] #[1:0] nos permite omitar el encabezado a la hora de leer los dat
lista1 = [] #Creacion de una lista que albergara los datos
#Obtencion de datos unicos de datos 
for i in range(0,len(datos_establecimiento),1): #Ciclo repetivio para recorrer los datos
        d=datos_establecimiento[i].split("|")#Los datos se separan mediante split y su separador
		#Almacenamos los atributos del excel en la variable dat
		#En la posicon [0] se encuentra la llave primaria con el codigo amie y en la posicion [1] se encuentra los nombres de los establecimientos
		# El resto de posicion representa los demos atributos colocados en la tabla establecimiento de genera_tablas.py 
        dat = d[0],d[1],d[8],d[11],d[9],d[12],d[13],d[10],d[14],d[15],d[6] #El ultimo atributo d[6] representa la llave foranea de parroquias
        lista1.append(dat) #Con el append lo transformamos en lista enviandole la variable auxiliar dat

lista1 = list(set(lista1)) #Mediante la funcion set obtenemos los valores unicos del excel de una lista de listas.
#print(lista1)
for i in lista1:
	#se toman los datos de la entidad Parroquia y se filtran si el codigo_parroquia es igual al codigo de llave foranea de la lista1
	datos_parroquia = session.query(Parroquia).filter_by(codigo_parroquia = i[10]).first() #first devuelve el primer valor de la columna seleccionada
	#De esta manera podemos relacionar las tablas de establecimiento y parroquia
	#print(datos_parroquia)
	# Los valores dentro de lista1 cambian con respecto a dat
	p = Establecimiento(codigo_amie=i[0],nombre_instituto=i[1],codigo_distrito=i[2],modalidad=i[3],sostenimiento=i[4],jornada=i[5],acceso=i[6],\
		tipo_edu=i[7],num_estudiantes=i[8],num_docentes=i[9],parroquia=datos_parroquia)
	session.add(p)#Se añade a la tabla
	#print(p)

#Cierre del archivo
establecimiento.close()

# se confirma las transacciones
session.commit()
