from cnn_Classifier import logger
from cnn_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnn_Classifier.pipeline.stage_02_preapare_base_model import PrepareBaseModelTrainingPipeline
from cnn_Classifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from cnn_Classifier.pipeline.stage_04_moel_evaluation import EvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage{STAGE_NAME} complted <<<<<\n\nx==========x")
    
except exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"
try:
    logger.info(f"***************")
    logger.info(f">>>>> stage{STAGE_NAME} stated <<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>> stage{STAGE_NAME} completed <<<<<\n\nx==========x")
except exception as e:
    logger.exception(e)
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