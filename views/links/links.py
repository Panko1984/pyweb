import reflex as rx
from pyweb.components.link_button import link_button
from pyweb.components.tittle import tittle
from pyweb.styles.styles import Size as Size
def links() -> rx.Component:
    return rx.vstack(
        tittle("Redes Sociales"),
        link_button("Facebook","Mi red social más antigua","meta.svg","https://www.facebook.com/joseangel.nicolaslopez/"),
        link_button("Instagram","No lo uso mucho","instagram.svg","https://www.instagram.com/panko_1984/"),
        link_button("X","Antiguo Twitter","twitter.svg","https://twitter.com/JosngelNicolsL1"),
        link_button("Discord","El Chat de la Comunidad","discord.svg","https://discord.gg/uue4z6VW"),
       
        tittle("Contacto y otras cositas"),
        link_button("GMAIL","Para contactar conmigo","envelope-solid.svg","mailto:oseangel.nicolas@gmail.com"),
        link_button("Invitame a un cafe...","Apoya mi trabajo :P ","mug-hot-solid.svg","https://www.buymeacoffee.com/joseangelnp"),
        link_button("Youtube","Mi canal de Yotube","youtube.svg","https://www.youtube.com/channel/UCVLYxa1memzTbQ_b8SuNPSQ"),

        width="100%",
        spacing=Size.DEFAULT.value,
        
        
       
        
    )