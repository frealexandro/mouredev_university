import reflex as rx
#import link_bio.constants as const
#from link_bio.components.newsletter import newsletter
#from link_bio.components.featured_link import featured_link
from mouredev_university.routes import Route
from mouredev_university.components.button import link_button
#from link_bio.components.title import title
from mouredev_university.styles.styles import Color
#from link_bio.state.PageState import PageState
from mouredev_university.styles.styles import Size 
from mouredev_university.styles import styles





def side_bar() -> rx.Component:
    return rx.flex(
        #utils.lang(),
        #navbar(),
        rx.flex(  # Usando rx.flex para un control más granular
            rx.vstack(
                link_button(
                    "GPT-3",
                    "Interactua con el modelo de lenguaje de OpenAI",
                    "/mouredev_university/assets/icons/openai.svg",
                    Route.COURSES.value,
                    False,
                    Color.SECONDARY.value,
                ),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            ),
            direction="column",  # Organizar los elementos en dirección vertical
            align_items="center",  # Centrar los elementos a lo largo del eje transversal (horizontal)
            justify_content="center",  # Centrar los elementos a lo largo del eje principal (vertical si direction es "column")
        ),
        #footer(),
        direction="column",  # Ajustar la dirección según sea necesario
    )