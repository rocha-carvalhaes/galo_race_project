# importing modules to be used
import tabula # to read pdf
import os # to treat directories
import pandas as pd # to manipulate data
#from pypdf import PdfReader # to count pdf pages

# Obtaining script path
abs_path = os.path.dirname(os.path.abspath(__file__))

# Getting to the root path of the project
root_path = abs_path.rsplit('\\', 1)[0]

# Getting to the "01_data\\01_raw" folder, where pdf's are stored
data_path = os.path.join(root_path, '01_data', '01_raw')

# List files in the data folder
list_files = os.listdir(data_path)

# Aranging files to display important info
df_files = pd.DataFrame(list_files)
df_files = df_files[0].str.split('.', expand=True)
df_files = df_files.loc[df_files[1] == 'pdf']
df_files = df_files[0].str.split('-', expand=True, n=2)
df_files.columns = ['distance', 'gender', 'n']

# Creating DataFrame to store extracted data
data = pd.DataFrame()
columns = ['pos','num','athlete','gender','age','group','ag','c','team','time','distance']

# Extracting data
for file_num in df_files.index:
    
    file_path = os.path.join(data_path, list_files[file_num])
    
    # Using tabula module to read pdf content
    table = tabula.read_pdf(
        file_path, 
        pages='all', # read all pages at once
        encoding='latin-1', 
        multiple_tables=False,
        lattice=True # informing tables are separeted by lines
    )
    
    # Adding a column with the race distance
    table[0]['distance'] = df_files.distance[file_num]
    
    # Minimum treatments to store structured data
    df = table[0] # temporary dataframe
    first_line = pd.DataFrame(table[0].columns).T # missandertood value placed in headers
    df.columns = columns # renaming columns to standarize concatenation
    first_line.columns = columns
    data = pd.concat([data, table[0], first_line], ignore_index=True)
    
    # Replacing line breakers so csv does not get messed up
    data.team = data.team.str.replace('\r', ' ')
    data.athlete = data.athlete.str.replace('\r', ' ')

# Exporting to csv
data.to_csv(os.path.join(root_path, '01_data\\02_treated\\02_datalake\\results.csv'))