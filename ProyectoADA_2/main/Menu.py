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
            if self.polinomio.cabeza is None:
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
                # Aquí verificamos si ya tiene elementos y cambiamos al menú correcto
                if self.polinomio.cabeza is not None:
                    print("\nTérmino agregado, ahora la lista tiene elementos.")
                    # Ya no es necesario volver a llamar al menú, el bucle seguirá solo
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

    def opcionSeleccionada1(self):
        print("\n================= Manual de uso =================")
        print("\n1. Siempre que la lista esté vacía, solo tendrás dos opciones: leer el manual o agregar un término.")
        print("\n2. Puedes agregar términos ingresando el coeficiente y el grado.")
        print("\n3. Después de ingresar términos, podrás ordenarlos y mostrarlos.")
        print("\n4. Disfruta el programa que ya sabes usar!")

    def opcionSeleccionada2(self):
        try:
            polinomio = (input("Ingresa el polinomio: "))
            listas_por_grado = self.polinomio.dividir_polinomio(polinomio)

            # Reconstruir y asignar el polinomio dividido a la lista actual
            self.polinomio = self.polinomio.reconstruir_polinomio(listas_por_grado)
            print(f"Polinomio agregado con éxito: {polinomio}")
        except AttributeError:
            print("\nPOR FAVOR, INGRESA VALORES VÁLIDOS.")

    def opcionSeleccionada3(self):
        print("\nOrdenando el polinomio...")
        self.polinomio.organizar_heap()
        print("Polinomio ordenado exitosamente.")

    def opcionSeleccionada4(self):
        print("\nPolinomio actual:")
        self.polinomio.imprimir()

menu = Menu()
menu