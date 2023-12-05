import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split


def prep_telco(isp):
    '''Takes the data frame and gets rid of unnecessary data converts isp charges data into a usable format for modeling''' 
    #isp = isp.drop(columns = ['customer_id','payment_type_id','internet_service_type_id','contract_type_id'])
    isp = isp.drop(columns=['customer_id', 'payment_type_id', 'internet_service_type_id', 'contract_type_id'])

    isp.total_charges = isp.total_charges.str.replace(' ', '0.0').astype(float)
    isp.gender = isp.gender.map({"Male":0,"Female":1}).astype(int)
    isp.dependents = isp.dependents.map({"No":0,"Yes":1}).astype(int)
    isp.partner = isp.partner.map({"No":0,"Yes":1}).astype(int)
    isp.churn = isp.churn.map({"No":0,"Yes":1}).astype(int)
    isp.phone_service = isp.phone_service.map({"No":0,"Yes":1}).astype(int)
    isp.paperless_billing = isp.paperless_billing.map({"No":0,"Yes":1}).astype(int)
    isp.internet_service_type = isp.internet_service_type.fillna("No internet service")
    isp['security_backup'] = ((isp['online_security'] == 'Yes') | 
                                             (isp['online_backup'] == 'Yes')).astype(int)
    isp['security_backup'] = ((isp['online_security'] == 'Yes') | 
                                             (isp['online_backup'] == 'Yes')).astype(int)
    isp['security_backup'] = ((isp['online_security'] == 'Yes') | 
                                             (isp['online_backup'] == 'Yes')).astype(int)
 
    isp.internet_service_type = isp.internet_service_type.map({'No internet service': 0, 'DSL': 1, 
                                                                                             'Fiber optic': 1})
    isp.multiple_lines = isp.multiple_lines.map({'No phone service': 0, 'No': 0, 'Yes': 1})
    
    isp = isp.drop(columns=["streaming_tv","streaming_movies","online_backup","online_security"])
    isp = isp.drop(columns=["device_protection","tech_support"])
    dummy1 = pd.get_dummies(isp[["contract_type"]], columns=["contract_type"], dtype="int")
    isp = pd.concat([isp, dummy1], axis=1)
    dummy2 = pd.get_dummies(isp[["payment_type"]],columns=["payment_type"],dtype="int")
    isp = pd.concat([isp, dummy2], axis=1)
    isp = isp.drop(columns=["payment_type","contract_type"])
    
    
      
    
    return isp

def keep_cust_prep_telco(isp):
    '''Takes the data frame and gets rid of unnecessary data converts isp charges data into a usable format for modeling, but    
     leaves customer ID'''
    isp = isp.drop(columns = ['payment_type_id','internet_service_type_id','contract_type_id'])
    isp.total_charges = isp.total_charges.str.replace(' ', '0.0').astype(float)
    isp.gender = isp.gender.map({"Male":0,"Female":1}).astype(int)
    isp.dependents = isp.dependents.map({"No":0,"Yes":1}).astype(int)
    isp.partner = isp.partner.map({"No":0,"Yes":1}).astype(int)
    isp.churn = isp.churn.map({"No":0,"Yes":1}).astype(int)
    isp.phone_service = isp.phone_service.map({"No":0,"Yes":1}).astype(int)
    isp.paperless_billing = isp.paperless_billing.map({"No":0,"Yes":1}).astype(int)
    isp.internet_service_type = isp.internet_service_type.fillna("No internet service")
    isp['security_backup'] = ((isp['online_security'] == 'Yes') | 
                                             (isp['online_backup'] == 'Yes')).astype(int)
    isp['security_backup'] = ((isp['online_security'] == 'Yes') | 
                                             (isp['online_backup'] == 'Yes')).astype(int)
    isp['security_backup'] = ((isp['online_security'] == 'Yes') | 
                                             (isp['online_backup'] == 'Yes')).astype(int)
 
    isp.internet_service_type = isp.internet_service_type.map({'No internet service': 0, 'DSL': 1, 
                                                                                             'Fiber optic': 1})
    isp.multiple_lines = isp.multiple_lines.map({'No phone service': 0, 'No': 0, 'Yes': 1})
    
    isp = isp.drop(columns=["streaming_tv","streaming_movies","online_backup","online_security"])
    isp = isp.drop(columns=["device_protection","tech_support"])
    dummy1 = pd.get_dummies(isp[["contract_type"]], columns=["contract_type"], dtype="int")
    isp = pd.concat([isp, dummy1], axis=1)
    dummy2 = pd.get_dummies(isp[["payment_type"]],columns=["payment_type"],dtype="int")
    isp = pd.concat([isp, dummy2], axis=1)
    isp = isp.drop(columns=["payment_type","contract_type"])
    
    
    
    return isp
    
def charts_telco(isp):
    '''Takes the data frame and gets rid of unnecessary data converts isp charges data into a usable format for CHARTS''' 
    isp = isp.drop(columns = ['customer_id','payment_type_id','internet_service_type_id','contract_type_id'])
    isp.total_charges = isp.total_charges.str.replace(' ', '0.0').astype(float)
    isp.gender = isp.gender.map({"Male":0,"Female":1}).astype(int)
    isp.dependents = isp.dependents.map({"No":0,"Yes":1}).astype(int)
    isp.partner = isp.partner.map({"No":0,"Yes":1}).astype(int)
    #isp.churn = isp.churn.map({"No":0,"Yes":1}).astype(int)
    isp.phone_service = isp.phone_service.map({"No":0,"Yes":1}).astype(int)
    isp.paperless_billing = isp.paperless_billing.map({"No":0,"Yes":1}).astype(int)
    isp.internet_service_type = isp.internet_service_type.fillna("No internet service")
    isp['security_backup'] = ((isp['online_security'] == 'Yes') | 
                                             (isp['online_backup'] == 'Yes')).astype(int)
    isp['security_backup'] = ((isp['online_security'] == 'Yes') | 
                                             (isp['online_backup'] == 'Yes')).astype(int)
    isp['security_backup'] = ((isp['online_security'] == 'Yes') | 
                                             (isp['online_backup'] == 'Yes')).astype(int)
 
    isp.internet_service_type = isp.internet_service_type.map({'No internet service': 0, 'DSL': 1, 
                                                                                             'Fiber optic': 1})
    isp.multiple_lines = isp.multiple_lines.map({'No phone service': 0, 'No': 0, 'Yes': 1})
    
    isp = isp.drop(columns=["streaming_tv","streaming_movies","online_backup","online_security"])
    isp = isp.drop(columns=["device_protection","tech_support"])
    dummy1 = pd.get_dummies(isp[["contract_type"]], columns=["contract_type"], dtype="int")
    isp = pd.concat([isp, dummy1], axis=1)
    dummy2 = pd.get_dummies(isp[["payment_type"]],columns=["payment_type"],dtype="int")
    isp = pd.concat([isp, dummy2], axis=1)
    isp = isp.drop(columns=["payment_type","contract_type"])
    
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

