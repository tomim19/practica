# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ejercicio_01 import Base, Persona, reset_tabla, borrar_Tabla
from ejercicio_02 import agregar_persona

borrar_Tabla()
engine = create_engine( 'sqlite:///sqlalchemy_practico03A.db',echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def buscar_persona(id_persona):
    usuario = session.query(Persona).filter(Persona.IdPersona==id_persona).one()
    if usuario is None:
        return False
    else:
        resultado= [usuario.IdPersona, usuario.Nombre, usuario.FechaNacimiento, usuario.DNI, usuario.Altura]
        print (resultado)
        return resultado

@reset_tabla
def pruebas():

    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15).strftime("%Y-%m-%d %H:%M:%S"), 32165498, 180))
    print (juan)
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15).strftime("%Y-%m-%d %H:%M:%S"), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
