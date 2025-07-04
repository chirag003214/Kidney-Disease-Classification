import sys
import os

# Add the src folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', 'src')))

from Kidney_Disease_Classification.components.data_ingestion import DataIngestion
from Kidney_Disease_Classification.config.configuration import ConfigurationManager
from Kidney_Disease_Classification import logger
from Kidney_Disease_Classification.components.model_training import Training  

import sys
import os

# Add the src folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..', 'src')))

STAGE_NAME = "Training"



class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()



if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        


# Define source and destination
