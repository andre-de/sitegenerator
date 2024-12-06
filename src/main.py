from textnode import *
from text_operations import *
from markdown_blocks import *


def main():
    test_md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items

# This is a heading

###########This is NOT a heading

> quote block
> quote block
> quote block

1. ordered list
2. ordered list
3. ordered list

``` code block```

``` not code block ``

` not code block ````

"""
    blocks = markdown_to_blocks(test_md)
    #print(blocks)
    block1 = blocks[0]
    block2 = blocks[1]
    block3 = blocks[2]
    block4 = blocks[3]
    block5 = blocks[4]
    block6 = blocks[5]
    block7 = blocks[6]
    block8 = blocks[7]
    block9 = blocks[8]
    block10 = blocks[9]
    print(block8)
    #print(is_heading_block(block4))
    #print(is_quote_block(block6))
    print(is_code_block(block8))








if __name__ == "__main__":
    main()