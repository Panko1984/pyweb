import reflex as rx
from pyweb.components.link_icon import link_icon 
from pyweb.components.info_text import info_text
from pyweb.styles.colors import Color as Color
from pyweb.styles.colors import TextColor as TextColor
from pyweb.styles.styles import Size as Size
import pyweb.styles.styles as styles
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pyweb.components.tittle import tittle

                
edad = relativedelta(datetime.now(), datetime(1984, 4, 29))

def header() -> rx.Component:
    return rx.vstack(
          rx.hstack(
            rx.avatar(
                name="José Ángel Nicolás",
                size="xl",
                src="jose.png",
                padding="2px",
                border="4px",
                border_color=Color.CONTENT.value,
                      
            ),
            rx.vstack(
                
                tittle(
                    "HOLA🤘, SOY JOSE ANGEL,"         
                ),
                rx.text(
                    "@panko1984",
                    margin_top=Size.ZERO.value,
                    color=TextColor.BODY.value
                    
                    
                ),

                
                link_icon("http://www.marca.com/"),
                align_items="start",
              

                
            ),
            Color=TextColor.BODY.value,
            spacing=Size.DEFAULT.value
          ),
            rx.flex(
                
                info_text(f"{edad.years}", f" años, {edad.months} meses y {edad.days} días desde que me parieron." )
            ),
            rx.text("Diplomado en Ciencias Empresariales,aprendiz de programador informático(con unas pocas asignaturas de la ingieneria sacadas 😛),eterno proyecto de Frontman en un grupo de Rock, contable-administrativo durante más de 10 años, actualmente Funcionario de Carrera en la Administración General de Estado con muchos intereses e inquietudes, algo friki y un deportista incansable. Aquí encontraras todos los enlaces de mis redes sociales.¡Bienvenid@!", text_align="justify", color=TextColor.BODY.value,font_size="0.9em"),
            
            align_items="start",
            spacing=styles.Size.BIG.value
           


    )
