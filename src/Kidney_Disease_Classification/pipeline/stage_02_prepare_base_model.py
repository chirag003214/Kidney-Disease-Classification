import sys
import os

from Kidney_Disease_Classification.config.configuration import ConfigurationManager
from Kidney_Disease_Classification.components.prepare_base_model import PrepareBaseModel
from Kidney_Disease_Classification import logger

STAGE_NAME = "Prepare Base Model Stage"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()

        base_model = PrepareBaseModel(config=prepare_base_model_config)
        base_model.get_base_model()
        base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        pipeline = PrepareBaseModelPipeline()
        pipeline.main()

        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
