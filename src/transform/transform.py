import pandas as pd

def transform_data(df):
    """
    Transforms the input DataFrame by cleaning, converting data types, and creating new features.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame.

    Returns:
    pd.DataFrame: Transformed DataFrame.
    """
    try:
        # Drop rows with missing CustomerID
        df_cleaned = df.dropna(subset=['CustomerID'])

        # Fill missing descriptions with "Unknown"
        df_cleaned['Description'].fillna("Unknown", inplace=True)

        # Remove negative Quantity and UnitPrice
        df_cleaned = df_cleaned[(df_cleaned['Quantity'] > 0) & (df_cleaned['UnitPrice'] > 0)]

        # Convert InvoiceDate to datetime
        df_cleaned['InvoiceDate'] = pd.to_datetime(df_cleaned['InvoiceDate'])

        # Convert CustomerID to integer
        df_cleaned['CustomerID'] = df_cleaned['CustomerID'].astype(int)

        # Create TotalPrice feature
        df_cleaned['TotalPrice'] = df_cleaned['Quantity'] * df_cleaned['UnitPrice']

        # Separate columns for time-based analysis
        df_cleaned['Year'] = df_cleaned['InvoiceDate'].dt.year
        df_cleaned['Month'] = df_cleaned['InvoiceDate'].dt.month
        df_cleaned['Day'] = df_cleaned['InvoiceDate'].dt.day
        df_cleaned['Hour'] = df_cleaned['InvoiceDate'].dt.hour

        print("Data Transformed Successfully")
        return df_cleaned
    except Exception as e:
        print(f"An error occurred during transformation: {e}")
        return None
