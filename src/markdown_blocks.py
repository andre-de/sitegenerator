def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):


    return "paragraph"


def is_quote_block(block):

    return False


def is_heading_block(block):

    return False


def is_code_block(block):

    return False


def is_unordered_list(block):

    return False


def is_ordered_list(block):

    return False

