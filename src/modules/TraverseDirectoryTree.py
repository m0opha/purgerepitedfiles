import os

def TraverseDirectoryTree(directory):
    files_found = []

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        if os.path.isfile(item_path):
            files_found.append(item_path)
        elif os.path.isdir(item_path):
            files_found.extend(TraverseDirectoryTree(item_path))

    return files_found
