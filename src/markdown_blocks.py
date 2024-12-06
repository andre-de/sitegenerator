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

