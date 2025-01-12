import os
import yaml
import markdown2
from bs4 import BeautifulSoup  # For parsing and modifying HTML

# Paths
markdown_root = "./templates/writing"
output_root = "./static/writing"
writing_html_path = "./templates/writing.html"

# Ensure the output directory exists
os.makedirs(output_root, exist_ok=True)

# Helper to extract YAML front matter
def extract_front_matter(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if content.startswith("---"):
        parts = content.split("---", 2)
        metadata = yaml.safe_load(parts[1])
        markdown_content = parts[2].strip()
        return metadata, markdown_content
    return {}, content

# Collect posts
posts = []
for root, dirs, files in os.walk(markdown_root):
    for file in files:
        if file == "main.md":
            md_path = os.path.join(root, file)
            rel_path = os.path.relpath(root, markdown_root)  # Subdirectory path (e.g., "2025-01-11_using-ghostty")

            # Extract metadata and convert Markdown
            metadata, md_content = extract_front_matter(md_path)
            html_content = markdown2.markdown(md_content)

            # Determine output path
            output_dir = os.path.join(output_root, rel_path)
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, "index.html")

            # Write HTML file
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(html_content)

            # Collect metadata for the index page
            title = metadata.get("title", "Untitled Post")
            publish_date = metadata.get("publishDate", "Unknown Date")
            edit_date = metadata.get("editDate", "")
            posts.append({
                "title": title,
                "publish_date": publish_date,
                "edit_date": edit_date,
                "url": f"/static/writing/{rel_path}/index.html"
            })

# Sort posts by publish date (most recent first)
posts.sort(key=lambda x: x["publish_date"], reverse=True)

# Parse and update the writing.html file
with open(writing_html_path, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Locate the <ul> in the <main> section
ul = soup.find("main").find("ul")
if ul:
    # Clear existing list items
    ul.clear()

    # Add new posts as <li> elements
    for post in posts:
        li = soup.new_tag("li")
        a = soup.new_tag("a", href=post["url"])
        a.string = f"{post['publish_date']}: {post['title']}"
        li.append(a)
        if post["edit_date"]:
            li.append(soup.new_string(f" (Edited: {post['edit_date']})"))
        ul.append(li)

# Write the updated HTML back to writing.html
with open(writing_html_path, "w", encoding="utf-8") as f:
    f.write(str(soup.prettify(formatter="html")))

