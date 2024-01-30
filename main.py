from cnn_Classifier import logger
from cnn_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnn_Classifier.pipeline.stage_02_preapare_base_model import PrepareBaseModelTrainingPipeline
from cnn_Classifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from cnn_Classifier.pipeline.stage_04_model_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage{STAGE_NAME} complted <<<<<\n\nx==========x")
    
except exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"***************")
    logger.info(f">>>>> stage{STAGE_NAME} stated <<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> stage{STAGE_NAME} completed <<<<<\n\nx==========x")
except exception as e:
    logger.exception(e)
    raise e





STAGE_NAME = "Training"
try:
    config = ConfigurationManager()
    training_config = config.get_prepare_base_model_config()
    training = training(config=training_config)
    training.get_base_model()
    training.train_valid_generator()
    training.train()
except Exception as e:
    raise e





STAGE_NAME = "Evaluation stage"
try:
    logger.info(f"")
    logger.info(f">>>>> stage{STAGE_NAME} started <<<<<")
    model_evaluation = EvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except exception as e:
    logger.exception(e)
    raise e