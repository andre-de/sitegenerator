import os
import shutil
import htmlnode
import copystatic
from markdown_blocks import markdown_to_html_node, extract_title
import textnode
import text_operations

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as md_file:
        md_file_data = md_file.read()
    with open(template_path, "r") as tp_file:
        tp_file_data = tp_file.read()
    node = markdown_to_html_node(md_file_data)
    html_string = node.to_html()
    html_title = extract_title(md_file_data)
    # replace {{Title}} and {{Content}} placeholders
    title_replaced = tp_file_data.replace("{{ Title }}", html_title)
    full_page = title_replaced.replace("{{ Content }}", html_string)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    new_html_file = open(dest_path, "w")
    new_html_file.write(full_page)
    new_html_file.close()






