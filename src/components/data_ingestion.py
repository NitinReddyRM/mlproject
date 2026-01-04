import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

from src.logger import logging
from src.exception import CustomException

from dataclasses import dataclass
from datetime import datetime

import shutil
from pathlib import Path
@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join("artifacts",'test.csv')
    raw_data_path:str=os.path.join('artifacts','raw_data.csv')

class DataTransmission:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
    def DataIngestion(self):
        logging.info("Entered the Data Ingestion method")
        try:
            data=pd.read_csv("src/notebook/data/data.csv")
            logging.info("Reading the data from CSV completed")
            path=Path(os.path.dirname(self.data_ingestion_config.train_data_path))
            if path.exists():
                shutil.rmtree(path)
            os.makedirs(path,exist_ok=True)
            data.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)

            logging.info(f"Raw data Saved in {self.data_ingestion_config.raw_data_path}")
            train_set,test_set=train_test_split(data,test_size=0.3,random_state=42)
            train_set.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            logging.info(f"Train data Saved in {self.data_ingestion_config.train_data_path}")
            test_set.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)
            logging.info(f"Test data saved in {self.data_ingestion_config.test_data_path}")
            
            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )
        
            

        except Exception as e:
            
            raise CustomException(e,sys)
        
        


    