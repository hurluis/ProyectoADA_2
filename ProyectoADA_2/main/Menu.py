from MaxHeap import Polinomio

class Menu:

    def __init__(self):
        self.polinomio = Polinomio()  
        self.mostrarMenu()

    def mostrarMenu(self):
        while True:
            print("\n====================================================")
            print("BIENVENIDO A SU ORDENADOR MAXHEAP DE POLINOMIOS")
            print("====================================================\n")

            # Verificar si el polinomio está vacío
            if self.polinomio.esta_vacio():
                self.mostrarOpcionesListaVacia()
            else:
                self.mostrarOpcionesListaConElementos()

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

    def mostrarOpcionesListaConElementos(self):
        try:
            print("1. Manual de uso.")
            print("2. Agregar un término a la lista.")
            print("3. Ordenar lista.")
            print("4. Mostrar lista.")
            print("5. Sumar términos del mismo grado.")  
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
            else:
                print("\nINGRESA UN NÚMERO EN EL RANGO")
        except ValueError:
            print("\n INGRESA UNA OPCIÓN VÁLIDA!!! \n")

    def opcionSeleccionada1(self):
        print("\n================= Manual de uso =================")
        print("\n1. Siempre que la lista este vacia, iniciara solo dos opciones, leer el manual o agregar un elemento. ")
        print("\n=======================================================================================================")
        print("\n2. Cada vez que le hunda en agregar, puede ponerle un polinomio, o un solo término")
        print("\n=======================================================================================================")
        print("\n3. Una vez haya ingresado los valores, saldrá otro menú más completo, contará con las mismas dos opciones,")
        print("además habilitará el mostrar la lista, ordenar la lista y sumar los elementos del mismo grado. ")
        print("\n=======================================================================================================")
        print("\n4. Disfruta el programa que ya lo sabes usar!")

    def opcionSeleccionada2(self):
        try:
            print("\n================= Ingreso de polinomio o término =================")
            polinomio = input("Ingresa el polinomio: ")
            self.polinomio.agregar_al_final(polinomio)
            print(f"\nPolinomio agregado con éxito: {polinomio}")
        except Exception as e:
            print(f"\nPOR FAVOR, INGRESA VALORES VÁLIDOS. Error: {str(e)}")

    def opcionSeleccionada3(self):
        print("\nOrdenando el polinomio...")
        self.polinomio.organizar_heap()
        print("\nPolinomio ordenado exitosamente.")
        print("\n==================================")

    def opcionSeleccionada4(self):
        print("\n================= Polinomio actual =================")
        self.polinomio.imprimir_polinomio()
        if self.polinomio.esta_ordenado:
            print("(El polinomio está ordenado)")
        if self.polinomio.esta_sumado:
            print("(Se han sumado los términos del mismo grado)")

    def opcionSeleccionada5(self):
        print("\n================= Simplificación de polinomio =================")
        print("\nSumando términos del mismo grado...")
        self.polinomio.sumar_mismos_grados()
        print("\nSuma completada. El polinomio ha sido simplificado.")

menu = Menu()
menu