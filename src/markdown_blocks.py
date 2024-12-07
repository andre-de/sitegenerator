from htmlnode import ParentNode
from text_operations import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"



def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks




def block_to_block_type(block): #tbd
    if is_quote_block(block):
        return "quote"
    if is_heading_block(block):
        return "heading"
    if is_code_block(block):
        return "code"
    if is_unordered_list(block):
        return "unordered_list"
    if is_ordered_list(block):
        return "ordered_list"
    return "paragraph"




def is_quote_block(block): #done
    block_lines = block.split("\n")
    for line in block_lines:
        if len(line) == 0:
            return False
        elif line[0] != ">":
            return False
    return True


def is_heading_block(block): #done
    elements = block.split()
    hash_count = elements[0].count("#")
    if hash_count > 0 and hash_count < 7 and hash_count == len(elements[0]):
        return True
    return False


def is_code_block(block): #done
    elements = block.split("\n")
    last_element = elements[len(elements)-1]

    # check first element for the three fronting backticks
    if len(elements[0]) < 3:
        return False
    if elements[0][0] != "`" or elements[0][1] != "`" or elements[0][2] != "`":
        return False
    
    #check last element for the three trailing backticks
    lle = len(last_element)
    if len(last_element) < 3:
        return False
    if last_element[lle-1] != "`" or last_element[lle-2] != "`" or last_element[lle-3] != "`":
        return False

    return True


def is_unordered_list(block):#done
    elements = block.split("\n")
    for line in elements:
        if len(line) < 2:
            return False
        if (line[0] != "*" and line[0] != "-") or line[1] != " ":
            return False
    return True


def is_ordered_list(block):#done
    counter = 0
    elements = block.split("\n")
    for line in elements:
        if len(line)<3:
            return False
        if not "." in line:
            return False
        sequence = line.split(".")
        if not sequence[0].isnumeric():
            return False
        if sequence[1][0] != " ":
            return False
        if int(sequence[0]) != counter + 1:
            return False
        counter += 1
        
    return True

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

