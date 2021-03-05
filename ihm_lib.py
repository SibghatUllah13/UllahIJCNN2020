import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import sys
import re
sys.path.insert(0, os.getcwd()[:-4])
from mimic3benchmark.readers import DecompensationReader
from mimic3benchmark.readers import InHospitalMortalityReader
from mimic3benchmark.readers import LengthOfStayReader
from mimic3benchmark.readers import PhenotypingReader
from mimic3benchmark.readers import MultitaskReader

''' Count Number of Episodes for each SUBJECT'''
def count_episodes(train_data):
    episodes = [ train_data[i]['name'].split('_')[:2] for i in range(len(train_data)) ]
    episodes = pd.DataFrame(np.array(episodes))
    episodes.columns = ['SUBJECT_ID','EPISODE #']
    return episodes.groupby('SUBJECT_ID').count()

''' Mathc Subject ID and ICU Stays ID'''
def return_icu_ids(subject,episodes,all_stays):
    if (episodes.loc[subject]['EPISODE #'] ==1):
        return list(all_stays[all_stays['SUBJECT_ID']==int(subject)].ICUSTAY_ID)
    else :
        return sorted(list(all_stays[all_stays['SUBJECT_ID']==int(subject)].ICUSTAY_ID))

''' Extract Diagnosis for a single ICU Stay '''
def extract_diagnosis(index, train_data, diag, epi):
    subject, episode = train_data[index]['name'].split('_')[:2]
    temp = diag[(diag['SUBJECT_ID']==int(subject))].sort_values('ICUSTAY_ID')
    return sorted(temp[temp['ICUSTAY_ID']==sorted(temp['ICUSTAY_ID'].unique())[int(re.findall(r'\d+', episode)[0])-1]].ICD9_CODE)

''' Get Binary Representation of a Patients Diagnostics'''
def binary_representation(all_dis,pres_dis):
    return np.array(np.isin(all_dis,pres_dis),dtype=int)

''' Extract Training Data Set of a single ICU Stay'''
def convert_pandas(index, train_data):
    X = pd.DataFrame(train_data[index]['X'])
    X.columns = train_data[index]['header']
    return X

''' Convert Categorical Variables into Numerical'''
def convert_categorical(X):
    cat_columns = ['Capillary refill rate','Glascow coma scale eye opening', 'Glascow coma scale motor response','Glascow coma scale total','Glascow coma scale verbal response']
    X[cat_columns] = X[cat_columns].astype('category')
    X[cat_columns] = X[cat_columns].apply(lambda x: x.cat.codes)
    return X

''' Extract Unique Values of all Categorical Variables from an ICU Stay'''
def extract_categories(X):
    return X['Capillary refill rate'].unique(),X['Glascow coma scale eye opening'].unique(),X['Glascow coma scale motor response'].unique(),X['Glascow coma scale total'].unique(),X['Glascow coma scale verbal response'].unique()

''' Extract String'''
def extract_string(index,train_data,column_name):
    a = list(np.unique(train_data[index][str(column_name)]))
    return [a[i] for i in range(len(a)) if a[i]]


''' Encode Categorical Variables to Numerical'''
def encode_cat(index, column, data, encoding, decoding):
    a = np.array(data[index][column])
    indices = [i for i in range(len(a)) if np.array(a)[i]]
    for k in range(len(indices)):
        a[indices[k]] = decoding[[j for j, e in enumerate(encoding) if e == a[indices[k]]][0]]
    return pd.Series(a)

''' Fill Out Missing Values with NANs'''
def fill_missing(index, data):
    for k in range(data[index].shape[1]):
        a = list(data[index].iloc[:,k])
        for i in range(len(a)):
            if not a[i]:
                a[i] = np.nan
        data[index].iloc[:,k] = pd.Series(np.round(np.array(a,dtype=float),2))
    return data[index]
