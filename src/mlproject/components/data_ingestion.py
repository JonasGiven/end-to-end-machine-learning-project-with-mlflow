import os
import urllib.request as request                                 #to download data from the url
import zipfile                                                   #to unzip the data
from src.mlproject.utils._init_ import logger
from src.mlproject.utils.common import get_size                  #to see the file size
from pathlib import Path
from src.mlproject.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
#download data from the url and logs

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size; {get_size(Path(self.config.local_data_file))}")
            
#extract data from zip file 

    def extract_zip_file(self):
       """
       
       zip_file_path: str
       Extracts the zip file into the data directory
       Funtion return none
       """
       
       unzip_path = self.config.unzip_dir
       os.makedirs(unzip_path, exist_ok=True)
       with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
           zip_ref.extractall(unzip_path)
