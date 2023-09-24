import pandas as pd
import os

target_mssa = ['Miami-Fort Lauderdale-West Palm Beach, FL',
               'Dallas-Fort Worth-Arlington, TX',
               'Houston-The Woodlands-Sugar Land, TX',
               'Atlanta-Sandy Springs-Roswell, GA',
               'Phoenix-Mesa-Scottsdale, AZ',
               'Charlotte-Concord-Gastonia, NC-SC',
               'Minneapolis-St. Paul-Bloomington, MN-WI',
               'Portland-Vancouver-Hillsboro, OR-WA',
               'Orlando-Kissimmee-Sanford, FL',
               'Tampa-St. Petersburg-Clearwater, FL',
               'San Antonio-New Braunfels, TX' ,
               'Anniston-Oxford-Jacksonville, AL',
               'Seattle-Tacoma-Bellevue, WA',
               'Baltimore-Columbia-Towson, MD',
               'Denver-Aurora-Lakewood, CO',
               'Austin-Round Rock, TX',
               'St. Louis, MO-IL',
               'Nashville-Davidson--Murfreesboro--Franklin, TN',
               'San Diego-Carlsbad, CA',
               'Raleigh, NC'
               ]
filter_condition = "AREA_TITLE.isin(target_mssa)"
df = pd.read_excel('../data/Wage_MSA_data/MSA_M2022_dl.xlsx',usecols=['AREA_TITLE','OCC_TITLE',
                                                'TOT_EMP',
                                                'EMP_PRSE',
                                                'JOBS_1000',
                                                'LOC_QUOTIENT',
                                                'H_MEAN',
                                                'A_MEAN',
                                                'MEAN_PRSE',
                                                'H_MEDIAN',
                                                'A_MEDIAN'])
df = df[df.AREA_TITLE.isin(target_mssa)]
mapping = {i:i.split('-')[0] for i in df.AREA_TITLE.unique()}
df['Metro_Name'] = df.AREA_TITLE.map(lambda x : mapping[x])
df.to_csv('../data_out/data_wage.csv')

