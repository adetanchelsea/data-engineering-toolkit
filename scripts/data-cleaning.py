import pandas as pd

def clean_data(input_file, output_file):
    """
    Load in a CSV file, drop duplicates, handle missing values, standardize column names and save the output.

    Parameters: 
    input_file (the file to be cleaned) 
    output_file (the path to the cleaned file)

    Returns:
    A cleaned file with no duplicates and missing values.
    """
    # Load the CSV file
    df = pd.read_csv(input_file)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Handle missing values (fill with empty string)
    df = df.fillna("")

    # Standardize column names (make lowercase, replace spaces with underscores)
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # Save the cleaned data to a new file
    df.to_csv(output_file, index=False)

    print(f"Data cleaned and saved to {output_file}")


if __name__ == "__main__":
    clean_data("raw_data.csv", "cleaned_data.csv")

