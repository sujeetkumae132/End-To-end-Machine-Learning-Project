# update the components
import os 
import urllib.request as request
from mlproject import logger
from mlproject.entity.config_entity import DataIngestionConfig
import zipfile
from pathlib import Path

class DataIngestion:
    def __init__(self,config=DataIngestionConfig):
        self.config=config
        
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            unzip_path=self.config.unzip_dir
            os.makedirs(unzip_path,exist_ok=True)
            filename,header=request.urlretrieve(
            url=self.config.source_url,
            filename=self.config.local_data_file)
            logger.info(f"{filename} download! with following info: \n {header}")
        else:
            logger.info(f"file already exists")
            

    def extract_zip_file(self):
        unzip_path=self.config.unzip_dir
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)