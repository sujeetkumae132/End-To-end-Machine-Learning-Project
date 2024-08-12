from src.mlproject import logger
from src.mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.mlproject.pipeline.stage_03_data_transformation import DataTransformationPipeline


stage_name='Data Ingestion Stage'

try:
    logger.info(f">>>>> stage {stage_name} started")
    obj=DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {stage_name} completed <<<<< /n/nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


stage_name='Data Validation Stage'

try:
    logger.info(f">>>>> stage {stage_name} started")
    obj=DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {stage_name} completed <<<<< /n/nx==========x")
except Exception as e:
    logger.exception(e)
    raise e



stage_name='Data Transformation Stage'

try:
    logger.info(f">>>>> stage {stage_name} started")
    obj=DataTransformationPipeline()
    obj.main()
    logger.info(f">>>> stage {stage_name} completed <<<<< /n/nx==========x")
except Exception as e:
    logger.exception(e)
    raise e