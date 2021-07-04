import os
import pandas as pd

currentDirectory = os.getcwd()

# default folder for user datasets
os.chdir("..")
datasetsDirectory =  os.path.join(os.getcwd(), "datasets")

def get_data_from_dir(directory, fileName):
    filePath = os.path.join(directory, fileName)
    return pd.read_csv(filePath)

def get_data(file_name):
    filePath = os.path.join(datasetsDirectory, file_name)
    return pd.read_csv(filePath)
