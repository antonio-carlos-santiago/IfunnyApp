import flet as ft



def main(page: ft.Page):
    
    page.bgcolor = "#18191e"
    
    page.platform = ft.PagePlatform.ANDROID
    
    imagem_titulo = ft.Image(src='./assets/likeifunny.png', width=100)
    
    campo_link = ft.TextField(
        text_align=ft.TextAlign.CENTER,
        border_color=ft.colors.AMBER,
        cursor_color=ft.colors.AMBER,
        hint_text="Insira o link",
        hint_style=ft.TextStyle(
            size=25,
            color="amber"
            ),
         text_style=ft.TextStyle(
            size=25,
            color="amber"
            ),    
    )
    
    funcao_select = ft.RadioGroup(
        content=ft.Row(
            controls=[
                ft.Radio(value=0),
                ft.Radio(value=0),
                ft.Radio(value=0),
                ft.Radio(value=0),
                ft.Radio(value=0),
            ],
            expand=True,
            vertical_alignment=ft.CrossAxisAlignment.END
            
        )
    )
    
    container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            imagem_titulo
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ),
                ft.Container(
                    padding=ft.padding.Padding(left=20, right=20, top=10, bottom=20),
                    content=ft.ResponsiveRow(
                        controls=[
                            campo_link,
                            funcao_select
                        ]
                    )
                ),
            ], 
        )
    )
        
    page.add(
        container
    )
    
    
ft.app(target=main)