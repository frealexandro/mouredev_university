import reflex as rx
import mouredev_university.styles.styles as styles
from mouredev_university.components.navbar import navbar
#from mouredev_university.components.button import li
from mouredev_university.views.index import side_bar

#import mouredev_university.utils as utils



def index() -> rx.Component:
    return rx.box(  
        rx.script(src="document.documentElement.lang='es'"),
        navbar(),
        rx.flex(
            side_bar(),
            max_width=styles.MAX_WIDTH,
            width="100%",
            margin_x=styles.Size.BIG.value,
            padding_y=styles.Size.BIG.value
        ),
    )



app = rx.App ( stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    )

app.add_page(index)