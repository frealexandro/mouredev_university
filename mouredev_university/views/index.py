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
from mouredev_university.styles.styles import Spacing
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
                    "/icons/openai-icon-.png",
                    Route.COURSES.value,
                    False,
                    Color.SECONDARY.value,
                ),
            ),
            direction="column",  # Asegura que los elementos dentro del flex sean apilados verticalmente
            align_items="stretch",  # Hace que los elementos tomen el ancho completo disponible
            spacing=Spacing.VERY_SMALL.value,  # Añade espacio entre los elementos del vstack
            padding=Size.MEDIUM.value,  # Añade padding alrededor del flex  # Centrar los elementos a lo largo del eje principal (vertical si direction es "column")
        ),

    )