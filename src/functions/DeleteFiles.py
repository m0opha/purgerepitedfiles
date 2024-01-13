import os

from .modules import Incrementor, ProgressBarLogger

def DeleteFiles(files:list):

    progress_logger = ProgressBarLogger()
    progress_logger.initUI("[*] Delete the repeated files in the source directory")    

    incrementor = Incrementor()

    for _file in files:

        try:
            os.remove(_file)
            incrementor.increment()

            progress_logger.drawProgressBar(int(incrementor.get()*100/len(files)))
            progress_logger.log(f"[-] {_file}")           

        except FileNotFoundError:
            print(f"The file {_file} does not exist.")
       
        except Exception as e:
            print(f"Error while trying to delete the file {_file}: {e}")

        finally:
            progress_logger.close()