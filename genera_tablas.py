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

class Establecimiento(Base):
    __tablename__ = 'establecimiento'
    codigo_amie = Column(String, primary_key=True)
    parroquia_cod = Column(String, ForeignKey('parroquia.codigo_parroquia'), primary_key=True)
    parroquia = relationship("Parroquia", back_populates="")
    nombre_instituto = Column(String(50), nullable=False)
    modalidad = Column(String(50), nullable=False)
    sostenimiento = Column(String(50), nullable=False)
    jornada = Column(String(50), nullable=False)
    acceso = Column(String(50), nullable=False)
    tipo_edu = Column(String(50), nullable=False)
    num_estudiantes = Column(String(50), nullable=False)
    num_docentes = Column(String(50), nullable=False)

    def __repr__(self):
        return "Establecimiento: Codigo-amie=%s\n Nombre-Institutos=%s\n"% (
                          self.codigo_amie, 
                          self.nombre_instituto)
    

class Parroquia(Base):
    __tablename__ = 'parroquia'
    codigo_parroquia = Column(String, primary_key=True)
    canton_code = Column(String, ForeignKey('canton.codigo_canton'), primary_key=True)
    canton = relationship("Canton", back_populates="parroquia")
    nombre_institutos = relationship("Establecimiento", back_populates="parroquia")
    parroquia = Column(String(50))
    codigo_distrito= Column(String(50))
    
    def __repr__(self):
        return "Parroquia: codigo=%s\n Parroquia=%s\n"% (
                          self.codigo_parroquia, 
                          self.parroquia)

class Canton(Base):
    __tablename__ = 'canton'
    codigo_canton = Column(Integer, primary_key=True)
    prov_cod= Column(String, ForeignKey('provincia.codigo_prov'), primary_key=True)
    provincia = relationship("Provincia", back_populates="cantones")
    parroquias = relationship("Parroquia", back_populates="canton")
    canton = Column(String(50))

    def __repr__(self):
        return "Canton: codigo=%s\n canton=%s\n"% (
                          self.codigo_canton, 
                          self.canton)
    

class Provincia(Base):
    __tablename__ = 'provincia'
    codigo_prov = Column(String, primary_key=True)
    cantones = relationship("Canton", back_populates="provincia")
    provincia = Column(String(50))

    def __repr__(self):
        return "Provincia: codigo=%s\n Provincia=%s\n"% (
                          self.codigo_prov, 
                          self.Provincia)
    

Base.metadata.create_all(engine)
