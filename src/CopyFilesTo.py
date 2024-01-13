import os
import shutil

from modules import ProgressBarLogger

def CopyFilesTo(files:list, destine_path:str):

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
