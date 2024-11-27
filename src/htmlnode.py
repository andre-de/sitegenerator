class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented("Not implemented yet")
    
    def props_to_html(self):
        return_string = ""
        for x in self.props.keys():
            return_string += (f'{x}="{self.props[x]}" ')

        return return_string
    
    def __repr__(self):
        return(f"Tag: {self.tag} Value: {self.value} Children: {self.children} Props: {self.props}")
