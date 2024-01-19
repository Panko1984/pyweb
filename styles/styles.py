
from .colors import Color as Color
from .colors import TextColor as TextColor
from .fonts import Font as Font
from enum import Enum
import reflex as rx
#constants
MAX_WIDTH ="600PX"

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap"
]

#Sizes
class Size(Enum):
    ZERO="0px !important"
    SMALL="0.5em"
    MEDIUM="0.8em"
    DEFAULT="1em"
    LARGE= "1.5em"
    BIG="2em"
    VERY_BIG="4em"

#Sytles
    
BASE_STYLE = {

  
"background_color" : Color.BACKGROUND.value+"!important",
 "font_family": Font.DEFAULT.value,
 

    rx.Button:{
        "width": "100%",
        "height": "100%",
         "white_space": "normal",
         "text_align": "start",

        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": TextColor.BODY.value,
        "background_color" : Color.CONTENT.value ,
        "_hover": {
            "background_color" : Color.PRIMARY.value
        }
        
    },
    rx.Link :{
        "text_decoration":"none",
        "_hover":{},
        "width": "100%"
        

    },

     rx.Box :{
        
        "background_color": Color.BACKGROUND.value + "!important",

    },

    rx.Heading:{
                    "color":TextColor.HEADER.value,
                    "size":"sm"
                    
                           
    }


}

button_tittle_style = dict(
    font_size=Size.LARGE.value,
    color=TextColor.HEADER.value,
    font_family=Font.TITLE.value


)


navbar_tittle_style = dict(

    font_family=Font.LOGO.value,
    font_size=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
    position="sticky",
    bg=Color.CONTENT.value,
    padding_x=Size.DEFAULT.value,
    padding_y=Size.SMALL.value,
    z_index="999",
    top="0"


)

button_body_style = dict(
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value,
    font_family=Font.DEFAULT.value


)

tittle_style = dict(
    font_family=Font.TITLE.value,
    width="100%",
    padding_top=Size.DEFAULT.value,
    color=TextColor.HEADER.value,
    size="SM"
    





)