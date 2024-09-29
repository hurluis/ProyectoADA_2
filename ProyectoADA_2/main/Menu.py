from funcion_polinomio import Polinomio

class Menu:

    def __init__(self):
        self.polinomio = Polinomio()  
        self.mostrarMenu()

    def mostrarMenu(self):
        print("\n====================================================")
        print("BIENVENIDO A SU ORDENADOR MAXHEAP DE POLINOMIOS")
        print("====================================================\n")

        # Verificar si el polinomio está vacío
        if self.polinomio.cabeza is None:
            self.mostrarOpcionesListaVacia()
        else:
            self.mostrarOpcionesListaConElementos()
        self.mostrarMenu()

    def mostrarOpcionesListaVacia(self):
        print("La lista está vacía, por favor ingrese un término para comenzar.")

        try:
            print("1. Manual de uso.")
            print("2. Agregar un término a la lista.")
            seleccionarOpcion: int = int(input("\nIngresa tu opción: "))
            if seleccionarOpcion == 1:
                self.opcionSeleccionada1()
            elif seleccionarOpcion == 2:
                self.opcionSeleccionada2()
            else:
                print("\nINGRESA UN NÚMERO EN EL RANGO")
        except ValueError:
            print("\n INGRESA UNA OPCIÓN VÁLIDA!!! \n")
            self.mostrarOpcionesListaVacia()

    def mostrarOpcionesListaConElementos(self):
        try:
            print("1. Manual de uso.")
            print("2. Agregar un término a la lista.")
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
            else:
                print("\nINGRESA UN NÚMERO EN EL RANGO")
        except ValueError:
            print("\n INGRESA UNA OPCIÓN VÁLIDA!!! \n")
            self.mostrarOpcionesListaConElementos()

    def opcionSeleccionada1(self):
        print("\n================= Manual de uso =================")
        print("\n1. Siempre que la lista esté vacía, solo tendrás dos opciones: leer el manual o agregar un término.")
        print("\n2. Puedes agregar términos ingresando el coeficiente y el grado.")
        print("\n3. Después de ingresar términos, podrás ordenarlos y mostrarlos.")
        print("\n4. Disfruta el programa que ya sabes usar!")

    def opcionSeleccionada2(self):
        try:
            coef = int(input("Ingresa el coeficiente: "))
            grado = int(input("Ingresa el grado: "))
            self.polinomio.insertar(coef, grado)
            print(f"Término agregado: {coef}x^{grado}")
        except ValueError:
            print("Por favor, ingresa valores válidos.")
        self.mostrarMenu()

    def opcionSeleccionada3(self):
        print("\nOrdenando el polinomio...")
        self.polinomio.organizar_heap()
        print("Polinomio ordenado exitosamente.")
        self.mostrarMenu()

    def opcionSeleccionada4(self):
        print("\nPolinomio actual:")
        self.polinomio.imprimir()
        self.mostrarMenu()

        

menu = Menu()
menu