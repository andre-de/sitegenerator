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

#### This is a heading

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
    print(blocks)






if __name__ == "__main__":
    main()