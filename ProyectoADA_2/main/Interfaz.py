from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
from MaxHeap import Polinomio

class PolinomioGUI(BoxLayout):
    def __init__(self, **kwargs):
        super(PolinomioGUI, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10
        self.polinomio = Polinomio()

        self.entrada = TextInput(
            multiline=False,
            size_hint_y=None,
            height=40,
            hint_text='Ingrese el polinomio'
        )
        self.add_widget(self.entrada)

        botones = BoxLayout(size_hint_y=None, height=40, spacing=10)
        botones.add_widget(Button(text='Agregar', on_press=self.agregar_polinomio))
        botones.add_widget(Button(text='Mostrar', on_press=self.mostrar_polinomio))
        botones.add_widget(Button(text='Ordenar', on_press=self.ordenar_polinomio))
        botones.add_widget(Button(text='Sumar Términos', on_press=self.sumar_terminos))
        self.add_widget(botones)

        self.resultado = TextInput(readonly=True, multiline=True)
        self.add_widget(self.resultado)

    def agregar_polinomio(self, instance):
        nuevo_polinomio = self.entrada.text
        if nuevo_polinomio:
            self.polinomio.agregar_al_final(nuevo_polinomio)
            self.entrada.text = ''
            self.actualizar_resultado()
            self.mostrar_mensaje('Éxito', 'Polinomio agregado correctamente')
        else:
            self.mostrar_mensaje('Error', 'Por favor ingrese un polinomio')

    def mostrar_polinomio(self, instance):
        self.actualizar_resultado()

    def ordenar_polinomio(self, instance):
        self.polinomio.organizar_heap()
        self.actualizar_resultado()
        self.mostrar_mensaje('Éxito', 'Polinomio ordenado correctamente')

    def sumar_terminos(self, instance):
        self.polinomio.sumar_mismos_grados()
        self.actualizar_resultado()
        self.mostrar_mensaje('Éxito', 'Términos sumados correctamente')

    def actualizar_resultado(self):
        resultado = str(self.polinomio)
        if self.polinomio.esta_ordenado:
            resultado += "\n(El polinomio está ordenado)"
        if self.polinomio.esta_sumado:
            resultado += "\n(Se han sumado los términos del mismo grado)"
        self.resultado.text = resultado

    def mostrar_mensaje(self, titulo, mensaje):
        # En una aplicación real, aquí implementaríamos un popup
        print(f"{titulo}: {mensaje}")

class PolinomioApp(App):
    def build(self):
        return PolinomioGUI()

if __name__ == '__main__':
    Window.size = (600, 400)
    PolinomioApp().run()