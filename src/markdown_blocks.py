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


    return "paragraph"




def is_quote_block(block): #done
    quoted_line = True
    block_lines = block.split("\n")
    for line in block_lines:
        if len(line) == 0:
            return False
        elif line[0] != ">":
            quoted_line = False
    return quoted_line


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


def is_unordered_list(block):#tbd

    return False


def is_ordered_list(block):#tbd

    return False

