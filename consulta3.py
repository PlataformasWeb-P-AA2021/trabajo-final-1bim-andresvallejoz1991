from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

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

Session = sessionmaker(bind=engine) # Objeto manejador de la base de Datos
# Creacion de un objeto tipo Session, mismo que va apermitir guardar, eliminar, actualizar, generar consultas en la base de datos
session = Session()

# Primero seleccionamos la entidad principal a consultar con session.query(),
# Luego un join a la/las tablas que necesitemos acceder y finalmente un filtrado con el numero de docentes por establecimiento
registros = session.query(Canton).join(Parroquia,Establecimiento).\
        filter(Establecimiento.num_docentes == 0).all()#all para obtener todos los resultados
 
#Impresion de la Consulta
print("Consulta N:-1 ")
print("Los cantones que tiene establecimientos con 0 número de profesores\n")
for i in registros: 
    print("%s" % (i))
print("-------------------------------------------------------------------------")    

# Primero seleccionamos la entidad principal a consultar con session.query(),
# Luego un join a la/las tablas que necesitemos acceder y finalmente un filter
# Dentro del filter tenemos dos condiones, la primera que las parroquias sean de Catacocha y el numero de estudiantes por establecimiento sea 21
registros_2 = session.query(Establecimiento).join(Parroquia).\
        filter(Parroquia.parroquia =="CATACOCHA",\
            Establecimiento.num_estudiantes >= 21).all()#all para obtener todos los resultados

#Impresion de la Consulta
print("Consulta N:-2 ")
print("Todos los establecimientos del cantón de Loja\n")
for i in registros_2: 
    print("%s" % (i))
print("-------------------------------------------------------------------------")  
