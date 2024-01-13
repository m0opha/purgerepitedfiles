from .modules import FileHashCalculator, TraverseDirectoryTree, ProgressBarLogger, Incrementor


def GetHashingFiles(path:str, extensions:list):

    progress_logger = ProgressBarLogger()
    progress_logger.initUI("[*] Hashing files")

    allFilesFind = TraverseDirectoryTree(path)
    hashing_files = {}
    
    total_files = len(allFilesFind)

    files_to_use = Incrementor()    
    incrementor = Incrementor()
    
    try:
        for _file in allFilesFind:
            file_extension = _file.split(".")[-1]
            
            if file_extension in extensions:
   
                hashing_files[incrementor.get()] = {FileHashCalculator(_file) : _file}
                progress_logger.drawProgressBar(int(incrementor.get()*100/total_files))
   
                progress_logger.log(f"[+] {_file}")
   
                files_to_use.increment()
        
            incrementor.increment()
   
    except KeyboardInterrupt:
        pass

    finally:
        progress_logger.close()

    return hashing_files , files_to_use.get()
