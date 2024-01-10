import json
import shutil
import os
import sys
from colorama import Fore, Style, Back

from modules import FileHashCalculator
from modules import TraverseDirectoryTree

def main():

    path = sys.argv[1]
    destine_path = sys.argv[2]
    extension_filter = sys.argv[3].split(",")

    continue_option = input("continue? (yes/no) : ")

    if continue_option in ["yes", "YES", "Y", "y"]:
        pass
    else:
        sys.exit(1)

    if not os.path.exists(destine_path):
        os.makedirs(destine_path)
    else:
        pass

    #hash calculing
    print("[*] hash calculing")
    find_files = TraverseDirectoryTree(path)
    files_info = {}
    count_all_files = 0
    count = 0
    total_files = len(find_files)
    for _file in find_files:
        extension_extract = _file.split(".")[-1]
        if extension_extract in extension_filter:
            files_info[count] = {FileHashCalculator(_file) : _file}
            print(f"    {Fore.GREEN}{Style.BRIGHT}[progress {round(count*100/total_files, 2)}%]{Style.RESET_ALL} {_file}")
            count_all_files += 1
        count += 1

    print("\n[*]Repited files find")
    #pruge repited files
    final_files = []
    repited_files = []
    for _value in files_info.values():        
        ActualHash = list(_value.keys())[0]
        ActualPath = list(_value.values())[0]

        for _value2 in files_info.values():
            probehash = list(_value2.keys())[0]
            probepath = list(_value2.values())[0]
            
            if (ActualHash == probehash) and (probepath != ActualPath) and (ActualPath not in repited_files):
                print(f"    {Fore.GREEN}{Style.BRIGHT}original {ActualPath} \n      {Fore.RED}{Style.BRIGHT}-> repited file: {probepath}{Style.RESET_ALL}")
                repited_files.append(probepath)                
                continue
            
        if ActualPath not in repited_files:
            final_files.append(ActualPath)

    #print(json.dumps(final_files, indent=2))

    print("\n[*]copy files")
    count = 0
    for _f in final_files:
        shutil.copy(_f , destine_path)
        count += 1
        print(f"    {Fore.GREEN}{Style.BRIGHT}[progress {round(count*100/len(final_files), 2)}]{Style.RESET_ALL} copy {_f} to {destine_path}")
        
    print(f"initial files : {count_all_files}, copied files : {len(final_files)}")

if __name__ == "__main__":
    main()