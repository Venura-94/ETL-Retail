from src.configurations.configurations import file_path, bucket_name, folder_name, aws_access_key, aws_secret_key, file_name
from src.extract.extract import extract_data
from src.transform.transform import transform_data
from src.load.load import load_to_s3
from src import logger

STAGE_NAME = "Data Extraction stage"

logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
df = extract_data(file_path)
logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")


STAGE_NAME = "Data Transform stage"

logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
df = transform_data(df)
logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")


STAGE_NAME = "Data loading stage"

logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
load_to_s3(df, bucket_name, folder_name, aws_access_key, aws_secret_key, file_name)
logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")



