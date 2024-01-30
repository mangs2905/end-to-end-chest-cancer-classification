from cnn_Classifier.config.configuration import ConfigurationManager
from cnn_Classifier.components.model_trainer import training
from cnn_Classifier import logger


STAGE_NAME = "Training"

class ModeltrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train() 
        
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModeltrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e