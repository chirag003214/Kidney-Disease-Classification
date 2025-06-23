from src.Kidney_Disease_Classification import logger
from src.Kidney_Disease_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Kidney_Disease_Classification.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline


STAGE_NAME = "Data Ingestion stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
    STAGE_NAME = "Prepare base model"
    try: 
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        prepare_base_model = PrepareBaseModelPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
