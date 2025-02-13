import os

def find_http_files(directory):
    http_files = []

    # Walk through all files and subdirectories
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    if "http://" in content:
                        http_files.append(filepath)
            except Exception as e:
                print(f"Could not read {filepath}: {e}")

    return http_files

# Example usage: Change '/path/to/directory' to your actual directory path
directory_path = "D:/Daniel/internet/danimedi.github.io/scripts"
files_with_http = find_http_files(directory_path)

# Print results
if files_with_http:
    print("Files containing 'http://':")
    for file in files_with_http:
        print(file)
else:
    print("No files contain 'http://'.")
