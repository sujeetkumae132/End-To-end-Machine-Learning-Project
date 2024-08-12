from mlproject.components.data_validation import DataValidation
from mlproject.config.configuration import ConfigurationManager
from mlproject import logger

stage_name='Data Validation Stage'

class DataValidationTrainingPipeline:
    
    def __init__(self):
        pass
    
    def main(self):
        try:
            config=ConfigurationManager()
            data_validation_config=config.get_data_validation_config()
            data_validation=DataValidation(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e


if __name__=="main":
    try:
        logger.info(f">>>>> stage {stage_name} started")
        obj=DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {stage_name} completed")
    except Exception as e:
        logger.exception(e)
        raise e