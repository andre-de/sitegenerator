import os
from markdown_blocks import markdown_to_html_node, extract_title
from pathlib import Path


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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)






