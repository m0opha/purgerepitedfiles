from  .FileHashCalculator import FileHashCalculator
from .TraverseDirectoryTree import TraverseDirectoryTree
from .ProgressBarLogger import ProgressBarLogger

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
