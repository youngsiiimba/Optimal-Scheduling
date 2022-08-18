
import urllib.request
import requests
import threading
import json

import random
import time
import pandas as pd


# Define a function that will post on server every 15 Seconds

def thingspeak_post(df):
    #threading.Timer(15,thingspeak_post).start()
    
    for i in range(df.shape[0]):
        tyd, solar_power, diesel_gen, battery_power, wind_power = data_extract(df, i)

        URl='https://api.thingspeak.com/update?api_key='
        KEY='MOOBKHKUNLXVCEEQ'
        HEADER='&field1={}&field2={}&field3={}&field4={}'.format(solar_power,diesel_gen, battery_power, wind_power)
        NEW_URL=URl+KEY+HEADER
        #print(NEW_URL)
        data=urllib.request.urlopen(NEW_URL)
        #print(data)
        read_data_thingspeak()
        time.sleep(0.5)
#####################################################

#####################################################
def read_data_thingspeak():
    #URL='https://api.thingspeak.com/channels/1833675/fields/1.json?api_key='
    URL='https://api.thingspeak.com/channels/1833675/feeds.json?api_key='
    KEY='EX7E2AQ928DYEUO7'
    HEADER='&results=1'
    NEW_URL=URL+KEY+HEADER
    #print(NEW_URL)

    get_data=requests.get(NEW_URL).json()
    #print(get_data)
    channel_id=get_data['channel']['id']
    #print(channel_id)
    feeds=get_data['feeds']
    #print(field_1)

    solar=[]
    diesel=[]
    battery=[]
    wind=[]

    for x in feeds:
        #print(x['field1'])
        solar.append(x['field1'])
        diesel.append(x['field2'])
        battery.append(x['field3'])
        wind.append(x['field4'])
    
    list_power = []
    list_power.append(solar[0])
    list_power.append(diesel[0])
    list_power.append(battery[0])
    list_power.append(wind[0])
    #print("Solar power (MW): ", solar)
    #print("Diesel power (MW): ", diesel)
    #print("Battery power (MW): ", battery)
    #print("Wind power (MW): ", wind)

    print("Most power: ", max(solar[0], diesel[0], battery[0], wind[0]), "MW")
    if(list_power.index(max(list_power)) == 0):
        cmd = 'solar'
        print("Solar power is now activated! Currently producing: ", max(solar[0], diesel[0], battery[0], wind[0]), "MW")
    elif (list_power.index(max(list_power)) == 1):
        cmd = 'diesel'
        print("Diesel generator is now activated! Currently producing: ", max(solar[0], diesel[0], battery[0], wind[0]), "MW")
    elif (list_power.index(max(list_power)) == 2):
        cmd = 'battery'
        print("Battery power is now activated! Currently producing: ", max(solar[0], diesel[0], battery[0], wind[0]), "MW")
    else:
        cmd = 'wind'
        print("Wind power is now activated! Currently producing: ", max(solar[0], diesel[0], battery[0], wind[0]), "MW")
    
    return cmd
#######################################################
#######################################################
def data_extract(df, i):
    df = df
    i = i
    tyd = df.iloc[i].values[0]
    solar_power = df.iloc[i].values[1]
    diesel_gen = df.iloc[i].values[2] 
    battery_power = df.iloc[i].values[3]
    wind_power = df.iloc[i].values[4]
    return tyd, solar_power, diesel_gen, battery_power, wind_power
#########################################################

if __name__ == '__main__':
    df = pd.read_excel('data\Microgrid Data.xlsx')
    thingspeak_post(df)


    read_data_thingspeak()