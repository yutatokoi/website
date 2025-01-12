import os
import yaml
import markdown2

# Paths
markdown_root = "./templates/writing"
output_root = "./static/writing"
index_file = "./templates/writing.html"

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

# Generate the index page
with open(index_file, "w", encoding="utf-8") as f:
    f.write("<!DOCTYPE html>\n<html lang='en'>\n<head>\n")
    f.write("<title>Writing</title>\n<link rel='stylesheet' href='../static/styles.css'>\n</head>\n<body>\n")
    f.write("<h1>My Writings</h1>\n<ul>\n")
    for post in posts:
        f.write(f"<li>\n")
        f.write(f"  <a href='{post['url']}'>{post['title']}</a>\n")
        f.write(f"  <span>(Published: {post['publish_date']}")
        if post['edit_date']:
            f.write(f", Edited: {post['edit_date']}")
        f.write(")</span>\n")
        f.write(f"</li>\n")
    f.write("</ul>\n</body>\n</html>")

