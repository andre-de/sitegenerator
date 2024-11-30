from htmlnode import *
from textnode import TextNode, TextType, text_node_to_html_node
import re

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

    '''def regex_test():
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        print(extract_markdown_images(text))
        # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]'''
    
def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
        
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    pass

def split_nodes_link(old_nodes):
    pass
