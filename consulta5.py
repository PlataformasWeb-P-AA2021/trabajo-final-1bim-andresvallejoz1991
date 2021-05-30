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
# Aplicamos un Join a la/las tablas que necesitemos
# Un filter que mediante el operador and que verifica que dos condiones se cumplan 
# El numero de docentes por establecimiento debe ser mayor o igual a 20 y que el tipo de educacion sea Permanente con la funcion like
# y ordenados por la parroquia mediante order_by 
registros = session.query(Establecimiento).join(Parroquia).\
        filter(and_(Establecimiento.num_docentes >=20,\
            Establecimiento.tipo_edu.like("%Permanente%"))).order_by(Parroquia.parroquia).all()
 
#Impresion de la Consulta
print("Consulta N:-1 ")
print("Los establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena Permanente en tipo de educación\n")
for i in registros: 
    print("%s" % (i))
print("-------------------------------------------------------------------------")    

# Primero seleccionamos la entidad principal a consultar con session.query(),
# En esta caso no aplicamos un Join , un filtrado con los establecimientos con el codigo de distrito 11D02
# y ordenados por el sostenimiento mediante el order_by.
registros_2 = session.query(Establecimiento).filter(Establecimiento.codigo_distrito == "11D02").\
        order_by(Establecimiento.sostenimiento).all()

#Impresion de la Consulta
print("Consulta N:-2 ")
print("Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02\n")
for i in registros_2: 
    print("%s" % (i))
print("-------------------------------------------------------------------------")  