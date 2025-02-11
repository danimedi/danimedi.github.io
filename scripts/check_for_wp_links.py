import os
import re

os.chdir("D:/Daniel/internet/danimedi.github.io")
print(os.getcwd())

posts_folder = "_posts"

url_pattern = "danimedi.com/wp-content"

for filename in os.listdir(posts_folder):
    if filename.endswith(".md"):
        file_path = os.path.join(posts_folder, filename)
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        if url_pattern in content:
            print(filename)
