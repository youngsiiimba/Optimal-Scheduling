import pandas as pd
from data_extract import data_extract
from OptimalScheduling import optimal_scheduling, index2name
import numpy as np
import re 
df = pd.read_excel('data\Microgrid Data.xlsx')

def string_alphabetical_sorter(S):
    W = S.split(" ")
    W.sort()
    return ' '.join(W)


op = []
ops = []
df.head()
for i in range(0, df.shape[0]):
    list_power = []
    result = []
    tyd, solar_power, diesel_gen, battery_power, wind_power, load_profile = data_extract(df, i)
    list_power.append(solar_power)
    list_power.append(diesel_gen)
    list_power.append(battery_power)
    list_power.append(wind_power)
    output_power, result = optimal_scheduling(list_power, load_profile)
    sources = index2name(result, list_power)
  
    string_sources = str(" ").join(sources)
    #string_sources = re.sub(r"(\w)([A-Z])", r"\1 \2", string_sources[0])
    print(string_sources)
    string_sources = string_alphabetical_sorter(string_sources)
    print(string_sources)
    op.append(output_power)
    ops.append(string_sources)

    print(i)

df['Output power (MW)'] = op
df['Output power (Sources)'] = ops

print(df.head(10))
print(list(df['Output power (Sources)'].unique()))
df.to_excel(r'data\Machine Learning Microgrid Data.xlsx', index = None, header=True)
df.to_csv (r'data\Machine Learning Microgrid Data.csv', index = None, header=True)
