import pandas as pd

def load_to_csv(df, filename):
    """
    Save a DataFrame to a CSV file.

    Parameters:
    df (DataFrame): Pandas DataFrame
    filename (str): Output csv filename
    """

    # Loading the dataframe to a csv file
    df.to_csv(filename, index=False)
    
    print(f"Data saved to {filename}")

