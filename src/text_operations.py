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
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        for image_alt, image_url in images:
            image_pattern = f"![{image_alt}]({image_url})"
            parts = node.text.split(image_pattern, 1)

            # Part before the image
            if parts[0]:  # Check for non-empty text  
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            # The image itself
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))

            # Prepare for the next iteration
            node.text = parts[1]

        # After loop: Check if there's remaining text after the last image
        if node.text:
            new_nodes.append(TextNode(node.text, TextType.TEXT))
            
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        for link_text, link_url in links:
            link_pattern = f"[{link_text}]({link_url})"
            parts = node.text.split(link_pattern, 1)

            # Part before the link
            if parts[0]:  # Check for non-empty text  
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            # The link itself
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            # Prepare for the next iteration
            node.text = parts[1]

        # After loop: Check if there's remaining text after the last link
        if node.text:
            new_nodes.append(TextNode(node.text, TextType.TEXT))
            
    return new_nodes


