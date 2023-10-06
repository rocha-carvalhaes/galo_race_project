import os
import pandas as pd
import tabula

class GetData:
    
    def __init__(self) -> None:
        pass
    
    def get_data(self, pdf_path):
        
        # List files in the data folder
        list_files = os.listdir(pdf_path)
        
        # Aranging files to display important info
        df_files = pd.DataFrame(list_files)
        df_files = df_files[0].str.split('.', expand=True)
        df_files = df_files.loc[df_files[1] == 'pdf']
        df_files = df_files[0].str.split('-', expand=True, n=2)
        df_files.columns = ['distance', 'gender', 'n']
        
        # Creating DataFrame to store extracted data
        self.data = pd.DataFrame()
        columns = ['pos','num','athlete','gender','age','group','ag','c','team','time','distance']
        
        # Extracting data
        for file_num in df_files.index:
            
            file_path = os.path.join(pdf_path, list_files[file_num])
            
            # Using tabula module to read pdf content
            table = tabula.read_pdf(
                file_path, 
                pages='all', # read all pages at once
                encoding='latin-1', 
                multiple_tables=False,
                lattice=True # informing tables are separeted by linesoooonb 
            )
            
            # Adding a column with the race distance
            table[0]['distance'] = df_files.distance[file_num]
            
            # Minimum treatments to store structured data
            df = table[0] # temporary dataframe
            first_line = pd.DataFrame(table[0].columns).T # missandertood value placed in headers
            df.columns = columns # renaming columns to standarize concatenation
            first_line.columns = columns
            self.data = pd.concat([self.data, table[0], first_line], ignore_index=True)
            
            # Replacing line breakers so csv does not get messed up
            self.data.team = self.data.team.str.replace('\r', ' ')
            self.data.athlete = self.data.athlete.str.replace('\r', ' ')   
        
        self.data = self.data.loc[self.data.pos != 'Pos']
        
        return self.data