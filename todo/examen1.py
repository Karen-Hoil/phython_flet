import flet as ft
import random

def main(page: ft.Page):
    page.window_width = 850
    page.window_height = 850
    page.scroll_to = True
    page.window_title = "Juega piedra, papel o tijera!!!"

    op = ["piedra", "papel", "tijera"]
    computer = random.choice(op)

    a_text = ft.Text("Empataste contra la computadora", style=ft.TextThemeStyle.TITLE_LARGE)
    a_alter = ft.Text("Ambos escogieron lo mismo", style=ft.TextThemeStyle.TITLE_SMALL)

    b_text = ft.Text("Perdiste contra la computadora", style=ft.TextThemeStyle.TITLE_LARGE)
    b_alter = ft.Text("Tú escogiste piedra y la computadora papel", style=ft.TextThemeStyle.TITLE_SMALL)

    c_text = ft.Text("Ganaste contra la computadora", style=ft.TextThemeStyle.TITLE_LARGE)
    c_alter = ft.Text("Tú escogiste tijera y la computadora papel", style=ft.TextThemeStyle.TITLE_SMALL)

    d_text = ft.Text("Perdiste contra la computadora", style=ft.TextThemeStyle.TITLE_LARGE)
    d_alter = ft.Text("Tú escogiste tijera y la computadora piedra", style=ft.TextThemeStyle.TITLE_SMALL)

    e_text = ft.Text("Ganaste contra la computadora", style=ft.TextThemeStyle.TITLE_LARGE)
    e_alter = ft.Text("Tú escogiste papel y la computadora piedra", style=ft.TextThemeStyle.TITLE_SMALL)

    f_text = ft.Text("Perdiste contra la computadora", style=ft.TextThemeStyle.TITLE_LARGE)
    f_alter = ft.Text("Tú escogiste papel y la computadora tijera", style=ft.TextThemeStyle.TITLE_SMALL)

    g_text = ft.Text("Ganaste contra la computadora", style=ft.TextThemeStyle.TITLE_LARGE)
    g_alter = ft.Text("Tú escogiste piedra y la computadora tijera", style=ft.TextThemeStyle.TITLE_SMALL)

    a =ft.Column(
        controls=[a_text, a_alter],
        scroll=ft.ScrollMode.ALWAYS
    )
    b =ft.Column(
        controls=[b_text, b_alter],
        scroll=ft.ScrollMode.ALWAYS
    )
    c =ft.Column(
        controls=[c_text, c_alter],
        scroll=ft.ScrollMode.ALWAYS
    )
    d =ft.Column(
        controls=[d_text, d_alter],
        scroll=ft.ScrollMode.ALWAYS
    )
    e2 =ft.Column(
        controls=[e_text, e_alter],
        scroll=ft.ScrollMode.ALWAYS
    )
    f =ft.Column(
        controls=[f_text, f_alter],
        scroll=ft.ScrollMode.ALWAYS
    )
    g =ft.Column(
        controls=[g_text, g_alter],
        scroll=ft.ScrollMode.ALWAYS
    )
    
    a.visible=False
    b.visible=False
    c.visible=False
    d.visible=False
    e2.visible=False
    f.visible=False
    g.visible=False

    def calcularJuego(e):
        empate = (player.value == computer)
        perdistePapel = (computer == "papel" and player.value == "piedra")
        ganastePapel = (computer == "papel" and player.value == "piedra")
        perdistePiedra = (computer == "piedra" and player.value == "papel")
        ganastePiedra = (computer == "piedra" and player.value == "tijera")
        perdisteTijera = (computer == "tijera" and player.value == "papel")
        ganasteTijera = (computer == "tijera" and player.value == "piedra")

        if empate:
            a.visible= True
            page.update()
        elif perdistePapel:
            b.visible = True
            page.update()
        elif ganastePapel:
            c.visible = True
            page.update()
        elif perdistePiedra:
            d.visible= True
            page.update()
        elif ganastePiedra:
            e2.visible = True
            page.update()
        elif perdisteTijera:
            f.visible = True
            page.update()
        elif ganasteTijera:
            g.visible = True
            page.update()

        page.update()

    def limpiar(e):
        calcularJuego(e)
        r = ft.Text(f"{nombre.value} elegiste {player.value} y la computadora eligio {computer}", style=ft.TextThemeStyle.TITLE_LARGE)
        page.controls.append(r)
        nombre.value= ''
        player.value=''
        a.visible=False
        b.visible=False
        c.visible=False
        d.visible=False
        e2.visible=False
        f.visible=False
        g.visible=False
        page.update()


    nombre = ft.TextField(
            label="Nombre : ",
            expand= True)
    player = ft.TextField(
            label="Elige una opcion: piedra, papel o tijera",
            expand= True)
    
    btn_calcular = ft.ElevatedButton(
    text="Calcular",
    on_click= calcularJuego,
    bgcolor=ft.colors.BLUE_GREY_100,
    color=ft.colors.BLACK,
    expand=1,
    width=100,
    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), ),
    )
    btn_guardar = ft.ElevatedButton(
    text="Guardar",
    on_click= limpiar,
    bgcolor=ft.colors.BLUE_GREY_100,
    color=ft.colors.BLACK,
    expand=1,
    width=100,
    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), ),
    )
    r1= ft.Row(
        controls=[nombre]
    )
    r2= ft.Row(
        controls=[player]
    )
    r3= ft.Row(
        controls=[btn_calcular, btn_guardar]
    )



    page.add(
        r1,
        r2,
        r3
    )
    page.add(
        
        ft.Text(
            spans=[
                ft.TextSpan(
                    "Juega piedra, papel o tijera!!!",
                    ft.TextStyle(
                        size=20,
                        weight=ft.FontWeight.BOLD
                    ),
                ),
            ],
        )
    )
    page.add(
        a,
        b,
        c,
        d,
        e2,
        f,
        g
    )
ft.app(target=main)
        