import os
from pathlib import Path
from blocks_markdown import markdown_to_html_node, extract_title


def generate_page(from_path, template_path, dest_path):
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

    # Ensure the destination directory exists
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)

    # Write the final HTML to the destination file
    with open(dest_path, "w", encoding="utf-8") as dest_file:
        dest_file.write(full_html)

    print(f"Page successfully generated at {dest_path}")




