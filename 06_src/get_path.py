import os

class GetPath:
    
    def __init__(self) -> None:
        pass
    
    def get_pdf_path(self):
        
        # Obtaining script path
        abs_path = os.path.dirname(os.path.abspath(__file__))

        # Getting to the root path of the project
        self.root_path = abs_path.rsplit('\\', 1)[0]

        # Getting to the "01_data\\0}1_raw" folder, where pdf's are stored
        self.pdf_path = os.path.join(self.root_path, '01_data', '01_raw')
        
        return self.pdf_path
