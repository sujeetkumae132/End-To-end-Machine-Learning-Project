from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_trainer import ModelTrainer
from mlproject import logger

stage_name='model trainer stage'

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        model_train_config=config.get_model_trainer_config()
        model_trainer_config=ModelTrainer(config=model_train_config)
        model_trainer_config.train()
        
if __name__=="main":
    try:
        logger.info(f">>>>> stage {stage_name} started")
        obj=ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {stage_name} completed")
    except Exception as e:
        logger.exception(e)
        raise e