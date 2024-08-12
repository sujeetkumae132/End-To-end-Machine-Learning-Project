from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

stage_name='Data Ingestion Stage'

try:
    logger.info(f">>>>> stage {stage_name} started")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {stage_name} completed")
except Exception as e:
    logger.exception(e)
    raise e