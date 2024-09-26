import os
import argparse

def generate_index_html(directory):
    html_content = "<html><body><h1>Index of {}</h1><ul>".format(directory)
    for root, dirs, files in os.walk(directory):
        for name in files:
            file_path = os.path.relpath(os.path.join(root, name), directory)
            html_content += '<li><a href="{}">{}</a></li>'.format(file_path, file_path)
    html_content += "</ul></body></html>"
    with open(os.path.join(directory, "index.html"), "w") as f:
        f.write(html_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an index.html file listing all files in a directory and its subdirectories.")
    parser.add_argument("directory", type=str, help="The directory to index")
    args = parser.parse_args()
    generate_index_html(args.directory)
