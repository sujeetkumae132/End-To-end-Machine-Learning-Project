import os
import logging
import sys

logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s:]"
            
log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    
    handlers=[
        logging.FileHandler(log_filepath), # this command will create the file and save the log into it
        logging.StreamHandler(sys.stdout)  # this will print the log in our terminal
    ]
)

logger=logging.getLogger('mlprojectlogger')  ## here we're intializing the logger