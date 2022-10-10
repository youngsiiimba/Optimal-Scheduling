
import urllib.request
import requests
import threading
import json

import random
import time
import pandas as pd

from OptimalScheduling import optimal_scheduling, index2name
from data_extract import data_extract

# Define a function that will post on server every 15 Seconds
def thingspeak_post(df):
    #threading.Timer(15,thingspeak_post).start()
    for i in range(0, df.shape[0]):
        tyd, solar_power, diesel_gen, battery_power, wind_power, load_profile = data_extract(df, i)

        URl='https://api.thingspeak.com/update?api_key='
        KEY='MOOBKHKUNLXVCEEQ'
        HEADER='&field1={}&field2={}&field3={}&field4={}&field5={}'.format(solar_power,diesel_gen, battery_power, wind_power, load_profile)
        NEW_URL=URl+KEY+HEADER
        data=urllib.request.urlopen(NEW_URL)
        read_data_thingspeak()
        time.sleep(0.5)
#####################################################

#Function to collect data from ThingsSpeak  
def read_data_thingspeak():
    URL='https://api.thingspeak.com/channels/1833675/feeds.json?api_key='
    KEY='EX7E2AQ928DYEUO7'
    HEADER='&results=1'
    NEW_URL=URL+KEY+HEADER

    get_data=requests.get(NEW_URL).json()
    channel_id=get_data['channel']['id']
    feeds=get_data['feeds']


    solar=[]
    diesel=[]
    battery=[]
    wind=[]
    load=[]

    for x in feeds:
        solar.append(x['field1'])
        diesel.append(x['field2'])
        battery.append(x['field3'])
        wind.append(x['field4'])
        load.append(x['field5'])
    
    list_power = []
    list_load = []
    list_power.append(solar[0])
    list_power.append(diesel[0])
    list_power.append(battery[0])
    list_power.append(wind[0])
    list_load.append(load[0])
    
    list_power = [float(j) for j in list_power]
    list_load = [float(k) for k in list_load]
    
    print("Available power:", list_power, "| Load required:", list_load[0], "MW")
    output_power, result= optimal_scheduling(list_power,list_load[0])
    sources = index2name(result, list_power)
    print("Power being produced is: ", output_power, "MW, from the following sources", sources)
    print("")

    #print("Most power: ", max(solar[0], diesel[0], battery[0], wind[0]), "MW")
    #if(list_power.index(max(list_power)) == 0):
    #    cmd = 'solar'
    #    print("Solar power is now activated! Currently producing: ", max(solar[0], diesel[0], battery[0], wind[0]), "MW")
    #elif (list_power.index(max(list_power)) == 1):
    #    cmd = 'diesel'
    #    print("Diesel generator is now activated! Currently producing: ", max(solar[0], diesel[0], battery[0], wind[0]), "MW")
    #elif (list_power.index(max(list_power)) == 2):
    #    cmd = 'battery'
    #    print("Battery power is now activated! Currently producing: ", max(solar[0], diesel[0], battery[0], wind[0]), "MW")
    #else:
    #    cmd = 'wind'
    #    print("Wind power is now activated! Currently producing: ", max(solar[0], diesel[0], battery[0], wind[0]), "MW")
    #return cmd

#######################################################


if __name__ == '__main__':
    df = pd.read_excel('data\Microgrid Data.xlsx')
    thingspeak_post(df)
    read_data_thingspeak()