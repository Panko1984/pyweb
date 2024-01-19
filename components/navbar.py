
import reflex as rx
from pyweb.styles.styles import Size as Size
from pyweb.styles.colors import Color as Color
from pyweb.styles.colors import TextColor as TextColor
import pyweb.styles.styles as styles
def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
       
            rx.span(
                "panko",
                color=TextColor.BODY.value,
                 bg=Color.CONTENT.value
              
               
            ),
             rx.span(
        
                     "1984",
                    color=Color.BACKGROUND.value,
                    bg=Color.CONTENT.value
            ),

                 
              
              
        
            bg=Color.CONTENT.value
            
        ),
       
    style=styles.navbar_tittle_style 
    )