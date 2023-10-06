import os
import pandas as pd

class SaveParquet:
    
    def __init__(self) -> None:
        pass
    
    def save_parquet(self, dataframe, parquets_name):
        abs_path = os.path.dirname(os.path.abspath(__file__))
        root_path = abs_path.rsplit('\\', 1)[0]
        self.folder_path = os.path.join(root_path, '01_data\\02_treated\\02_datalake')
        filename = parquets_name + '.parquet'
        saving_path = os.path.join(self.folder_path, filename)
        dataframe.to_parquet(saving_path)
        return self.folder_path