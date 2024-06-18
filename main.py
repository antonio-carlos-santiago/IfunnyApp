import flet as ft



def main(page: ft.Page):
    page.bgcolor = "#18191e"
    imagem_titulo = ft.Image(src='./assets/likeifunny.png', width=100)
    campo_link = ft.TextField(
        text_align=ft.TextAlign.CENTER,
        border_color=ft.colors.AMBER,
        cursor_color=ft.colors.AMBER,
        
        
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
                    padding=ft.padding.Padding(left=20, right=20, top=0, bottom=20),
                    content=ft.ResponsiveRow(
                        controls=[
                            campo_link
                        ]
                    )
                )
            ], 
        )
    )
        
    page.add(
        container
    )
    
    
ft.app(target=main)