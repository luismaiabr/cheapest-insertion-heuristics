#let's get the data from the xlsx files which is in the 'affinity' tab
import pandas as pd
from pydantic import BaseModel, field_validator
from typing import Any

class ProductData(BaseModel):
    """
    Pydantic model for product affinity dataframe.
    - 49x50 integer/float matrix (49 products, 50 columns)
    - No headers (skiprows=1 in Excel)
    - Values represent affinity scores between products
    """
    data: pd.DataFrame
    class Config:
        arbitrary_types_allowed = True
    @field_validator('data')
    @classmethod
    def validate_dataframe(cls, v: pd.DataFrame) -> pd.DataFrame:
        if v.shape != (49, 50):
            raise ValueError(f"DataFrame must be 49x50, got {v.shape}")
        return v

class Product:
    def __init__(self):
        self.data = self.get_data_from_xlsxs_affinity('data.xlsx')
        self.data = ProductData(data=self.data).data
    def get_data_from_xlsxs_affinity(self, file_path):
        # Read the Excel file
        xls = pd.ExcelFile(file_path)  
        # Check if 'affinity' sheet exists
        if 'affinity' not in xls.sheet_names:
            raise ValueError("The specified sheet 'affinity' does not exist in the Excel file.")
        df_affinity = pd.read_excel(xls, sheet_name='affinity', usecols="B:AY", skiprows=1, nrows=50)
        return df_affinity
    def calculate_affinity(self,p1,p2):
        #affinity of p1 (int) and p2 (int) is the value in the dataframe at row p1 and column p2
        return self.data.iat[p1, p2]
    def calculate_aversion(self,p1,p2):
        return self.calculate_affinity(p1,p2) * -1
    def get_by_coords(self, x, y):
        return self.data.iat[x, y]
    
        
    

if __name__ == "__main__":
    file_path = 'data.xlsx'  # replace with your actual file path
    product = Product()
