import flet as ft
import random

def main(page: ft.Page):
    page.window_width = 850
    page.window_height = 850
    page.scroll_to = True
    page.window_title = "Juega piedra, papel o tijera!!!"


    nombre = ft.TextField(
            label="Nombre : ",
            width=600)
    player = ft.TextField(
            label="Elige una opcion: piedra, papel o tijera",
            width=600)
    
    btn_calcular = ft.ElevatedButton(
    text="Calcular",
    on_click= calcular,
    bgcolor=ft.colors.BLUE_GREY_100,
    color=ft.colors.BLACK,
    width=100,
    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), ),
    )
    btn_guardar = ft.ElevatedButton(
    text="Guardar",
    on_click= limpiar,
    bgcolor=ft.colors.BLUE_GREY_100,
    color=ft.colors.BLACK,
    width=100,
    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), ),
    )

    a_text = ft.Text(f"{nombre} empataste contra la computadora", style=ft.TextThemeStyle.TITLE_LARGE)
    a_alter = ft.Text("Ambos escogieron lo mismo", style=ft.TextThemeStyle.TITLE_SMALL)

    b_text = ft.Text(f"{nombre} perdiste contra la computadora", style=ft.TextThemeStyle.TITLE_LARGE)
    b_alter = ft.Text(f"Tú escogiste {player} y la computadora papel", style=ft.TextThemeStyle.TITLE_SMALL)

    c_text = ft.Text(f"{nombre} ganaste contra la computadora", style=ft.TextThemeStyle.TITLE_LARGE)
    c_alter = ft.Text(f"Tú escogiste {player} y la computadora papel", style=ft.TextThemeStyle.TITLE_SMALL)

    d_text = ft.Text(f"{nombre} perdiste contra la computadora", style=ft.TextThemeStyle.TITLE_LARGE)
    d_alter = ft.Text(f"Tú escogiste {player} y la computadora piedra", style=ft.TextThemeStyle.TITLE_SMALL)

    e_text = ft.Text(f"{nombre} ganaste contra la computadora", style=ft.TextThemeStyle.TITLE_LARGE)
    e_alter = ft.Text(f"Tú escogiste {player} y la computadora piedra", style=ft.TextThemeStyle.TITLE_SMALL)

    f_text = ft.Text(f"{nombre} perdiste contra la computadora", style=ft.TextThemeStyle.TITLE_LARGE)
    f_alter = ft.Text(f"Tú escogiste {player} y la computadora tijera", style=ft.TextThemeStyle.TITLE_SMALL)

    g_text = ft.Text(f"{nombre} ganaste contra la computadora", style=ft.TextThemeStyle.TITLE_LARGE)
    g_alter = ft.Text(f"Tú escogiste {player} y la computadora tijera", style=ft.TextThemeStyle.TITLE_SMALL)

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
    e =ft.Column(
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
    e.visible=False
    f.visible=False
    g.visible=False


    r1= ft.Row(
        controls=[nombre]
    )
    r2= ft.Row(
        controls=[player]
    )
    r3= ft.Row(
        controls=[btn_calcular, btn_guardar]
    )

    def calcular(e):
        op = ["piedra", "papel", "tijera"]
        computer = random.choice(op)

        empate = (player == computer)
        perdistePapel = (computer == 'papel' and player == 'piedra')
        ganastePapel = (computer == 'papel' and player == 'tijera')
        perdistePiedra = (computer == 'piedra' and player == 'papel')
        ganastePiedra = (computer == 'piedra' and player == 'tijera')
        perdisteTijera = (computer == 'tijera' and player == 'papel')
        ganasteTijera = (computer == 'tijera' and player == 'piedra')

        if empate:
            a.visible = True
            page.update()
        elif perdistePapel:
            b.visible = True
            page.update()
        elif ganastePapel:
            c.visible = True
            page.update()
        elif perdistePiedra:
            d.visible = True
            page.update()
        elif ganastePiedra:
            e.visible = True
            page.update()
        elif perdisteTijera:
            f.visible = True
            page.update()
        elif ganasteTijera:
            g.visible = True
            page.update()
        
        page.update()

    def limpiar(e):
        r = ft.Text(f"Nombre: {nombre} Elección: {player}", style=ft.TextThemeStyle.TITLE_LARGE)
        page.controls.append(r)
        player.value=''
        a.visible=False
        b.visible=False
        c.visible=False
        d.visible=False
        e.visible=False
        f.visible=False
        g.visible=False
        page.update()

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
        e,
        f,
        g
    )
ft.app(target=main)
        