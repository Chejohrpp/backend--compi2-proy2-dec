import os
import pandas as pd

def getDataFrame(file):
    root, extension = os.path.splitext(file)
    if(extension == '.csv'):
        df = pd.read_csv(file)
        return df
    elif(extension == '.json'):
        df = pd.read_json(file)
        return df
    elif(extension == '.xlsx' or extension == '.xls'):
        df = pd.read_excel(file)
        return df
    else:
        return None