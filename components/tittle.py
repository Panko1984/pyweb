import reflex as rx
import pyweb.styles.styles as styles


def tittle(text:str)-> rx.Component:
    return rx.heading(
        text,
        
        style=styles.tittle_style,
        
    
    )