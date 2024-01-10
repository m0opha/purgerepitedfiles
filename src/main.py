import shutil
import os
import json
import sys
from colorama import Fore, Style, Back

from modules import FileHashCalculator
from modules import TraverseDirectoryTree
from modules import ProgressBarLogger

def GetHashingFiles(path:str, extensions:list):

    progress_logger = ProgressBarLogger()
    progress_logger.initUI("[*] Hashing files")

    allFilesFind = TraverseDirectoryTree(path)
    hashing_files = {}
    used_files = 0    
    total_files = len(allFilesFind)
    auto_increment = 0
    
    try:
        for _file in allFilesFind:
            file_extension = _file.split(".")[-1]
            if file_extension in extensions:
                hashing_files[auto_increment] = {FileHashCalculator(_file) : _file}
                progress_logger.drawProgressBar(int(auto_increment*100/total_files))
                progress_logger.log(f"[+] {_file}")
                used_files += 1
        
            auto_increment += 1
    except KeyboardInterrupt:
        progress_logger.close()

    finally:
        progress_logger.close()

    return hashing_files , used_files

def findrepitedfiles(hashingfiles:dict):
    progress_logger = ProgressBarLogger()
    progress_logger.initUI("[*] Find repited files and purge")
    
    non_repited_files = []
    repited_files = []
    total_files = len(hashingfiles)
    auto_increment = 0
    try:
        for _ , _value in hashingfiles.items():        
            
            ActualHash = list(_value.keys())[0]
            ActualPath = list(_value.values())[0]

            for _intenrkey , _internvalue in hashingfiles.items():
                probehash = list(_internvalue.keys())[0]
                probepath = list(_internvalue.values())[0]
                
                if (ActualHash == probehash) and (probepath != ActualPath) and (ActualPath not in repited_files):
                
                    progress_logger.drawProgressBar(int(auto_increment*100/total_files))
                    progress_logger.log(f"[-] {probepath}")
                    
                    repited_files.append(probepath)                 
                    continue
                
            if ActualPath not in repited_files:
                non_repited_files.append(ActualPath)
            
            auto_increment += 1

    except KeyboardInterrupt:
        progress_logger.close()

    finally:
        progress_logger.close()

    return non_repited_files
 
def copyfilesto(files:list, destine_path:str):

    if not os.path.exists(destine_path):
        os.makedirs(destine_path)
    else:
        pass

    progress_logger = ProgressBarLogger()
    progress_logger.initUI("[*] copying files to destination")    
    auto_increment = 0
    try:
        for _file in files:
            shutil.copy(_file , destine_path)
            auto_increment += 1

            progress_logger.drawProgressBar(int(auto_increment*100/len(files)))
            progress_logger.log(f"[-] {_file}")            

    except KeyboardInterrupt:
        progress_logger.close()

    finally:
        progress_logger.close()

    return auto_increment
    
def parser():
    arguments_tree= {}
    key = "filename"
    value = []
    set_filename = True
    for _args in sys.argv:
        if _args[0] == "-":
            if key != _args:
                if value == []:
                    arguments_tree[key] = None
                else:
                    arguments_tree[key] = value if len(value) > 1 else value[0]
                    value = []
            key = _args
        else:
            if set_filename:
                set_filename = False
                arguments_tree[key] = _args

                key = "lone"
                value = []
                continue

            value.append(_args)
    if key:
        if value == []:
            arguments_tree[key] = None

        else:
            arguments_tree[key] = value if len(value) > 1 else value[0]

    return arguments_tree

def main():

    destine_path = ""
    path = ""

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
    selectedfiles = findrepitedfiles(hashingfiles)
    files_copied = copyfilesto(selectedfiles, destine_path=destine_path)

    print(f"total files : {usedfiles}, copied : {files_copied}, repited : {usedfiles - files_copied}")

if __name__ == "__main__":
    main()
    #print(json.dumps(parser(), indent=2))
