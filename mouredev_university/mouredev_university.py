# import sys
# sys.path.append('/home/frealexandro/proyectos_personales/mouredev_university')
import reflex as rx
from mouredev_university.styles.styles import BASE_STYLE
from mouredev_university.styles.styles import STYLESHEET


def index( ) -> rx.Component:
    return rx.box(

    )



app = rx.App(
    stylesheets = STYLESHEET,
    style= BASE_STYLE,

)



app.add_page(index,
             title="Mouredev University",
             description="this is a university website free to learn",
             
             
             )

