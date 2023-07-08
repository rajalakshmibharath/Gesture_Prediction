import os
import urllib.request as request
import zipfile
from sign_language_prediction import logger
from sign_language_prediction.utils.common import get_size
from sign_language_prediction.entity.config_entity import DataIngestionConfig
from sign_language_prediction.entity.config_entity import PrepareBaseModelConfig
from sign_language_prediction.entity.config_entity import PrepareCallbacksConfig

import tensorflow as tf
import time

from pathlib import Path

class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config


    
    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}",
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    

    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )


    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]