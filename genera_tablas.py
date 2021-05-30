from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

class Establecimiento(Base): #Creacion de la Entidad Establecimiento
    __tablename__ = 'establecimiento' #Nombre de la tabla
    codigo_amie = Column(String, primary_key=True) #LLave primaria de la Tabla
    parroquia_cod = Column(String, ForeignKey('parroquia.codigo_parroquia'), primary_key=True) # LLave foranea de la tabla parroquia
    parroquia = relationship("Parroquia", back_populates="nombre_institutos") #Relacion con la tabla parroquia con el atributo nombre_institutos
    nombre_instituto = Column(String(50), nullable=False)# atributo que guardas el nombre de las instituciones
    codigo_distrito = Column(String(50), nullable=False)# atributo que guardas el codigo de distrito
    modalidad = Column(String(50), nullable=False)# atributo que guarda la modalidad
    sostenimiento = Column(String(50), nullable=False)# atributo que guardas el sostenimiento
    jornada = Column(String(50), nullable=False)# atributo que guarda la jornada
    acceso = Column(String(50), nullable=False)# atributo que guardas el acceso
    tipo_edu = Column(String(50), nullable=False)# atributo que guarda el tipo de educacion 
    num_estudiantes = Column(String(50), nullable=False) # atributo que guarda el número de estudiantes
    num_docentes = Column(String(50), nullable=False) # atributo que guardas el número de docentes
#Se convierten los datos de tipo objeto a tipo String
    def __repr__(self):
        return "Establecimiento: Codigo-amie=%s\n Nombre-Institutos=%s\n Distrito=%s\n Modalidad=%s\n Sostenimiento=%s\n Jornada=%s\n Acceso=%s\n Tipo=%s\n Estudiantes=%s\n Docentes=%s\n"% (
                          self.codigo_amie, 
                          self.nombre_instituto,
                          self.codigo_distrito,
                          self.modalidad,
                          self.sostenimiento,
                          self.jornada,
                          self.acceso,
                          self.tipo_edu,
                          self.num_estudiantes,
                          self.num_docentes)
    

class Parroquia(Base): #Creacion de la entidad Parroquia
    __tablename__ = 'parroquia' #Nombre de la tabla
    codigo_parroquia = Column(String, primary_key=True) #LLave primaria de la tabla con los codigos de cada provincia
    canton_code = Column(String, ForeignKey('canton.codigo_canton'), primary_key=True) # LLave foranea de la tabla canton 
    canton = relationship("Canton", back_populates="parroquias") #Relacion con la tabla canton mediante el atributo parroquias
    nombre_institutos = relationship("Establecimiento", back_populates="parroquia")#Atributo de relacion con la tabla de establecimientos
    parroquia = Column(String(50))#Atributo con los nombres de las parroquias
    
#Se convierten los datos de tipo objeto a tipo String
    def __repr__(self):
        return "Parroquia: codigo=%s\n Parroquia=%s\n "% (
                          self.codigo_parroquia, 
                          self.parroquia)

class Canton(Base):#Creacion entidad Canton 
    __tablename__ = 'canton' #Nombre de la tabla
    codigo_canton = Column(String, primary_key=True) #LLave primaria con los codigos de cada canton 
    prov_cod= Column(String, ForeignKey('provincia.codigo_prov'), primary_key=True) #LLave foranea de la tabla provincia
    provincia = relationship("Provincia", back_populates="cantones") #Relacion con la tabla provincia mediante el atributo cantones
    parroquias = relationship("Parroquia", back_populates="canton") # Relacion con la tabla parroquia mediante el atributo canton 
    canton = Column(String(50)) # Atributos con los nombres de los cantones 
#Se convierten los datos de tipo objeto a tipo String
    def __repr__(self):
        return "Canton: codigo=%s\n canton=%s\n"% (
                          self.codigo_canton, 
                          self.canton)
    
#Nota: La tabla provincia es la primera en llenarse con datos ya que no posee llave foranea. 
class Provincia(Base): #Creacion de la Entidad Base
    __tablename__ = 'provincia' #Nombre de la tabla
    codigo_prov = Column(String, primary_key=True) #LLave primaria con los codigos de cada provincia
    cantones = relationship("Canton", back_populates="provincia") # Relacion con la tabla cantones con el atributo provincia
    provincia = Column(String(50)) #Atributo con los nombres de las provincias
#Se convierten los datos de tipo objeto a tipo String
    def __repr__(self):
        return "Provincia: codigo=%s\n Provincia=%s\n"% (
                          self.codigo_prov, 
                          self.provincia)
    

Base.metadata.create_all(engine)
