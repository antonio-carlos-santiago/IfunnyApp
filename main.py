import flet as ft



def main(page: ft.Page):
    
    page.bgcolor = "#18191e"
    
    imagem_titulo = ft.Image(src='./assets/likeifunny.png', width=150)
    
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
                ft.Radio(value=0, active_color="amber"),
                ft.Radio(value=1, active_color="amber"),
                ft.Radio(value=2, active_color="amber"),
                ft.Radio(value=3, active_color="amber"),
                ft.Radio(value=4, active_color="amber"),
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            
        )
    )
    
    icons_funcoes = ft.Row(
        expand=True,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[
            ft.Image(src='./assets/like.png', width=30),
            ft.Image(src='./assets/dislike.png', width=30),
            ft.Image(src='./assets/republicar.png', width=30),
            ft.Image(src='./assets/seguir.png', width=30),
            ft.Image(src='./assets/comentar.png', width=30)
        ]
    )
    
    campo_de_comentario = ft.TextField(
        border_color=ft.colors.AMBER,
        cursor_color=ft.colors.AMBER,
        height=400
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
                    padding=ft.padding.Padding(left=20, right=20, top=10, bottom=0),
                    content=ft.ResponsiveRow(
                        controls=[
                            campo_link,                            
                        ]
                    )
                ),
                ft.Container(
                    padding=ft.padding.Padding(left=20, right=20, top=0, bottom=20),
                    content=ft.ResponsiveRow(
                        controls=[
                            funcao_select,
                            icons_funcoes
                        ]
                    )
                )
            ], 
        )
    )
        
    page.add(
        ft.SafeArea(
            content=container
        )
    )
    
    
ft.app(target=main)