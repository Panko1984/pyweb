"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from pyweb.components.navbar import navbar
from pyweb.views.header.header import header
from pyweb.views.links.links import links
from pyweb.components.footer import footer
import pyweb.styles.styles as styles
from pyweb.styles.colors import Color as Color

class State(rx.State):
    
    pass


def index() -> rx.Component:

    return rx.box(
        
            navbar(),
            rx.center(
            rx.vstack(
           
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=styles.Size.BIG.value
                )   
            ),
            footer(),
    
         
        )
     

    
 

app= rx.App(
    stylesheets=styles.STYLESHEETS,
    
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Panko1984 | Un poco de mí",
    description="Hola, me llamo Jose Ángel. Hago recopilación de mis redes sociales y os cuento un poco de mi",
    image="panko.ico"

)


