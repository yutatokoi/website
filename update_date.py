import os
import re
from datetime import datetime

# The directory to check for the latest modification
directory = "."

# Get the latest modification time across all files and subdirectories
latest_modification_time = max(
    os.path.getmtime(os.path.join(root, file))
    for root, _, files in os.walk(directory)
    for file in files
)

# Convert the timestamp to ISO8601 format (YYYY-MM-DD)
last_updated_date = datetime.fromtimestamp(latest_modification_time).strftime("%Y-%m-%d")

# HTML file path
html_file = "index.html"

# Read the HTML file content
with open(html_file, "r") as file:
    html_content = file.read()

# Regular expression to match the "Last updated:" line, allowing for different formats
last_updated_pattern = r"Last updated:.*?\d{4}-\d{2}-\d{2}|Last updated:.*?[A-Za-z]+\s\d{4}"

# Replace the existing "Last updated" line with the new date
new_html_content = re.sub(
    last_updated_pattern,
    f"Last updated: {last_updated_date}",
    html_content
)

# Save the updated HTML file
with open(html_file, "w") as file:
    file.write(new_html_content)

print(f"Updated 'Last updated' date to {last_updated_date}")