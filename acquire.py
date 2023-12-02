
import pandas as pd
import numpy as np

import access # get access to the telco database
import os # enables checking the  the file file



def check_file_exists(file, query, url):
  
    if os.path.exists(file):
        print('this file exists, reading csv')
        frame = pd.read_csv(file, index_col=0)
    else:
        print('this file doesnt exist, read from sql, and export to csv')
        frame = pd.read_sql(query, url)
        frame.to_csv(file)
        
    return frame

def get_telco_data():
    '''Acquires the telco data from the SQL titanic database'''
    
    query =  '''select * from customers as cust
	left join contract_types as ct
		using(contract_type_id)
	left join internet_service_types as ist
		using(internet_service_type_id)
	left join payment_types as pt
        using(payment_type_id)
    '''
    url = access.get_db_url('telco_churn')
    file = 'telco.csv'
     
    frame = check_file_exists(file, query, url)
    return frame

get_telco_data = get_telco_data()