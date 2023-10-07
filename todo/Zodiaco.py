import flet as ft


def main(page:ft.Page):
    page.window_width = 850
    page.window_height = 850
    page.scroll_to = True
    page.window_title = "Calcula tu signo zodiacal"

  
    
    sAries = ft.Text("Tu simbolo Zodiacal es : Aries", style=ft.TextThemeStyle.TITLE_LARGE)
    sFechaAries = ft.Text("Las personas que nacen del 21 de Marzo al 20 de Abril", style=ft.TextThemeStyle.TITLE_SMALL)
    
    sTauro = ft.Text("Tu simbolo Zodiacal es : Tauro", style=ft.TextThemeStyle.TITLE_LARGE)
    sFechaTauro= ft.Text("Las personas que nacen del del 21 de Abril al 20 de Mayo", style=ft.TextThemeStyle.TITLE_SMALL) 
    
    sGeminis = ft.Text("Tu simbolo Zodiacal es : !Geminis", style=ft.TextThemeStyle.TITLE_LARGE)
    sFechaGeminis = ft.Text("Las personas que nacen del del 21 de Mayo al 20 de Junio", style=ft.TextThemeStyle.TITLE_SMALL)
    
    sCancer = ft.Text("Tu simbolo Zodiacal es : Cancer", style=ft.TextThemeStyle.TITLE_LARGE)
    sFechaCancer = ft.Text("Las personas que nacen del 21 de Junio al 20 de Julio", style=ft.TextThemeStyle.TITLE_SMALL)
    
    sLeo = ft.Text("Tu simbolo Zodiacal es : Leo", style=ft.TextThemeStyle.TITLE_LARGE)
    sFechaLeo = ft.Text("Las personas que nacen del 21 de Julio al 20 de Agosto", style=ft.TextThemeStyle.TITLE_SMALL)
    
    sVirgo = ft.Text("Tu simbolo Zodiacal es : Acuario", style=ft.TextThemeStyle.TITLE_LARGE)
    sFechaVirgo = ft.Text("Las personas que nacen del 21 de Agosto al 20 de Septiembre", style=ft.TextThemeStyle.TITLE_SMALL) 
    
    sLibra = ft.Text("Tu simbolo Zodiacal es : Libra", style=ft.TextThemeStyle.TITLE_LARGE)
    sFechaLibra = ft.Text("Las personas que nacen del 21 de Septiembre al 20 de Octubre", style=ft.TextThemeStyle.TITLE_SMALL)
    
    sEscorpio = ft.Text("Tu simbolo Zodiacal es : Escorpio", style=ft.TextThemeStyle.TITLE_LARGE)
    sFechaEscorpio = ft.Text("Las personas que nacen del 21 de Octubre al 20 de Noviembre", style=ft.TextThemeStyle.TITLE_SMALL)
    
    sSagitario = ft.Text("Tu simbolo Zodiacal es : Sagitario", style=ft.TextThemeStyle.TITLE_LARGE)
    sFechaSagitario  = ft.Text("Las personas que nacen del 21 de Noviembre al 20 de Diciembre", style=ft.TextThemeStyle.TITLE_SMALL)
    
    sCapricornio = ft.Text("Tu simbolo Zodiacal es : Capricornio", style=ft.TextThemeStyle.TITLE_LARGE)
    sFechaCapricornio = ft.Text("Las personas que nacen del 21 de Diciembre al 20 de Enero", style=ft.TextThemeStyle.TITLE_SMALL) 
    
    sAcuario = ft.Text("Tu simbolo Zodiacal es : Acuario", style=ft.TextThemeStyle.TITLE_LARGE)
    sFechaAcuario = ft.Text("Las personas que nacen del 21 de Enero al 20 de Febrero", style=ft.TextThemeStyle.TITLE_SMALL)
    
    sPiscis = ft.Text("Tu simbolo Zodiacal es : Piscis", style=ft.TextThemeStyle.TITLE_LARGE)
    sFechaPiscis = ft.Text("Las personas que nacen del 21 de Febrero al 20 de Marzo", style=ft.TextThemeStyle.TITLE_SMALL)
    
    aries =ft.Column(
        controls=[sAries, sFechaAries],
         scroll=ft.ScrollMode.ALWAYS
    )
    tauro =ft.Column(
        controls=[sTauro, sFechaTauro],
        scroll=ft.ScrollMode.ALWAYS
    )
    geminis =ft.Column(
        controls=[sGeminis, sFechaGeminis],
         scroll=ft.ScrollMode.ALWAYS
    )
    cancer =ft.Column(
        controls=[sCancer, sFechaCancer],
         scroll=ft.ScrollMode.ALWAYS
    )
    leo =ft.Column(
        controls=[sLeo, sFechaLeo],
        scroll=ft.ScrollMode.ALWAYS
    )
    virgo =ft.Column(
        controls=[sVirgo, sFechaVirgo],
        scroll=ft.ScrollMode.ALWAYS
    )
    libra =ft.Column(
        controls=[sLibra, sFechaLibra],
        scroll=ft.ScrollMode.ALWAYS
    )
    escorpio =ft.Column(
        controls=[sEscorpio, sFechaEscorpio],
        scroll=ft.ScrollMode.ALWAYS
    )
    sagitario =ft.Column(
        controls=[sSagitario, sFechaSagitario],
        scroll=ft.ScrollMode.ALWAYS
    )
    capricornio =ft.Column(
        controls=[sCapricornio, sFechaCapricornio],
        scroll=ft.ScrollMode.ALWAYS
    )
    acuario =ft.Column(
        controls=[sAcuario, sFechaAcuario],
        scroll=ft.ScrollMode.ALWAYS
    )
    piscis =ft.Column(
        controls=[sPiscis, sFechaPiscis],
        scroll=ft.ScrollMode.ALWAYS
    )
    
    aries.visible = False
    tauro.visible = False
    geminis.visible = False
    cancer.visible = False
    leo.visible = False
    virgo.visible = False
    libra.visible = False
    escorpio.visible = False
    sagitario.visible = False
    capricornio.visible = False
    acuario.visible = False
    piscis.visible = False
    
    def calcularSigno(e):
        dia = int(inputDia.value)
        mes = int(inputMes.value)
        year = int(inputYear.value)
        
        Aries = (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20)
        Tauro = (mes == 4 and dia >= 21) or (mes == 5 and dia <= 20)
        Geminis = (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20)
        Cancer = (mes == 6 and dia >= 21) or (mes == 7 and dia <= 20)
        Leo = (mes == 7 and dia >= 21) or (mes == 8 and dia <= 20)
        Virgo = (mes == 8 and dia >= 21) or (mes == 9 and dia <= 20)
        Libra = (mes == 9 and dia >= 21) or (mes == 10 and dia <= 20)
        Escorpio = (mes == 10 and dia >= 21) or (mes == 11 and dia <= 20)
        Sagitario = (mes == 11 and dia >= 21) or (mes == 12 and dia <= 20)
        Capricornio = (mes == 12 and dia >= 21) or (mes == 1 and dia <= 20)
        Acuario = (mes == 1 and dia >= 21) or (mes == 2 and dia <= 20)
        Piscis = (mes == 2 and dia >= 21) or (mes == 3 and dia <= 20)
        
        if Aries:
            aries.visible = True
            page.update()
        elif Tauro:
            tauro.visible = True
            page.update()
        elif Geminis:
            geminis.visible = True
            page.update()
        elif Cancer:
            cancer.visible = True
            page.update()
        elif Leo:
            leo.visible = True
            page.update()
        elif Virgo:
            virgo.visible = True
            page.update()
        elif Libra:
            libra.visible = True
            page.update()
        elif Escorpio:
            escorpio.visible = True
            page.update()
        elif Sagitario:
            sagitario.visible = True
            page.update()
        elif Capricornio:
            capricornio.visible = True
            page.update()
        elif Acuario:
            acuario.visible = True
            page.update()
        elif Piscis:
            piscis.visible = True
            page.update()
                
        page.update()
    
    def limpiar(e):
        r = ft.Text(f"Nombre: {inputN.value} Dia: {inputDia.value} Mes: {inputMes.value} Año: {inputYear.value}", style=ft.TextThemeStyle.TITLE_LARGE)
        page.controls.append(r)
        inputDia.value = ""
        inputMes.value = ""
        inputYear.value = ""
        aries.visible = False
        tauro.visible = False
        geminis.visible = False
        cancer.visible = False
        leo.visible = False
        virgo.visible = False
        libra.visible = False
        escorpio.visible = False
        sagitario.visible = False
        capricornio.visible = False
        acuario.visible = False
        piscis.visible = False
        page.update()
        
        
    inputN = ft.TextField(
            label="Nombre : ",
            width=600)
    inputDia = ft.TextField(
            label="Dia de nacimiento (en formato numerico) : ",
            width=200)
    inputMes = ft.TextField(
            label="Mes de nacimiento (en formato numerico)  : ", 
            width=200)
    inputYear = ft.TextField(
            label="Año de nacimiento (en formato numerico) : ",
            width=200)
    
    btn_calcular = ft.ElevatedButton(
    text="Calcular",
    bgcolor=ft.colors.BLUE_GREY_100,
    color=ft.colors.BLACK,
    expand=1,
    on_click= calcularSigno,
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
    
    r1= ft.Row(
        controls=[inputN]
    )
    r2= ft.Row(
        controls=[inputDia, inputMes, inputYear]
    )
    r3= ft.Row(
        controls=[btn_calcular, btn_guardar]
    )
    page.add(
        
        ft.Text(
            spans=[
                ft.TextSpan(
                    "Calcula tu signo zodiacal",
                    ft.TextStyle(
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        foreground=ft.Paint(
                            gradient=ft.PaintLinearGradient(
                                (0, 20), (150, 20), [ft.colors.BLUE_GREY_100, ft.colors.BLUE_GREY_900]
                            )
                        ),
                    ),
                ),
            ],
        )
    )
    page.add(r1, r2, r3)
    page.add(
        tauro,
        aries,
        geminis,
        cancer,
        leo,
        virgo,
        libra,
        escorpio,
        sagitario,
        capricornio,
        acuario,
        piscis
    )
    
ft.app(target=main)