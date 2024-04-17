import io
import pandas as pd
import requests
import os
import gdown

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_kaggle(*args, **kwargs):
    """
    Template for loading data from API
    """
    # Define the Google Drive file URL
    file_url = 'https://drive.google.com/uc?id=1tNhiSBOTO0uKcyN52sUN6E4Bj8UCk-sZ'
    print('file_url',file_url)
    
    # Define the output file path (where to save the downloaded file)
    filename = 'imdb.csv'
    
    if not os.path.exists("data"):
        os.makedirs("data")

    output_file = os.path.join("data", filename)

    
    if os.path.exists(output_file):
        print("Dataset already downloaded and exists.")
    else:
        print("Downloading the dataset.")
        # Download the file from the Google Drive link
        gdown.download(file_url, output_file, quiet=True)
        print(f"File '{output_file}' downloaded successfully!")


    #data type of cols
    imdb_dtypes = {
        'id': int,
        'title': str,
        'vote_average': float,
        'vote_count': int,
        'status': str,
        'release_date': str,
        'revenue': int,
        'runtime': int,
        'adult': bool,
        'backdrop_path': str,
        'budget': int,
        'homepage': str,
        'imdb_id': str,
        'original_language': str,
        'original_title': str,
        'overview': str,
        'popularity': float,
        'poster_path': str,
        'tagline': str,
        'genres': str,
        'production_companies': str,
        'production_countries': str,
        'spoken_languages': str,
        'keywords': str,
    }

    # Date cols 
    parse_dates = ['release_date']

    df = pd.read_csv(output_file, sep=',', dtype=imdb_dtypes, parse_dates=parse_dates)
    print(df.dtypes)

    # converting so that we get only date and not datetime
    df['release_date'] = df['release_date'].dt.date

    # droping unnecessary columns (not needed for analysis)
    df.drop(['backdrop_path','homepage','poster_path','production_companies', 'production_countries', 'spoken_languages'], axis=1, inplace=True)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
