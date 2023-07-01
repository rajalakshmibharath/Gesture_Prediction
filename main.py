from sign_language_prediction import logger
from sign_language_prediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


#we give stagfe name for all the satges
STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
	 #we call the training pipeline and run the main
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e