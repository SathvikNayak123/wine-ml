from src.mlProject import logger
from src.mlProject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.mlProject.pipeline.satge02_data_validation import DataValidationPipeline
from src.mlProject.pipeline.stage03_data_transformation import DataTransformationPipeline
from src.mlProject.pipeline.stage04_model_trainer import ModelTrainPipeline
from src.mlProject.pipeline.stage05_model_evaluation import ModelEvaluationPipeline

STAGE_NAME=" data ingestion"
try:
    logger.info(f"{STAGE_NAME} begins")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed ")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME=" data validation"
try:
    logger.info(f"{STAGE_NAME} begins")
    obj = DataValidationPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed ")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME=" data transformation"
try:
    logger.info(f"{STAGE_NAME} begins")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed ")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="model training"
try:
    logger.info(f"{STAGE_NAME} begins")
    obj = ModelTrainPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed ")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME=" data transformation"
try:
    logger.info(f"{STAGE_NAME} begins")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed ")
except Exception as e:
    logger.exception(e)
    raise e