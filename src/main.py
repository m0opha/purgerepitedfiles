from .functions import (ArgHandler, 
                        GetHashingFiles, 
                        FindRepitedFiles, 
                        CopyFilesTo,
                        DeleteFiles)

def main():
    
    (selected_extensions, 
     path,
     destine_path, 
     purge_duplicates) = ArgHandler()
    
    hashingfiles , usedfiles = GetHashingFiles(path=path,  extensions=selected_extensions)     
    selectedfiles , repited_files = FindRepitedFiles(hashingfiles=hashingfiles)

    if purge_duplicates:
        DeleteFiles(repited_files)
        print(f"Total files: {usedfiles}, Delete files : {len(repited_files)}")

    if destine_path != None:
        files_copied = CopyFilesTo(files=selectedfiles, destine_path=destine_path)
        print(f"Total files : {usedfiles}, copied : {files_copied}, repited : {usedfiles - files_copied}")