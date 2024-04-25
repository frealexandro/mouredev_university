import reflex as rx 
from mouredev_university.styles.colors import TextColor
from mouredev_university.styles.colors import Color
from mouredev_university.styles.fonts import Font

STYLESHEET = [

    #fuente de google fonts
    "https://fonts.googleapis.com/css?family=Jersey+15&display=swap",
]

print(Color.PRIMARY.value)

BASE_STYLE = {
    "font-family": Font.DEFAULT.value,
    "color":  TextColor.PRIMARY.value,
    "background-color": Color.PRIMARY.value,

}