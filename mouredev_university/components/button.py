import reflex as rx
import mouredev_university.styles.styles as styles
#from mouredev_university.routes import Route
from mouredev_university.styles.styles import Size ,Spacing
from mouredev_university.styles.colors import Color , TextColor






def link_button(title: str,
                body: str,
                image: str,
                url: str,
                is_external=True,
                highlight_color=None,
                animated=False) -> rx.Component:

    return rx.button(
        rx.hstack(
            rx.image(
                src=image,
                width=Size.LARGE.value,
                height=Size.LARGE.value,
                margin=Size.MEDIUM.value,
                alt=title
            ),
            rx.vstack(
                rx.text(
                    title,
                    size=Spacing.SMALL.value,
                    style=styles.button_title_style
                ),
                rx.text(
                    body,
                    size=Spacing.VERY_SMALL.value,
                    style=styles.button_body_style
                ),
                align_items="start",
                spacing=Spacing.VERY_SMALL.value,
                padding_y=Size.SMALL.value,
                padding_right=Size.SMALL.value
            ),
            align="center",
            width="100%"
        ),
        border=f"{'2px' if highlight_color != None else '0px'} solid {highlight_color}",
        class_name=styles.BOUNCEIN_ANIMATION if animated else None,
        on_click=rx.redirect(path=url, external=is_external),
        padding=Size.MEDIUM.value,
        style={
            'display': 'flex',
            'align_items': 'center',
            'justify_content': 'flex-start'  # Alinea horizontalmente al inicio
        }
    )
    