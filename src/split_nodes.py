from htmlnode import *
from textnode import TextNode, TextType, text_node_to_html_node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    total_list = []
    for node in old_nodes:
        if delimiter == "" or node.text_type != TextType.TEXT:
            total_list.append(node)
        else:
            segments = node.text.split(delimiter)
            for index, segment in enumerate(segments):
                if index %2 == 0:
                    new_node = TextNode(segment, TextType.TEXT)
                else:
                    new_node = TextNode(segment, text_type)
                total_list.append(new_node)
    return total_list  
