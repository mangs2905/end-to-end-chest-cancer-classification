import os
from urllib.request import requests
from zipfile import ZipFile
import tensorflow as tf
import time
from cnn_Classifier.entity.config_entity import trainingConfig
from pathlib import Path

class training:
    def __init__(self, config: trainingConfig):
        self.config = config
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )
        
    def train_valid_generator(self):
        
        datagenerator_kwargs = dict(
            rescale = 1./255
            validation_split = 0.20
        )
        
        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1]
            batch_size = self.config.params_batch_size,
            interpolation = "bilinear"
        )
        
        valid_datagenerator = tf.keras.preprocessing.Image>imageDataGenerator(
            **datagenerator_kwargs
        )
        
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory = self.config.training_data,
            subset = "validation",
            shuffle = False,
            **dataflow_kwargs
        )
        
        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.Image.imageDataGenerator(
                rotation_range= 40,
                horizontal_flip = True,
                width_shift_range = 0.2,
                height_shift_range = 0.2,
                shear_range = 0.2,
                zoom_range = 0.2,
                **dataflow_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator
            
        self.train_generator = train_datagenerator.flow_from_directory(
            directory = self.config.training_data,
            subset = "training",
            shuffle = True,
            **dataflow_kwargs
        )
        
        
    @staticmethod
    def save_model(path:Path, model:tf.keras.Model):
        model.save(path)
        
        
    def train(self):
        self.steps_per_epoch = self.train_generator.sample // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.sample // self.valid_generator.batch_size
        
        self.model.fit(
            self.train_generator,
            epochs= self.config.params_epochs,
            steps_per_epochs = self.steps_per_epoch,
            validation_step = self.validation_steps,
            validation_data = self.valid_generator
        )
        
        self.save_model(
            path = self.config.trained_model_path,
            model = self.model
        )
        