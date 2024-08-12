from mlproject.components.data_ingestion import DataIngestion
from mlproject.config.configuration import ConfigurationManager
from mlproject import logger

stage_name='Data Ingestion Stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config=ConfigurationManager()  ## reading the yaml file and passing the parameters/values
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        
    
if __name__=="main":
    try:
        logger.info(f">>>>> stage {stage_name} started")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {stage_name} completed")
    except Exception as e:
        logger.exception(e)
        raise e