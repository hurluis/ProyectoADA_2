from Max_heap import Maxheap


class Menu:

    def __init__(self):
        self.Maxheap = Maxheap()

        self.mostrarMenu()
        

    def mostrarMenu(self):
        print("\n====================================================")
        print("BIENVENIDO A SU ORDENADOR MAXHEAP")
        print("====================================================\n")
        if self.Maxheap.length == 0:
            self.mostrarOpcionesListaVacia()
        elif self.Maxheap.length > 0:
            self.mostrarOpcionesListaConElementos()
        self.mostrarMenu()

    def mostrarOpcionesListaVacia(self):    

        try:   
            print("1. Manual de uso.")
            print("2. Agregar un termino a la lista.")
            seleccionarOpcion: int = int(input("\nIngresa tu opción: "))
            if seleccionarOpcion == 1:
                self.opcionSeleccionada1()
            if seleccionarOpcion == 2:
                self.opcionSeleccionada2()
            else:
                print("\nINGRESA UN NÚMERO EN EL RANGO")
        except:    
            print("\n INGRESA UNA OPCIÓN VÁLIDA!!! \n")
            self.mostrarOpcionesListaVacia()
    
    def mostrarOpcionesListaConElementos(self):
        try:
            print("1. Manual de uso.")
            print("2. Agregar un termino a la lista.")
            print("3. Ordenar lista.")
            print("4. Mostrar lista.")
            seleccionarOpcion: int = int(input("\nIngresa tu opción: "))

            if seleccionarOpcion == 1:
                self.opcionSeleccionada1()
            elif seleccionarOpcion == 2:
                self.opcionSeleccionada2()
            elif seleccionarOpcion == 3:
                self.opcionSeleccionada3()
            elif seleccionarOpcion == 4:
                self.opcionSeleccionada4()
            elif seleccionarOpcion == 5:
                self.opcionSeleccionada5()
            elif seleccionarOpcion == 6:
                self.opcionSeleccionada6()
            else:
                print("\nINGRESA UN NÚMERO EN EL RANGO")
        except:
            print("\n INGRESA UNA OPCIÓN VÁLIDA!!! \n")
            self.mostrarOpcionesListaConElementos()
    #No valida cuando hay un repetido y aun asi lo agrega(el repetido se comprueba por el numero unico)
    def opcionSeleccionada1(self):
        print("\n================= Manual de uso =================")
        print("\n1. Siempre que la lista este vacia, iniciara solo dos opciones, leer el manual o agregar un elemento. ")
        print("\n=======================================================================================================")
        print("\n2. Cada vez que vaya a ingresar un elemento, solo podrá ingresar un término a la vez, se le")
        print("pedirán 2 datos, el coheficiente, y el grado de la X, ejemplo: \n")
        print("si  ingresa en coheficiente: -4. ")
        print("si  ingresa en grado: 2. ")
        print("lo que queda es: -4X^2. ")
        print("\n=======================================================================================================")
        print("\n3. Una vez haya ingresado el término, saldrá otro menú más completo, contará con las mismas dos opciones,")
        print("además habilitará el mostrar la lista y ordenar la lista. ")
        print("\n=======================================================================================================")
        print("\n4. Disfruta el programa que ya lo sabes usar!")


    def opcionSeleccionada2(self):
        print("\n================= Agregar un paciente al hospital =================")
        AgregarPaciente = Registrar(self.hospital)
        AgregarPaciente.agregarPaciente()

    def opcionSeleccionada2(self):
        print("\n================= Siguiente paciente en espera =================")

        MostrarPaciente = Mostrar(self.hospital)
        MostrarPaciente.mostrarPaciente()
    

    def opcionSeleccionada3(self):
        print("\n================= Vamos a atender a un paciente =================")

        AtenderPaciente = Atender(self.hospital)
        AtenderPaciente.atenderPaciente()


#DE ACA PARA ABAJO SON LOS QUE FALTAN

    #se escribe en mostrar
    def opcionSeleccionada4(self):
        print("\n================= Consultemos los pacientes del hospital =================")
        Mostrarhospital = Mostrar(self.hospital)
        Mostrarhospital.mostrarHospital()
    #se escribe en mostrar
    
    def opcionSeleccionada5(self):
        print("\n================= Consultemos los pacientes por triaje =================")
        Triaje = int(input("Ingrese el Triaje a consultar"))      
        Mostrarportriaje = Mostrar(self.hospital)
        Mostrarportriaje.mostrarTriaje(Triaje)

    #Este se escribe en el modulo Eliminar
    def opcionSeleccionada6(self):
        print("\n================= Retiremos un paciente del hospital =================")
        numeroPaciente: int = int(input("Ingresa el identificador único del paciente: "))

        EliminaPaciente = Eliminar(self.hospital)
        EliminaPaciente.eliminar_paciente(numeroPaciente)

   
        
        

menu = Menu()
menu