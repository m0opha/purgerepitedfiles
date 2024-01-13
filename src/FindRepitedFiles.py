from modules import ProgressBarLogger

def FindRepitedFiles(hashingfiles:dict):

    progress_logger = ProgressBarLogger()
    progress_logger.initUI("[*] Find repited files and purge")
    
    non_repited_files = []
    repited_files = []
    
    total_files = len(hashingfiles)
    auto_increment = 0
    
    try:
        for _value in hashingfiles.values():        
            
            ActualHash = list(_value.keys())[0]
            ActualPath = list(_value.values())[0]

            if ActualPath in repited_files:
                auto_increment += 1
                continue

            for _internvalue in hashingfiles.values():
          
                probehash = list(_internvalue.keys())[0]
                probepath = list(_internvalue.values())[0]
                
                if (ActualHash == probehash) and (probepath != ActualPath):
                    progress_logger.drawProgressBar(int(auto_increment*100/total_files))
                    progress_logger.log(f"[*] {probepath}")
                    repited_files.append(probepath)                 
                    continue
                
            non_repited_files.append(ActualPath)
            auto_increment += 1

    except KeyboardInterrupt:
        progress_logger.close()

    finally:
        progress_logger.close()

    return non_repited_files
