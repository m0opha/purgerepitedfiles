from .functions import (ArgHandler, 
                        GetHashingFiles, 
                        FindRepitedFiles, 
                        CopyFilesTo)

def main():
    
    selected_extensions , path , destine_path = ArgHandler()
    
    hashingfiles , usedfiles = GetHashingFiles(path=path,  extensions=selected_extensions)     
    selectedfiles = FindRepitedFiles(hashingfiles=hashingfiles)
    files_copied = CopyFilesTo(files=selectedfiles, destine_path=destine_path)

    print(f"total files : {usedfiles}, copied : {files_copied}, repited : {usedfiles - files_copied}")