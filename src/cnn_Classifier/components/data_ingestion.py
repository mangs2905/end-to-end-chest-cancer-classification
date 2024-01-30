import os
from urllib.request import request
import zipfile
import gdown
from cnn_Classifier import logger
from cnn_Classifier.utils.common import get_size
from cnn_Classifier.entity.config_entity import DataIngestionConfig




class DataIngestion:
    def __init__(self, config: DataIngestionConfig)
    self.config = config
    
    def download_file(self) -> str:
        """fetch data from URl
        """
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"downloading data from {dataset_url} into file {zip_download_dir}")
            
            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix+file_id, zip_download_dir)
            
            logger.info(f"Download data form {dataset_url} into file {zip_download_dir}")
            
        except exception as e:
            raise e
        
    def extract_zip_file(self):
        """zip_file_path : str
            extraact zip file into the data directory
            function returns None
        """
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)