import os
import shutil
import logging
from website import generate_page

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(message)s")


def clean_and_copy_directory(src_dir, dst_dir):
    """
    Recursively copies all contents from src_dir to dst_dir.
    Deletes all contents of dst_dir before copying to ensure a clean copy.
    Logs the path of each file being copied.
    """
    if not os.path.exists(src_dir):
        logging.error(f"Source directory does not exist: {src_dir}")
        return

    if os.path.exists(dst_dir):
        logging.info(f"Deleting existing destination directory: {dst_dir}")
        shutil.rmtree(dst_dir)

    os.makedirs(dst_dir, exist_ok=True)
    logging.info(f"Created destination directory: {dst_dir}")

    def copy_recursive(src, dst):
        for item in os.listdir(src):
            src_path = os.path.join(src, item)
            dst_path = os.path.join(dst, item)

            if os.path.isdir(src_path):
                logging.info(f"Copying directory: {src_path} -> {dst_path}")
                os.makedirs(dst_path, exist_ok=True)
                copy_recursive(src_path, dst_path)
            else:
                logging.info(f"Copying file: {src_path} -> {dst_path}")
                shutil.copy2(src_path, dst_path)

    copy_recursive(src_dir, dst_dir)
    logging.info(f"Finished copying from {src_dir} to {dst_dir}")


def main():
    """
    Main function to execute the script logic.
    """
    # Copy static files to the public directory
    source_directory = "static"
    destination_directory = "public"
    clean_and_copy_directory(source_directory, destination_directory)

    # Generate the HTML page from Markdown and template
    from_path = "content/index.md"
    template_path = "template.html"
    dest_path = "public/index.html"
    generate_page(from_path, template_path, dest_path)


# Entry point of the script
if __name__ == "__main__":
    main()
