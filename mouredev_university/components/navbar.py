import reflex as rx
import mouredev_university.styles.styles as styles
##from mouredev_university.routes import Route
from mouredev_university.styles.styles import Size
from mouredev_university.styles.colors import Color , TextColor
#from mouredev_university.state import State

# agregar buscador en el medio del navbar

#from chat.state import State


def sidebar_chat(chat: str) -> rx.Component:
    """A sidebar chat item.

    Args:
        chat: The chat item.
    """
    return  rx.drawer.close(rx.hstack(
        rx.button(
            #chat, on_click=lambda: State.set_chat(chat), width="80%", variant="surface"
        ),
        rx.button(
            rx.icon(
                tag="trash",
                on_click=State.delete_chat,
                stroke_width=1,
            ),
            width="20%",
            variant="surface",
            color_scheme="red",
        ),
        width="100%",
    ))



def sidebar(trigger) -> rx.Component:
    """The sidebar component."""
    return rx.drawer.root(
        rx.drawer.trigger(trigger),
        rx.drawer.overlay(),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.heading("Chats", color=rx.color("mauve", 11)),
                    rx.divider(),
                    #rx.foreach(State.chat_titles, lambda chat: sidebar_chat(chat)),
                    align_items="stretch",
                    width="100%",
                ),
                top="auto",
                right="auto",
                height="100%",
                width="20em",
                padding="2em",
                background_color=rx.color("mauve", 2),
                outline="none",
            )
        ),
        direction="left",
    )



def modal(trigger) -> rx.Component:
    """A modal to create a new chat."""
    return rx.dialog.root(
        rx.dialog.trigger(trigger),
        rx.dialog.content(
            rx.hstack(
                rx.input(
                    placeholder="Type something...",
                    #on_blur=State.set_new_chat_name,
                    width=["15em", "20em", "30em", "30em", "30em", "30em"],
                ),
                rx.dialog.close(
                    rx.button(
                        "Create chat",
                        #on_click=State.create_chat,
                    ),
                ),
                background_color=rx.color("mauve", 1),
                spacing="2",
                width="100%",
            ),
        ),
    )





def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("El", as_="span", color=Color.PRIMARY.value),
                rx.text("Model", as_="span", color=Color.SECONDARY.value),


                rx.text("aje", as_="span", color=Color.PRIMARY.value),
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
                    "width" : "30vw",
                    "::placeholder" : {
                    "color" : TextColor.HEADER.value
                    }
                
            }),
            position="sticky",
            bg=Color.CONTENT.value,
            padding_x=   "10vw",   #Size.HUGE.value,
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