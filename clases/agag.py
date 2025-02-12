class Paciente:
    def __init__(self, nombre: str, edad: int, enfermedad: str):

        self.nombre = nombre
        self.edad = edad
        self.__enfermedad = enfermedad 

    def get_enfermedad(self) -> str:
        return self.__enfermedad

    def set_enfermedad(self, nueva_enfermedad: str):
        self.__enfermedad = nueva_enfermedad

    def __str__(self) -> str:
        return f"Paciente: {self.nombre}, Edad: {self.edad}"


class Hospital:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.pacientes = []

    def registrar_paciente(self, paciente: Paciente):
        self.pacientes.append(paciente)
        print(f"Paciente '{paciente.nombre}' registrado en {self.nombre}.")

    def listar_pacientes(self):
        if self.pacientes:
            print("Lista de pacientes registrados:")
            for paciente in self.pacientes:
                print(paciente)
        else:
            print("No hay pacientes registrados.")

    def buscar_paciente(self, nombre: str) -> Paciente:
        for paciente in self.pacientes:
            if paciente.nombre.lower() == nombre.lower():
                return paciente
        return None

    def mostrar_informacion_medica(self, nombre: str):
        paciente = self.buscar_paciente(nombre)
        if paciente:
            print(f"Información médica de {paciente.nombre}:")
            print(f"\nEnfermedad: {paciente.get_enfermedad()}")
        else:
            print("Paciente no encontrado.")


if __name__ == "__main__":
    hospital = Hospital("Clínica Central")

    # Crear algunos pacientes
    paciente1 = Paciente("Pepe Pérez", 30, "Gripe")
    paciente2 = Paciente("María López", 45, "Hipertensión")
    paciente3 = Paciente("Carlos Ruiz", 50, "Diabetes")

    hospital.registrar_paciente(paciente1)
    hospital.registrar_paciente(paciente2)
    hospital.registrar_paciente(paciente3)

    hospital.listar_pacientes()

    nombre_busqueda = "María López"
    paciente_encontrado = hospital.buscar_paciente(nombre_busqueda)
    if paciente_encontrado:
        print(f"\nPaciente encontrado: {paciente_encontrado}")
    else:
        print("\nPaciente no encontrado.")

    print()
    hospital.mostrar_informacion_medica("Pepe Pérez")
