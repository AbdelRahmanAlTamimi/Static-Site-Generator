class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("LeafNode requires a value")
        super().__init__(tag=tag, value=value, children=None, props=props)
    
    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.props == other.props
        )
    
    def to_html(self):
        if self.tag is None:
            return f"{self.value}"

        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode requires a tag")
        if children is None:
            raise ValueError("ParentNode requires children")
        super().__init__(tag,None,children,props)
    
    def to_html(self):
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
