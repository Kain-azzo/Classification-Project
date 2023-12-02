import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split


def prep_telco(isp):
    '''Takes the data frame and gets rid of unnecessary data converts isp charges data into a usable format for modeling''' 
    isp = isp.drop(columns = ['payment_type_id','internet_service_type_id','contract_type_id'])
    isp.total_charges = isp.total_charges.str.replace(' ', '0.0').astype(float)
    isp.dependents = isp.dependents.map({"No":0,"Yes":1}).astype(int)
    isp.partner = isp.partner.map({"No":0,"Yes":1}).astype(int)
    isp.phone_service = isp.phone_service.map({"No":0,"Yes":1}).astype(int)
    isp.paperless_billing = isp.paperless_billing.map({"No":0,"Yes":1}).astype(int)
    internet_service_type = internet_service_type.fillna("No internet service")
    
    return isp

def chop_data(frame, col):
    '''Takes the data frame and breaks it into train, test, and split information, with two splits'''

    train, validate_test = train_test_split(frame,
                     train_size=0.6,
                     random_state=123,
                     stratify=frame[col]
                    )

    validate, test = train_test_split(validate_test,
                                     train_size=0.5,
                                      random_state=123,
                                      stratify=validate_test[col]
                        
                                     )
    return train, validate, test

