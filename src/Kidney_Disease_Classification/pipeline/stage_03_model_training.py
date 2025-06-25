from Kidney_Disease_Classification.components.data_ingestion import DataIngestion
from Kidney_Disease_Classification.config.configuration import ConfigurationManager
from Kidney_Disease_Classification import logger
from Kidney_Disease_Classification.components.model_training import Training  


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
        
import os
import shutil

# Define source and destination
source = "artifacts/prepare_base_model/updated_model.h5"
destination_dir = "prediction_model"
destination = os.path.join(destination_dir, "updated_model.h5")

# Create the destination folder if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Move the model file
if os.path.exists(source):
    shutil.move(source, destination)
    print(f"✅ Moved updated_model.h5 to {destination}")
else:
    print("❌ updated_model.h5 not found in artifacts/prepare_base_model.") 