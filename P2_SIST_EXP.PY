import collections.abc
import collections

# Parche para compatibilidad de experta con Python 3.10+
collections.Mapping = collections.abc.Mapping
collections.MutableMapping = collections.abc.MutableMapping
collections.Sequence = collections.abc.Sequence
collections.Iterable = collections.abc.Iterable

from experta import Fact, KnowledgeEngine, Rule, NOT, MATCH

# PARTE 1_Definir hechos

class Sintoma(Fact):
    pass

class Diagnostico(Fact):
    pass

# PARTE 2_EJ1_Creación del sistema experto

class SistDiagnosticoMedico(KnowledgeEngine):
    """
    Motor de inderencia para diagnostico medico simple basado en ecademnamiento
    hacia adelante mediante la libreria experta.
    """

    # REGLAS

    @Rule(Sintoma(fiebre=True, tos=True, dolor_garganta=True))
    def regla_Gripe(self):
        """Diagnostico de Gripe"""
        self.declare(Diagnostico(enfermedad="Gripe"))
        print("\nDIAGNOSTICO IDENTIFICADO: Gripe")
        print("RECOMENDACIÓN: Reposo en cama, abundante hidratación y tomar analgésicos.")

    @Rule(Sintoma(fiebre=True, dolor_cabeza=True, nauseas=True))
    def regla_Migrana(self):
        """Diagnostico de Migraña"""
        self.declare(Diagnostico(enfermedad="Migraña"))
        print("\nDIAGNOSTICO IDENTIFICADO: Migraña")
        print("RECOMENDACIÓN: Reposo en una habitación oscura y silenciosa. Evitar la luz brillante y mantenerse hidratado.")

        @Rule(Sintoma(estornudos=True, congestión_nasal=True, picazón_ojos=True))
        def regla_Alergia(self):
            """Diagnostico de Alergia"""
            self.declare(Diagnostico(enfermedad="Alergia"))
            print("\nDIAGNOSTICO IDENTIFICADO: Alergia")
            print("RECOMENDACIÓN: Evitar los alérgenos conocidos.")

        @Rule(Sintoma(dolorestomago=True, diarrea=True, vomito=True))
        def regla_gastroenteritis(self):
            """Diagnostico de Gastroenteritis"""
            self.declare(Diagnostico(enfermedad="Gastroenteritis"))
            print("\nDIAGNOSTICO IDENTIFICADO: Gastroenteritis")
            print("RECOMENDACIÓN: Consumir suero oral en pequeñas cantidades para evitar la deshidratación y mantener dieta blanta.")

# Reglas ampliadas_EJE1 

@Rule(Sintoma(fiebre=True, tos_seca=True, perdida_olfato=True))
def regla_covid(self):
    """Ampliación 1: COVID-19"""
    self.declare(Diagnostico(enfermedad="COVID-19"))
    print("\nDIAGNOSTICO IDENTIFICADO: COVID-19")
    print("RECOMENDACIÓN: Aislamiento, monitorear los niveles de oxigenación y realizarse la prueba de antígeno/PCR.")

@Rule(Sintoma(congestion_nasal=True, estornudos=True, tos_leve=True))
def regla_resfriado(self):
    """Ampliación 2: Resfriado Común"""
    self.declare(Diagnostico(enfermedad="Resfriado Común"))
    print("\nDIAGNOSTICO IDENTIFICADO: Resfriado Común")
    print("RECOMENDACIÓN: consumir bebidas calientes, mantenerse abrigado y mantener reposo")

@Rule(Sintoma(tos_persistente=True, flemas=True, dificultad_respiratoria=True))
def regla_bronquitis(self):
    """Ampliación 3: Bronquitis"""
    self.declare(Diagnostico(enfermedad="Bronquitis"))
    print("\nDIAGNOSTICO IDENTIFICADO: Bronquitis")
    print("RECOMENDACIÓN: Evitar irritantes del aire y acudir a eevaluación médica para prescripcion de tratamiento.")

@Rule(Sintoma(dolor_articular=True, erupcion_cutanea=True, fiebre=True))
def regla_dengue(self):
    """Ampliacion 4: Dengue"""
    self.declare(Diagnostico(enfermedad="Dengue"))
    print("\nDIAGNOSTICO IDENTIFICADO: Dengue")
    print("RECOMENDACIÓN: Acudir a urgencias inmediatamente para realizar biometría hemática. Guardar reposo absoluto e hidratación.")

#REGLA RESPALDO

@Rule(NOT(Diagnostico(enfermedad=MATCH.e)))
def regla_respaldo(self):
    """
    La regla respaldo se activa unicamente si no existe ningun diagnostico declarado
    en la memoria de trabajo.
    """
    print("\nATENCIÓN: No se pudo determinar un diagnostico especifico con los sintomas proporcionados.")
    print("RECOMENDACIÓN: Por favor consulte a un médico profesional para una valoración")

#PARTE 3_EJE2 Script de pruebas

def ejecutar_caso(nombre_caso, **sintomas):
    print("=" * 70)
    print(f"EJECUTANDO: {nombre_caso}")
    print(f"Sintomas ingresados: {sintomas}")
    print("=" * 70)

    engine = SistDiagnosticoMedico()
    engine.reset()
    engine.declare(Sintoma(**sintomas))
    print()

if __name__ == "__main__":
    # Caso 1: Gripe
    ejecutar_caso("Caso 1: Gripe", fiebre=True, tos=True, dolor_garganta=True)
    # Caso 2: Alergia
    ejecutar_caso("Caso 2: Alergia", estornudos=True, congestión_nasal=True, picazón_ojos=True)
    # Caso 3: Gastroenteritis
    ejecutar_caso("Caso 3: Gastroenteritis", dolorestomago=True, diarrea=True, vomito=True)
    # Caso 4: Sin diagnostico
    ejecutar_caso("Caso 4: Sin diagnostico", dolor_muscular=False, fatiga=False)

#CASO 5_EJE2: Conflicto de reglas (DIAGNOSTICOS MÚLTIPLES)

ejecutar_caso("Caso 5 / Ejercicio 2",
              fiebre=True, tos=True, dolor_garganta=True,
              estornudos=True, congestion_nasal=True, picazon_ojos=True)
