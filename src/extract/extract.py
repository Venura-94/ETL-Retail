import pandas as pd

def extract_data(file_path):
    """
    Extracts data from a CSV file and returns a DataFrame.
    
    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing the extracted data.
    """
    try:
        # Read CSV file
        df = pd.read_csv(file_path, encoding="ISO-8859-1")
        print("Data Extracted Successfully")
        print(df.info())
        return df
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

