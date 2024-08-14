from mlproject.components.data_transformation import DataTransformation
from mlproject.config.configuration import ConfigurationManager
from mlproject import logger
from pathlib import Path

stage_name='Data Transformation Stage'

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        path="D:\\AIML Projects\\ineuron-python\\self_practical\\End-To-end-Machine-Learning-Project\\artifacts\\data_validation\\status.txt"
        try:
            with open(path,"r") as f:
                status=f.read().split(" ")[-1]
                
            if status=="True":
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("data schema is not valid")
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