# import sys
# sys.path.append('/home/frealexandro/proyectos_personales/mouredev_university')
import reflex as rx
from mouredev_university.styles.styles import styles



def index( ) -> rx.Component:
    return rx.box(

    )



app = rx.App(
    styles=styles.STYLESHEET,
    style= styles.BASE_STYLE,

)



app.add_page(index,
             title="Mouredev University",
             description="this is a university website free to learn",
             
             
             )

app.compile()