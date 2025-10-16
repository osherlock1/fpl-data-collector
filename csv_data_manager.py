import pandas as pd
import csv
from sklearn.preprocessing import LabelEncoder
#File for handling csv data

#class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)[source]

# try:
#     player_data = pd.read_csv("fpl_training_data/merged_gw.csv", on_bad_lines='skip')
# except pd.errors.ParserError as e:
#     print(f"Parset errors {e}")


# df = pd.DataFrame(data=player_data)
# print(df.columns)


class CSVDataManager:
    def __init__(self):
        self.player_mapping = {}
        
    def csv_to_df(self, file_path) -> pd.DataFrame:
        data = pd.read_csv(file_path, on_bad_lines='skip')
        df = pd.DataFrame(data=data)
        return df

    def _label_encoder(self, dataframe: pd.DataFrame):
        le = LabelEncoder()
        #Identify categorical columns 
        #categorical_columns = ["position", "modified", "was_home"]
        categorical_columns = dataframe.select_dtypes(include=['object']).columns
        excluded_columns = ['name', 'team']
        
        for col in categorical_columns:
            if col not in excluded_columns:
                dataframe[col] = le.fit_transform(dataframe[col].astype(str))
        
        return dataframe
    
    def create_player_mapping(self, df) -> pd.DataFrame:
        unique_players = df["name"].unique()
        self.player_mapping = {name: idx for idx, name in enumerate(unique_players)}
        return self.player_mapping
    
    def add_player_ids(self, df: pd.DataFrame, name_column='name'):
        if not self.player_mapping:
            self.create_player_mapping(df, name_column)
        
        df['player_id'] = df[name_column].map(self.player_mapping)
        return df