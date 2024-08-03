from src.mlProject import logger
from src.mlProject.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME=" data ingestion"
try:
    logger.info(f"{STAGE_NAME} begins")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"{STAGE_NAME} completed ")
except Exception as e:
    logger.exception(e)
    raise e
