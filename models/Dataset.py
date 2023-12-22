import pandas as pd

class Dataset:
    def __init__(self, csv_path):
        # load csv data into dataframe
        self.data = pd.read_csv(csv_path, index_col=0)

    def get_all(self):
        return self.data
    
    def get_desk_work_data_low(self):
        partial = self.data[self.data["usage desk work"] == True]
        return partial[partial["price"] == "Low"]
    
    def get_desk_work_data_medium(self):
        partial = self.data[self.data["usage desk work"] == True]
        return partial[partial["price"] == "Medium"]
    
    def get_desk_work_data_high(self):
        partial = self.data[self.data["usage desk work"] == True]
        return partial[partial["price"] == "High"]


    def get_engineering_data_low(self):
        partial = self.data[self.data["usage Engineering"] == True]
        return partial[partial["price"] == "Low"]
    
    def get_engineering_data_medium(self):
        partial = self.data[self.data["usage Engineering"] == True]
        return partial[partial["price"] == "Medium"]
    
    def get_engineering_data_high(self):
        partial = self.data[self.data["usage Engineering"] == True]
        return partial[partial["price"] == "High"]
    
    def get_gaming_design_low(self):
        partial = self.data[self.data["usage Gaming and Design"] == True]
        return partial[partial["price"] == "Low"]
    
    def get_gaming_design_medium(self):
        partial = self.data[self.data["usage Gaming and Design"] == True]
        return partial[partial["price"] == "Medium"]
    
    def get_gaming_design_high(self):
        partial = self.data[self.data["usage Gaming and Design"] == True]
        return partial[partial["price"] == "High"]
    
    