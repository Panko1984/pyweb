import reflex as rx
import pyweb.styles.styles as styles


def link_button(tittle: str, body:str,image:str, url: str) -> rx.Component:
    return rx.link(
         rx.button(
             rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin=styles.Size.DEFAULT.value    
                ),
                rx.vstack(
                    rx.text(tittle, style=styles.button_tittle_style),
                    rx.text(body, style=styles.button_body_style),
                    align_items="start",
                    padding_y=styles.Size.SMALL.value,
                    spacing=styles.Size.MEDIUM.value,
                    padding_RIGHT=styles.Size.SMALL.value,
                ),
               spacing=styles.Size.BIG.value,
               width="100%"
            )
         ),
            href=url,
            is_external=True,
            
        
        

            


    

        
    )
        
    
    
    
    
    
    