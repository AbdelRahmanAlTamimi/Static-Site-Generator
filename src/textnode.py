from enum import Enum


class TextType(Enum):
    TEXT = "text"  
    BOLD = "bold"  
    ITALIC = "italic"  
    CODE = "code"  
    LINK = "link"  
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return(
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )
    def __repr__(self):
        text_type_value = (
            self.text_type.value if isinstance(self.text_type, Enum) else self.text_type
        )
        return f"TextNode({self.text}, {text_type_value}, {self.url})"
    

