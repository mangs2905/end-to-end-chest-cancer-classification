import os
from cnn_Classifier.constants import *
from cnn_Classifier.utils.common import read_yaml, create_directories, save_json
from cnn_Classifier.entity.config_entity import (DataIngestionConfig,
                                                 PrepareBaseModelConfig,
                                                 trainingConfig,
                                                 EvaluationConfig)


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH
        
        self.config = read_yaml(config_filepath)
        self.params = params_yaml(params_filepath)
        
        create_directories([self.config.artifacts_root]))
    
    def get_ingestion_configuration(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        
        return data_ingestion_config

    def get_ingestion_configuration(self) -> PrepareBaseModelConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )
        
        return prepare_base_model_config





    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model= self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "kidney_city_scan_iamge")
        create_directories([
            Path(training.root_dir)
        ])
        
        training_config = trainingConfig(
            root_dir = Path(training.root_dir),
            trained_model_path = path(training.trained_model_path),
            updated_base_model_path = Path(prepare_base_model.updated_base_model_path),
            training_data = Path(training_data),
            params_epochs = params.EPOCHS,
            params_batch_size = params.BATCH_SIZE,
            params_is_augmentation = params.AUGMENTATION,
            params_iamge_size = params.IMAGE_SIZE
        )
        
        return training_config
    
    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model = "artifacts/training/model.h5",
            training_data = "artifacts/data_ingestion/kidney_city_scan_image",
            mlflow_uri = "************",
            all_params= self.params,
            params_image_size = self.params.IMAGE_SIZE,
            params_batch_size= self.params_BATCH_SIZE
        )
        return eval_config