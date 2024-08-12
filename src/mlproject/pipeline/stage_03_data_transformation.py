from mlproject.components.data_transformation import DataTransformation
from mlproject.config.configuration import ConfigurationManager
from mlproject import logger

stage_name='Data Transformation Stage'

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config=ConfigurationManager()
            data_transformation_config=config.get_data_transformation_config()
            data_transformation=DataTransformation(config=data_transformation_config)
            data_transformation.train_test_spliting()
        except Exception as e:
            raise e
        
        
if __name__=="main":
    try:
        logger.info(f">>>>> stage {stage_name} started")
        obj=DataTransformationPipeline()
        obj.main()
        logger.info(f">>>> stage {stage_name} completed")
    except Exception as e:
        logger.exception(e)
        raise e