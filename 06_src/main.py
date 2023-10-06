import os
from save_parquet import SaveParquet
from get_data import GetData
from get_path import GetPath

class Run:
    
    def __init__(self) -> None:
        pass
    
    def check_run(self, saving_path) -> bool:
        list_files = os.listdir(saving_path)
        if self.parquets_name+'.parquet' in list_files:
            return True
        
    
    def run(self):
        pdf_path = GetPath().get_pdf_path()
        data = GetData().get_data(pdf_path=pdf_path)
        self.parquets_name = 'results'
        self.saving_folder = SaveParquet().save_parquet(dataframe=data, parquets_name=self.parquets_name)
        if self.check_run(self.saving_folder) == True:
            print('Sucesso!\nArquivo salvo no repositório')
        else:
            print('Ops!\nArquivo não foi salvo no repositório')
        
Run().run()