from mlproject.constant import *
from mlproject.utils.common import read_yaml_file,create_directories
from mlproject.entity.config_entity import DataIngestionConfig,DataValidationConfig

class ConfigurationManager:
    def __init__(self,
                config_filepath=config_file_path,
                params_filepath=config_file_path,
                schema_filepath=config_file_path):
        self.config=read_yaml_file(config_filepath)
        self.params=read_yaml_file(params_filepath)
        self.schema=read_yaml_file(schema_filepath)
        
        create_directories([self.config.artifacts_root])  # this artifacts root name mentioned in the config.yaml
        
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config=self.config.data_ingestion
        
        create_directories([self.config.artifacts_root])
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )
        
        return data_ingestion_config
        
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config=self.config.data_validation
        schema=self.schema.columns
        
        
        create_directories([config.root_dir])
        
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_dir=config.unzip_data_dir,
            status_file=config.STATUS_FILE,
            all_schema=schema
        )
        
        return data_validation_config