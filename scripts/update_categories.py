import os
import yaml
import re

os.chdir("D:\Daniel\internet\danimedi.github.io")

# Define the category mapping (old category -> new category)
CATEGORY_MAP = {
    "Web y programación": "Programación",
    # Add more category replacements as needed
}

# Path to the _posts folder
POSTS_FOLDER = "_posts"

def update_categories(file_path):
    """Update the categories in the YAML front matter of a Markdown file."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if the file contains a YAML front matter
    match = re.match(r"^---\n(.*?)\n---\n(.*)", content, re.DOTALL)
    if not match:
        print(f"Skipping {file_path}: No YAML front matter found.")
        return

    yaml_content, post_body = match.groups()

    # Parse YAML front matter
    yaml_data = yaml.safe_load(yaml_content)

    # Update categories if present
    if "categories" in yaml_data:
        updated_categories = [CATEGORY_MAP.get(cat, cat) for cat in yaml_data["categories"]]
        yaml_data["categories"] = updated_categories

        # Convert back to YAML
        new_yaml_content = yaml.dump(yaml_data, sort_keys=False, allow_unicode=True).strip()

        # Reconstruct the file
        new_content = f"---\n{new_yaml_content}\n---\n{post_body}"

        # Save the changes
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated categories in {file_path}")

def main():
    """Iterate through all Markdown files in _posts and update categories."""
    for filename in os.listdir(POSTS_FOLDER):
        if filename.endswith(".md"):
            update_categories(os.path.join(POSTS_FOLDER, filename))

if __name__ == "__main__":
    main()
