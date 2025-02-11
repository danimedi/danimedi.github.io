import os
import re

os.chdir("D:/Daniel/internet/danimedi.github.io")
print(os.getcwd())

# Define paths
blog_url_prefix = "https://danimedi.com/blog/"
posts_folder = "_posts"

# Regex to find links starting with the blog URL
url_pattern = re.compile(r'\[([^\]]+)\]\(https://danimedi.com/blog/([^\)]+)\)')

def convert_to_relative_links(content):
    """Replace absolute links to blog posts with relative links."""
    def replace_link(match):
        text, post_path = match.groups()
        relative_path = f"/{post_path}"
        final_text = "[" + text + "]" + "({{ " + "'/blog" + relative_path + "' | relative_url }})"
        return final_text
    
    return url_pattern.sub(replace_link, content)

# Process all markdown files in _posts
for filename in os.listdir(posts_folder):
    if filename.endswith(".md"):
        file_path = os.path.join(posts_folder, filename)
        
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        updated_content = convert_to_relative_links(content)
        
        if content != updated_content:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(updated_content)
            print(f"Updated links in {filename}")
        else:
            print(f"No changes in {filename}")
