from csv_data_manager import CSVDataManager


def main ():
    CSV_PATH = "fpl_training_data/merged_gw.csv"

    csv_manager = CSVDataManager()
    df = csv_manager.csv_to_df(file_path = CSV_PATH)
    print(df.columns)

    df_col = df.columns

    df_encoded = csv_manager._label_encoder(df)
    for col in df_encoded:
        print(col)
        print(df_encoded[col].head(10))

    player_encoding = csv_manager.create_player_mapping(df_encoded)
    print(player_encoding)
    player_id_df = csv_manager.add_player_ids(df_encoded)
    print(player_id_df[["name","player_id"]])




    
if __name__ == "__main__":
    main()