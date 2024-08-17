from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_evaluation import ModelEvaluation
from mlproject import logger

stage_name='model evaluation stage'

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation_config()
        model_evaluation_config=ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()
        

if __name__=="main":
    try:
        logger.info(f">>>>> stage {stage_name} started")
        obj=ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>> stage {stage_name} completed")
    except Exception as e:
        logger.exception(e)
        raise e