import pandas as pd

def transform_data(df):
    """
    Transform a dataframe.

    Parameters:
    df (DataFrame): A python (pandas) dataframe

    Return:
    A transformed dataframe with the name column capitalized and the salary increased by 10%.
    
    """

    # Capitalize the name column
    df["Name"] = df["Name"].str.title()

    # Salary Increase
    df["Salary"] = df["Salary"] * 1.10

    # Return transformed dataframes
    return df

