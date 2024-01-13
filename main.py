from colorama import Fore, Style, Back

from src import (GetHashingFiles,
                 FindRepitedFiles,
                 CopyFilesTo,
                 ArgHandler)

def main():
    
    selected_extensions , path , destine_path = ArgHandler()
    
    hashingfiles , usedfiles = GetHashingFiles(path=path,  extensions=selected_extensions)     
    selectedfiles = FindRepitedFiles(hashingfiles)
    files_copied = CopyFilesTo(selectedfiles, destine_path=destine_path)

    print(f"total files : {usedfiles}, copied : {files_copied}, repited : {usedfiles - files_copied}")

if __name__ == "__main__":
    main()