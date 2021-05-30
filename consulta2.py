from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_  # se importa el operador and
from sqlalchemy import or_ #Se importa el operador or
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
# Luego un join a la/las tablas que necesitemos acceder y finalmente un filtrado para las instituciones con jornada Nocturna
registros = session.query(Parroquia).join(Establecimiento).\
        filter(Establecimiento.jornada == "Nocturna").all()#all para obtener todos los resultados

#Impresion de la Consulta
print("Consulta N:-1 ")
print("Las parroquias que tienen establecimientos únicamente en la jornada Nocturna\n")
for i in registros:
    print("%s" % (i))
print("-------------------------------------------------------------------------")

# Primero seleccionamos la entidad principal a consultar con session.query(),
# Luego un join a la/las tablas que necesitemos acceder y finalmente un filtrado para los establecimientos con distintos números de estudiantes
# Dentro del filter usamos el operador or que verifica que almenos 1 condiciones se cumpla para obtener resultados
registros_2 = session.query(Canton).join(Parroquia, Establecimiento).\
        filter(or_(Establecimiento.num_estudiantes == 448, Establecimiento.num_estudiantes == 450,
        	Establecimiento.num_estudiantes == 451, Establecimiento.num_estudiantes == 454, Establecimiento.num_estudiantes == 458,
        	Establecimiento.num_estudiantes == 459)).all() #all para obtener todos los resultados

#Impresion de la Consulta
print("Consulta N:-2")
print("Los cantones que tienen establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459\n")
for i in registros_2:
    print("%s" % (i))
print("-------------------------------------------------------------------------")
