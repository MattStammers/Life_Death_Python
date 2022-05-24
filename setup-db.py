import sqlite3
import pandas as pd

con = sqlite3.connect('qipy.db')
DATA_FOLDER = "datafiles"

databases = {
  "Demographics" : {
    "filename" : "demographics.csv",
    "dtypes" : {},
    "date_cols" : ["date_of_death"]
  },
  "Admissions" : {
    "filename" : "admissions.csv",
    "dtypes" : {},
    "date_cols" : [] 
  },
  "Physiology" : {
    "filename" : "physiology.csv",
    "dtypes" : {},
    "date_cols" : [] 
  },
  "Comorbidity" : {

    "filename" : "comorbidity.csv",
    "dtypes" : {},
    "date_cols" : [] 

  },
}

for table, table_details in databases.items():
  df = pd.read_csv(f'{DATA_FOLDER}/{table_details["filename"]}', parse_dates=table_details['date_cols'], dayfirst=True)
  df.to_sql(table, con)
  
con.close()