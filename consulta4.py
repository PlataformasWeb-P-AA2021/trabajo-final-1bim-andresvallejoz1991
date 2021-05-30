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

Session = sessionmaker(bind=engine)# Objeto manejador de la base de Datos
# Creacion de un objeto tipo Session, mismo que va apermitir guardar, eliminar, actualizar, generar consultas en la base de datos
session = Session()

# Primero seleccionamos la entidad principal a consultar con session.query(),
# En esta caso no aplicamos un Join , un filtrado con el numero de docentes por establecimiento que sea mayor a 100
# y ordenados por el numero de estudiantes con un order_by 
registros = session.query(Establecimiento).filter(Establecimiento.num_docentes > 100).\
        order_by(Establecimiento.num_estudiantes).all()#all para obtener todos los resultados
 
#Impresion de la Consulta
print("Consulta N:-1 ")
print("Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores\n")
for i in registros: 
    print("%s" % (i))
print("-------------------------------------------------------------------------")    

# Primero seleccionamos la entidad principal a consultar con session.query(),
# En esta caso no aplicamos un Join , un filtrado con el numero de docentes por establecimiento que sea mayor a 100
# y ordenados por el numero de docentes con un order_by 
registros_2 = session.query(Establecimiento).filter(Establecimiento.num_docentes > 100).\
        order_by(Establecimiento.num_docentes).all()#all para obtener todos los resultados

#Impresion de la Consulta
print("Consulta N:-2 ")
print("Todos los establecimientos del cantón de Loja\n")
for i in registros_2: 
    print("%s" % (i))
print("-------------------------------------------------------------------------")  
