import os
import yaml

os.chdir("C:\\Users\\danie\\Documents\\danimedi.github.io")
POSTS_FOLDER = "_posts"

# Map your old Spanish categories to the new English names
CATEGORY_MAP = {
    "Escritos": "Writings",
    "Anécdotas": "Anecdotes",
    "Estudio y Anki": "Study & Anki",
    "Medicina": "Medicine",
    "Pensamientos": "Thoughts",
    "Programación": "Programming"
}

def update_frontmatter(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Frontmatter must start with '---'
    if not content.startswith("---"):
        return

    # Split the YAML frontmatter from the Markdown body
    parts = content.split("---", 2)
    if len(parts) < 3:
        return

    frontmatter_raw = parts[1]
    body = parts[2]

    try:
        data = yaml.safe_load(frontmatter_raw)
    except yaml.YAMLError:
        return

    # Update categories if present
    if "categories" in data and isinstance(data["categories"], list):
        updated_categories = [
            CATEGORY_MAP.get(cat, cat) for cat in data["categories"]
        ]
        data["categories"] = updated_categories

        # Re-encode frontmatter to YAML and rebuild the file
        new_frontmatter = yaml.dump(data, allow_unicode=True, sort_keys=False)
        new_content = f"---\n{new_frontmatter}---{body}"

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated: {filepath}")

# Execute for all markdown files in current directory
for root, _, files in os.walk("."):
    for file in files:
        if file.endswith((".md", ".markdown")):
            update_frontmatter(os.path.join(root, file))

def main():
    """Iterate through all Markdown files in _posts and update categories."""
    if not os.path.exists(POSTS_FOLDER):
        print(f"Folder '{POSTS_FOLDER}' not found. Check the directory path.")
        return

    for filename in os.listdir(POSTS_FOLDER):
        if filename.endswith(".md"):
            update_frontmatter(os.path.join(POSTS_FOLDER, filename))

if __name__ == "__main__":
    main()
