import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.expection import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPiplineConfig

if __name__ == '__main__':
    try:
        dataingestionconfig = DataIngestionConfig(TrainingPiplineConfig())
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion completed")
        datavalidationconfig = DataValidationConfig(TrainingPiplineConfig())
        data_validation = DataValidation(dataingestionartifact,datavalidationconfig)
        logging.info("Initiate the data vlidation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("data validation complted")
        print(data_validation_artifact)
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)