import shutil
import os
import json
import sys
from colorama import Fore, Style, Back

from modules import parser
from modules import GetHashingFiles
from modules import FindRepitedFiles
from modules import CopyFilesTo 

def help():
    pass

def main():

    destine_path = None
    path = None

    doc_extensions = ['doc', 'docx', 'pdf', 'txt', 'rtf', 'odt', 'xls', 'xlsx', 'ppt', 'pptx', 'csv', 'html', 'htm', 'pages']
    video_extensions = ['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv', 'm4v', 'mpeg', 'mpg', 'webm', '3gp', 'vob', 'swf']
    img_extensions = ['jpg', 'jpeg', 'png', 'gif', 'svg', 'bmp', 'tiff', 'tif', 'raw', 'psd', 'ai', 'eps']
    music_extensions = ['mp3', 'wav', 'flac', 'aac', 'ogg', 'wma', 'm4a', 'midi', 'opus', 'ac3']

    selected_extensions = []

    extracted_argv = parser()
    allowed_argv = ["filename",
                    "lone",
                    "--path",
                    "--destine", 
                    "--img",
                    "--music",
                    "--video",
                    "--doc",
                    "--custom",
                    "-p",
                    "-d",
                    "-i",
                    "-m",
                    "-v",
                    "-d",
                    "-c"]
    
    for _argv , _value in extracted_argv.items():
        if _argv not in allowed_argv:
            print(f"[+] unrecognized argument {_argv}")
            sys.exit()
        
        elif _argv in ["--path", "-p"]:
            if len( _value) < 1:
                print(f"[-] You can only enter a single path in {_argv}")
                sys.exit()
            else:
                path = _value

        elif _argv in ["--destine", "-d"]:
            if len( _value) < 1:
                print(f"[-] You can only enter a single path {_argv}")
                sys.exit(1)
            else:
                destine_path = _value
        
        elif _argv in ["--img", "-i"]:
            selected_extensions.extend(img_extensions)

        elif _argv in ["--music", "-m"]:
            selected_extensions.extend(music_extensions)

        elif _argv in ["--video", "-v"]:
            selected_extensions.extend(video_extensions)
        
        elif _argv in ["--doc", "-d"]:
            selected_extensions.extend(doc_extensions)
        
        elif _argv in ["--custom", "-c"]:
            selected_extensions.extend(_value)


    if len(selected_extensions) == 0:
        print("[-] you must select an extension option")
        sys.exit(1)


    hashingfiles , usedfiles = GetHashingFiles(path=path,  extensions=selected_extensions)     
    selectedfiles = FindRepitedFiles(hashingfiles)
    files_copied = CopyFilesTo(selectedfiles, destine_path=destine_path)

    print(f"total files : {usedfiles}, copied : {files_copied}, repited : {usedfiles - files_copied}")


if __name__ == "__main__":
    main()