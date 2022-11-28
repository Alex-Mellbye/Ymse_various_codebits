# This is code for data imports and various data exploration bits

import pandas as pd
import numpy as np
from io import StringIO 

df1 = pd.read_csv(
        '../data/lcs_person.sdv', # the ".." signifies the working directory
        na_values={'.', ' .'},
        sep = ';'
        )

print(df1.isnull().sum()) # To get the number of missing for every column

# Display gives a better presentation than print - at least with tables.
display(pd.crosstab(df1.marital_status.fillna("Missing"), columns="Frequency", margins=True))


# Reloading the data, but this time Im assigning the columns dtypes through the uploading process
df3 = pd.read_csv(
        '../data/lcs_person.sdv',
        dtype={'hhid':'object', 'region':'object', 'rel_to_head':'object', 'sex':'object', 'marital_status':'object', 'occupation':'object'},
        na_values={'.', ' .'},
        sep = ';'
        )

print(df3.info())

# This line gives me income and age by region. In other words the descriptive statitvs of each regions' income and age
df3[['income', 'age']].groupby(df3['region']).describe()

# Here we are nesting a loc statement within a cross tab
display(pd.crosstab(df4.loc[df4['region'] == '4', 'toilet'], columns='Frequency', margins=True))


# Changing labels for column values. First I create a dictionary (columns) with their sub dictionaries (column values) in the "labels" object. 
# I then apply this to the dataset using the .replace() function. 

labels = { 'region':{ '1':'West', '2':'North', '3':'East', '4':'South'},

'rel_to_head':{ '1':'Head', '2':'Spouse', '3':'Daughter/Son', '4':'Grand child', '5':'Parent', '6':'Other relative', '7':'Non relative'},

'sex':{ '1':'Male', '2':'Female'},

'marital_status':{ '1':'Never married', '2':'Married', '3':'Widowed', '4':'Separated', '5':'Divorced', '8':'Not applicable (less than 12 yrs)'},

'occupation':{ '1':'Farmer with non-family employees', '2':'Farmer with only family members', '3':'Unpaid family farm worker', '4':'Non-farm employer with non-family employees', '5':'Non-farm employer with only family employees', '6':'Unpaid assistance in family enterprise', '7':'Self-Employed Independent contractor, technician, professional, etc', '8':'Wage Employee in Private Company (with contract)', '9':'Paid Employee in Private Company (without contract)', '10':'Wage Employee for Government', '11':'Wage Employee in Parastatal (government owned company)', '12':'Casual/Day Laborer', '13':'Intern/free labor/voluntary work', '14':'Home maker', '15':'Was not working, but was looking for work and has worked previously', '16':'Was not working, but was looking for work. Has never worked before', '17':'Was not working, and was not looking for work', '18':'Student', '19':'Retired/pensioner', '20':'Was not working because of disability or chronical illness'},

'dwelling_type':{ '1':'A single house occupied by one household dwelling', '2':'A house occupied by multiple households', '3':'Multi-storied building with one household', '4':'Multi-storied building with more households', '5':'Group of enclosed dwellings: multiple households', '6':'Group of enclosed dwellings occupied by a single household', '7':'Other'},

'own_dwelling':{ '1':'Yes', '2':'No'},

'toilet':{ '1':'No toilet', '2':'Pit latrine without slab/Open pit', '3':'Pit latrine with slab (not washable)', '4':'Pit latrine with slab (washable)', '5':'VIP', '6':'Pour flush', '7':'Flush toilet', '8':'Ecosan', '9':'Other'},

'drinkingwater_source':{ '1':'Tap water within the household', '2':'Tap water within the neighbouring household', '3':'Community tap water', '4':'Deep driiled well', '5':'Covered well', '6':'Uncovered well', '7':'Taped/captured spring', '8':'Untaped spring', '9':'Rain water', '10':'Mineral bottled water', '11':'Vendors water (Bucket)', '12':'River/lake/Dam water', '13':'Nyingine, taja'},

'energy_source':{ '1':'Collected firewood', '2':'Purchased firewood', '3':'Grass', '4':'Paraffin', '5':'Electricity', '6':'Gas', '7':'Battery/dry cell torch', '8':'Candles'}}

df3_noduprec = df3_noduprec.replace(labels)
df3_noduprec

# Changing categorical column types to "category" as opposed to "object". This type is better for storing data. 

df3_noduprec = df3_noduprec.astype({            'region': 'category',
                                                'rel_to_head': 'category',
                                                'sex': 'category',
                                                'marital_status': 'category',
                                                'occupation': 'category',
                                               }
                                              )

df3_noduprec.info()


# Working with strings
df4_nodup['own_dwelling_1'] = df4_nodup['own_dwelling'].str[:1].str.lower() # Makes the first position lower case
df4_nodup['own_dwelling_2'] = df4_nodup['own_dwelling'].str.replace('y', '1').str.replace('n', '0') # Change all y's to 1s and n's to 0s
df4_nodup['drinkingwater_t'] = df4_nodup['drinkingwater_source'].str.lower().str.count('t') # Make all Ts lower case and count them
df4_nodup['dwelling_type_find'] = df4_nodup['dwelling_type'].str.find('o') # Find the first posision of the letter "o"
df4_nodup['dwelling_type_rfind'] = df4_nodup['dwelling_type'].str.rfind('o') # Find the last posisjon of the letter "0" 
df4_nodup['own_dwelling_3'] = df4_nodup['own_dwelling'].str.endswith('es') # Creates a boolean variable which is True if the original variable ends with "es"
