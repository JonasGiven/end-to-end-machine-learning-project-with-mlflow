from src.mlproject.utils._init_ import logger  # or import logger
from src.mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")             #Data Ingestion Stage has started
    obj = DataIngestionTrainingPipeline()                                #initialising this class
    obj.main()                                                           #calling this main
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e