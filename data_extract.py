def data_extract(df, i):
    df = df
    i = i
    tyd = df.iloc[i].values[0]
    solar_power = df.iloc[i].values[1]
    diesel_gen = df.iloc[i].values[2] 
    battery_power = df.iloc[i].values[3]
    wind_power = df.iloc[i].values[4]
    load_profile = df.iloc[i].values[5]
    return tyd, solar_power, diesel_gen, battery_power, wind_power, load_profile
