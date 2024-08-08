import energias.modelo_energias as md_energias

class Acciones_Energias:

    def obtenerTablas():

        return None
    """
    def agregar(self):
        print("\nOK!! Vamos a registrarte en el sistema...")
    
        # Input (Campos)
        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email= input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        # Model (Modelo)
        energias = md_energias.Modelo_Energias(nombre, apellidos, email, password)

        # Register (Registrar)
        registro = energias.registrar()

        # Validate (Validar)
        if registro[0] >= 1:
            print(f"\nSe registraron todos los datos de energias!!")
        else:
            print("\nNo te has registrado correctamente!!")
    """