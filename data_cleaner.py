import pandas as pd
import os

RENTAL_DATA_PATH = './data/rental_data'
GLOBAL_PATH = '/Users/Ben/Documents/Programming/Predictive-Gentrification-Model'

def rename_rental_data(RENTAL_DATA_PATH):
    print(os.listdir(RENTAL_DATA_PATH))
    files = sorted([f for f in os.listdir(RENTAL_DATA_PATH)])
    
    year = 2023
    print(files)
    
    for i, file_name in enumerate(files):
    
        new_name = f"average_rent_{year - i}.csv"
        old_file_path = os.path.join(RENTAL_DATA_PATH, file_name)
        new_file_path = os.path.join(RENTAL_DATA_PATH, new_name)
        
        os.rename(old_file_path, new_file_path)
        print(f"Renamed '{file_name}' to '{new_name}'")


def clean_rental_data(file_name):
    try:
        df = pd.read_csv(
            GLOBAL_PATH + RENTAL_DATA_PATH[1:] + '/' + file_name, 
            skiprows=2,
            encoding='ISO-8859-1', 
            on_bad_lines='skip'
        )
        
    except pd.errors.ParserError as e:
        print("ParserError:", e)
        
    df = df.drop(columns=['Unnamed: 2', 'Unnamed: 4', 'Unnamed: 6', 'Unnamed: 8', 'Unnamed: 10', 'Unnamed: 11'])
    df = df.rename(columns={'Unnamed: 0': 'Neighborhood'})
    df = df.replace('**', 0)
    print(df['1 Bedroom'])
    df = df.iloc[:-6]
    df.iloc[:, 1:] = df.iloc[:, 1:].apply(lambda x: x.replace({',': ''}, regex=True).astype(int))
    print(df)
    df.to_csv(f'data/rental_data/{file_name}_cleaned.csv', index=False)
    
    
if __name__ == '__main__':
    files = sorted([f for f in os.listdir(RENTAL_DATA_PATH) if ".csv" in f])
    for f in files:
        clean_rental_data(f)