import pandas as pd
import numpy as np
from tqdm import tqdm 
import os
import warnings
warnings.filterwarnings("ignore")
#getting all xlxs files containing data for various MSAs
file_paths = ['./cpi_data/' + i for i in os.listdir('./cpi_data') if i.split('.')[1] == 'xlsx']
print(file_paths)
def generate_data(file):
    df = pd.read_excel(file)
    df = df.iloc[10:,:-3]
    df.columns = df.iloc[0,:]
    df = df.iloc[1:,:]
    df = df.melt(id_vars=['Year'], var_name='Month', value_name='Value')
    city = file.split('-')[0]
    df['city'] = city
    df = df.sort_values(by=['Year','Month'],ascending=True).reset_index(drop=True)

    return df
def save_file(data):
    try:
        os.mkdir('./data')
        c_data.to_csv('./data/Combined_cpi_data.csv')
    except:
        c_data.to_csv('./data/Combined_cpi_data.csv')

## Driver
c_data = pd.DataFrame()
for file_path in tqdm(file_paths):
    df = generate_data(file_path)
    c_data = pd.concat([c_data,df],axis=0)
print("Data Generated!")
save_file(c_data)
os.chdir('./data')
print("Data saved in {path}".format(path = os.getcwd()))




