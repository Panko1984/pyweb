import reflex as rx
import datetime
from pyweb.styles.styles import Size as Size
from pyweb.styles.colors import TextColor as TextColor

def footer() -> rx.Component:
    return rx.vstack(

        
        rx.image(src="panko.png",width="100px",height="auto",border_radius="15px 50px",border="5px solid #555",box_shadow="lg"),
       
        rx.text(f"2023-{datetime.date.today().year}®Todos los derechos reservados. Producto Murciano by panko1984", font_size=Size.MEDIUM.value, margin_top=Size.ZERO.value),
        padding_bottom=Size.BIG.value,
        marging_bottom=Size.BIG.value,
        spacing=Size.BIG.value,
        color=TextColor.FOOTER.value,
         padding_y=Size.BIG.value

        

        
    )