from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Ejercicio 1
Alumno: Nombre, Apellido
Division: Div J

'''


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_agregar = customtkinter.CTkButton(
            master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=0, column=0, pady=10, padx=10)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, column=0, pady=10, padx=10)

        self.lista_de_nombres = ["Juan", "María", "Pedro", "Laura",
                                 "Carlos", "Ana", "Luis", "Elena", "Miguel", "Sofía"]
        self.lista_plato_principal = ["Pizza", "Hamburguesa", "Ensalada", "Pizza",
                                      "Hamburguesa", "Ensalada", "Pizza", "Hamburguesa", "Ensalada", "Pizza"]
        self.lista_cantidad_de_platos = [2, 1, 3, 2, 2, 4, 3, 1, 1, 3]
        self.lista_bebidas_elegidas = [
            "Refresco", "Agua", "Jugo", "Refresco", "Agua", "Jugo", "Refresco", "Agua", "Jugo", "Refresco"]
        self.lista_cantidad_de_bebidas = [2, 1, 5, 3, 2, 5, 1, 2, 1, 3]

    def btn_agregar_on_click(self):
        pregunta = True

        while pregunta == True:
            nombre_del_amigo = prompt(
                title="Nombre", prompt="Ingrese el nombre del amigo")

            plato_elegido = prompt(
                title="Plato", prompt="Ingrese el nombre del plato elegido 'Pizza', 'Hamburguesa', 'Ensalada'")

            while plato_elegido != "Ensalada" and plato_elegido != "Pizza" and plato_elegido != "Hamburguesa":
                plato_elegido = prompt(
                    title="Plato", prompt="Error! Ingrese el nombre del plato elegido 'Pizza', 'Hamburguesa', 'Ensalada'")

            cantidad_plato = prompt(
                title="Cantidad_plato", prompt="Ingrese la cantidad del plato ingresado")
            cantidad_plato = int(cantidad_plato)

            while cantidad_plato < 1:
                cantidad_plato = prompt(
                    title="Cantidad_plato", prompt="Error!! Ingrese la cantidad del plato ingresado")
                cantidad_plato = int(cantidad_plato)

            bebida_elegida = prompt(
                title="Plato", prompt="Ingrese el nombre del bebida elegido 'Refresco', 'Agua', 'Jugo' ")

            while bebida_elegida != "Jugo" and bebida_elegida != "Agua" and bebida_elegida != "Refresco":
                bebida_elegida = prompt(
                    title="bebida", prompt="Error! Ingrese el nombre del bebida elegido 'Refresco', 'Agua', 'Jugo'")

            cantidad_bebida = prompt(
                title="cantidad_bebida", prompt="Ingrese la cantidad del bebida ingresado")
            cantidad_bebida = int(cantidad_bebida)

            while cantidad_bebida < 1:
                cantidad_bebida = prompt(
                    title="cantidad_bebida", prompt="Error!! Ingrese la cantidad del bebida ingresado")
                cantidad_bebida = int(cantidad_bebida)

            self.lista_de_nombres.append(nombre_del_amigo)
            self.lista_plato_principal.append(plato_elegido)
            self.lista_cantidad_de_platos.append(cantidad_plato)
            self.lista_bebidas_elegidas.append(bebida_elegida)
            self.lista_cantidad_de_bebidas.append(cantidad_bebida)

            pregunta = question(
                title="Ingreso", message="Quiere seguir ingresando")

    def btn_mostrar_on_click(self):
        PRECIO_UNITARIO_PLATO = 800
        PRECIO_UNITARIO_BEBIDA = 200
        largo_lista_nombres = len(self.lista_de_nombres)
        total_gastado = 0
        total_gastado_jugo = 0
        cont_compraron_jugo = 0
        acum_platos_hamburguesa = 0
        acum_platos_ensalada = 0
        acum_platos_pizza = 0
        lista_nombres_ensalada = []  # 2
        lista_nombres_amigos_mas_siete_pedidos = []  # 7
        # bandera_del_primero = True

        for indice in range(largo_lista_nombres):
            nombre = self.lista_de_nombres[indice]
            plato_elegido = self.lista_plato_principal[indice]
            cantidad_platos = self.lista_cantidad_de_platos[indice]
            bebida_elegida = self.lista_bebidas_elegidas[indice]
            cantidad_bebidas = self.lista_cantidad_de_bebidas[indice]

            cantidad_total_pedidos = cantidad_bebidas + cantidad_platos
            costo_bebida = PRECIO_UNITARIO_BEBIDA * cantidad_bebidas
            costo_plato = PRECIO_UNITARIO_PLATO * cantidad_platos

            # print(f"en el indice {indice} tengo el nombre {nombre}, plato {plato_elegido}, cantidad plato {cantidad_platos}, bebida {bebida_elegida}, cant bebida {cantidad_bebidas}\nCosto B {costo_bebida}, costo plato {costo_plato}")

            if (bebida_elegida == "Jugo"):
                total_gastado_jugo += costo_bebida
                cont_compraron_jugo += 1

            match(plato_elegido):
                case "Hamburguesa":
                    acum_platos_hamburguesa += cantidad_platos
                case "Pizza":
                    acum_platos_pizza += cantidad_platos
                case _:
                    lista_nombres_ensalada.append(nombre)
                    acum_platos_ensalada += cantidad_platos

            total_gastado = total_gastado + costo_bebida + costo_plato

            if (indice == 0 or cantidad_total_pedidos > max_cantidad_total_pedidos):
                max_cantidad_total_pedidos = cantidad_total_pedidos
                max_nombre_amigo = nombre

            if (cantidad_total_pedidos > 7):
                lista_nombres_amigos_mas_siete_pedidos.append(nombre)

            # if (bandera_del_primero == True or cantidad_total_pedidos > max_cantidad_total_pedidos):
            #     max_cantidad_total_pedidos = cantidad_total_pedidos
            #     max_nombre_amigo = nombre
            #     bandera_del_primero = False

        propina_sugerida = total_gastado * 10 / 100
        total_gastado = total_gastado + propina_sugerida

        # ========================A===============================
        print(f"A El total gastado es {total_gastado}")
        print(f"A Propina sugerida {propina_sugerida}")

        # ========================B==============================
        if (cont_compraron_jugo > 0):
            promedio_gasto_jugo = total_gastado_jugo / cont_compraron_jugo
            print(
                f"B compraron jugo {cont_compraron_jugo}, gastaron en total {total_gastado_jugo} , el promedio es {promedio_gasto_jugo:.2f}")
        else:
            print("No se vendio jugo")

        # ========================C=============================

        total_platos = acum_platos_pizza + acum_platos_ensalada + acum_platos_hamburguesa
        procentaje_platos_pizza = acum_platos_pizza / total_platos * 100
        procentaje_platos_ensalada = acum_platos_ensalada / total_platos * 100
        procentaje_platos_hamburguesa = acum_platos_hamburguesa / total_platos * 100

        print(f"C [{procentaje_platos_pizza:.2f}% pizza, {procentaje_platos_ensalada:.2f}% ensaladas, {procentaje_platos_hamburguesa:.2f}% hamburguesas] ")

        # ========================D============================

        print(
            f"D El nombre del amigo premiado es {max_nombre_amigo}, total pedidos es {max_cantidad_total_pedidos}")

        # ========================E============================

        print("El punto 2 es {0}".format(lista_nombres_ensalada))
        print("El punto 7 es {0}".format(
            lista_nombres_amigos_mas_siete_pedidos))


print(__name__)
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
