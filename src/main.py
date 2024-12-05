from textnode import *
from text_operations import *

def main():
    test_md = """# Heading

    Paragraph here.

    * List item"""

    print(markdown_to_blocks(test_md))






if __name__ == "__main__":
    main()