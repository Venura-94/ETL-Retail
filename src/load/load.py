import boto3
import io

def load_to_s3(df, bucket_name, folder_name, aws_access_key, aws_secret_key, file_name):
    """
    Loads the DataFrame to AWS S3 in CSV format.

    Parameters:
    df (pd.DataFrame): DataFrame to upload.
    bucket_name (str): AWS S3 bucket name.
    folder_name (str): Folder name in S3 bucket.
    aws_access_key (str): AWS access key.
    aws_secret_key (str): AWS secret key.
    file_name (str): Name of the file to be uploaded.
    """
    try:
        # Initialize S3 client
        s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )

        # Convert DataFrame to CSV in memory
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)

        # Upload to S3
        s3_client.put_object(Bucket=bucket_name, Key=f"{folder_name}/{file_name}", Body=csv_buffer.getvalue())
        print(f"Data loaded to S3 bucket '{bucket_name}' in folder '{folder_name}' as '{file_name}'")
    except Exception as e:
        print(f"An error occurred while uploading to S3: {e}")