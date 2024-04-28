import reflex as rx
import mouredev_university.styles.styles as styles
##from mouredev_university.routes import Route
from mouredev_university.styles.styles import Size
from mouredev_university.styles.colors import Color , TextColor

# agregar buscador en el medio del navbar


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("Moure", as_="span", color=Color.PRIMARY.value),
                rx.text("dev", as_="span", color=Color.SECONDARY.value),


                rx.text("University", as_="span", color=Color.PRIMARY.value),
                style= styles.navbar_title_style
            ),
            ##href=Route.INDEX.value
        ),
        #
         rx.vstack(
                rx.input(placeholder="¿ Que quieres aprender hoy ?", type="text", style ={
                    **styles.input_style,
                    "background-color" : Color.CONTENT.value,
                    "border-color" : Color.PRIMARY.value,
                    "color" : TextColor.HEADER.value,
                    "width" : "300xp",
                    "::placeholder" : {
                    "color" : TextColor.HEADER.value
                    }
                
            }),
            position="sticky",
            bg=Color.CONTENT.value,
            padding_x=Size.HUGE.value,
            top="0",
            style=styles.input_style

        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )