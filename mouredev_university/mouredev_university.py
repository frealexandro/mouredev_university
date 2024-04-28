import reflex as rx
import mouredev_university.styles.styles as styles
from mouredev_university.components.navbar import navbar
#import mouredev_university.utils as utils







def index() -> rx.Component:
    return rx.box(  
        navbar(),
    )



app = rx.App ( stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    )

app.add_page(index)