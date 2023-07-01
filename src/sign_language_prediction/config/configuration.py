from sign_language_prediction.constants import *
from sign_language_prediction.utils.common import read_yaml, create_directories
from sign_language_prediction.entity.config_entity import *

class ConfigurationManager:
    def __init__(
        self,
				#we get these values from constant
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):
				
				#using read yaml fun we read the files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
				
				#Here the read_yaml file retuen configBox type ie key:pair type so we 
				#crete the dictionary with the key value
        create_directories([self.config.artifacts_root])


    #we gat all the values from config file and create directories
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config