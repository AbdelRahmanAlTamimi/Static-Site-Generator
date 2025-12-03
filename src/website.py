import os
from pathlib import Path
from blocks_markdown import markdown_to_html_node, extract_title


def generate_page(from_path, template_path, dest_path, basepath="/"):
    """
    Generates an HTML page from a Markdown file using a template.
    Replaces {{ Title }} and {{ Content }} placeholders in the template.
    Writes the result to the destination path.
    """
    # Print the generation message
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the Markdown file
    with open(from_path, "r", encoding="utf-8") as md_file:
        markdown_content = md_file.read()

    # Read the template file
    with open(template_path, "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    # Convert Markdown to HTML
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    # Extract the title from the Markdown
    title = extract_title(markdown_content)

    # Replace placeholders in the template
    full_html = template_content.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_content
    )

    # Replace href="/ and src="/ with basepath
    full_html = full_html.replace('href="/', f'href="{basepath}')
    full_html = full_html.replace('src="/', f'src="{basepath}')

    # Ensure the destination directory exists
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)

    # Write the final HTML to the destination file
    with open(dest_path, "w", encoding="utf-8") as dest_file:
        dest_file.write(full_html)

    print(f"Page successfully generated at {dest_path}")



def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    """
    Recursively crawls the content directory, finds Markdown files, and generates HTML files
    using the provided template. The generated files are saved in the destination directory
    with the same directory structure.
    """
    # Ensure the destination directory exists
    os.makedirs(dest_dir_path, exist_ok=True)

    # Iterate through all entries in the content directory
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)
        dest_entry_path = os.path.join(dest_dir_path, entry)

        if os.path.isdir(entry_path):
            # If the entry is a directory, recursively process it
            generate_pages_recursive(entry_path, template_path, dest_entry_path, basepath)
        elif entry.endswith(".md"):
            # If the entry is a Markdown file, generate the corresponding HTML file
            html_filename = os.path.splitext(entry)[0] + ".html"
            dest_html_path = os.path.join(dest_dir_path, html_filename)
            generate_page(entry_path, template_path, dest_html_path, basepath)
            print(f"Generated: {dest_html_path}")
