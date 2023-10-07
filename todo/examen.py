import flet as ft
from random import randint

def main(page: ft.Page):
        def limpiar(e):
            r = ft.Text(f"Nombre: {nombre.value} Opcion elejida: {player}", style=ft.TextThemeStyle.TITLE_LARGE)
            page.controls.append(r)
            nombre.value = ""
            player.value=""
            page.update()

        nombre = ft.TextField(hint_text="ingresa tu nombre")
        player = ft.TextField(hint_text="Escoge piedra, papel o tijera")
        
        btn_calcular = ft.ElevatedButton(
        text="Ejecutar",
        bgcolor=ft.colors.BLUE_GREY_100,
        color=ft.colors.BLACK,
            expand=1,
        on_click= ejecutar,
        width=100,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), ),
        )
        btn_guardar = ft.ElevatedButton(
        text="Guardar",
        bgcolor=ft.colors.BLUE_GREY_100,
        color=ft.colors.BLACK,
        expand=1,
        on_click= limpiar,
        width=100,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), ),
        )

        def ejecutar(e):
            op = ["Piedra", "Papel", "Tijera"]
            computer = op[randint(0,2)]
            if player == computer:
                    a = ft.Text("Empate", style=ft.TextThemeStyle.TITLE_LARGE)
            elif player == "Piedra":
                    if computer == "Papel":
                        b =ft.Text("Perdiste! ", computer, " > ", player)
                    else:
                        c =ft.Text("Ganaste !", player, " < ", computer)
            elif player == "Papel":
                    if computer == "Tijera":
                        d =ft.Text("Perdiste! ", computer, " > ", player)
                    else:
                        e =ft.Text("Ganaste! ", player, " < ", computer)
            elif player == "Tijera":

                    if computer == "Piedra":

                        f =ft.Text("Perdiste! ", computer, " > ", player)

                    else:
                        g =ft.Text("Ganaste! ", player, " < ", computer)
            else:
                    h =ft.Text("Error - Opción no valida, Intenta escribir las opciones como las vez.")

            page.update()    

        
        


        page.add(
            nombre,
            player,
            btn_calcular,
            btn_guardar
        )

ft.app(target=main)
