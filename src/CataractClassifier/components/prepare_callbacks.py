import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from CataractClassifier.entity.config_entity import PrepareCallbacksConfig




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

    def _create_ckpt_callbacks(self):
        # Ensure the filepath is a string
        ckpt_dir = str(self.config.checkpoint_model_filepath)
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=ckpt_dir,
            save_weights_only=True,
            monitor='val_loss',
            mode='min',
            save_best_only=True
        )

    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,  # Call the property to get the callback instance
            self._create_ckpt_callbacks()  # Call the method to get the callback instance
        ]
