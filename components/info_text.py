import reflex as rx
import pyweb.styles.styles as styles
from pyweb.styles.styles import Size as Size
from pyweb.styles.colors import TextColor as TextColor



def info_text(tittle:str,body:str)-> rx.Component:
    return rx.box(
        rx.span(tittle, 
                font_wight="bold",
                color=TextColor.HEADER.value
        ),
        f"{body}", 
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value

    )