import time
import pandas as pd
# !pip install azure-iot-hub
from azure.iot.device import IoTHubDeviceClient, Message
#Create an IoT Hub from the Azure portal, then in your IoT Hub click on "Devices" in the side panel and create a new device.
#After creating your device, copy and paste the connection string for your device here
#CONNECTION_STRING = "HostName=microgrid.azure-devices.net;DeviceId=micro-grid;SharedAccessKey=otk0lR0W2GcNX+f58d6p/WUSs7Jdq5/IwC+TBkyqSuM="
#CONNECTION_STRING = "HostName=optimal-scheduling.azure-devices.net;DeviceId=smarr-microgrid;SharedAccessKey=8YQ91Hh3gCfrExpswiJ9350my+ftE4iF+EeHDKTnnX0="

####IoT centrl#########
CONNECTION_STRING = "HostName=microgridiotcentral.azureiotcentral.com;DeviceId=microgrid;SharedAccessKey=87YTuW/3EJ3hUWvsA/yE3hsMjkiocCTnH3IoB1hjQS0="
MSG_TXT = '{{"Time": {tyd}, "Solar Power(MW)": {solar_power}, "Diesel Generator(MW)": {diesel_gen}, "Battery Power(MW)": {battery_power}, "Wind Power(MW)": {wind_power} }}'

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def iothub_client_telemetry(client, df):
    client.connect() 
    print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

    for i in range(df.shape[0]):
        tyd, solar_power, diesel_gen, battery_power, wind_power = data_extract(df, i)


        #format the message for Azure IoT Hub
        msg_text_formatted = MSG_TXT.format(tyd=tyd, solar_power=solar_power, diesel_gen=diesel_gen, battery_power=battery_power, wind_power=wind_power)
        message = Message(msg_text_formatted)

                # Add a custom application property to the message.
                # An IoT hub can filter on these properties without access to the message body.
            #  if temperature > 30:
            #    message.custom_properties["temperatureAlert"] = "true"
            #  else:
            #    message.custom_properties["temperatureAlert"] = "false"

            # Send the message.
        print( "Sending message: {}".format(message) )
        client.send_message(message)
        client.connect()
        print ( "Message successfully sent.")
        time.sleep(10)
    
def data_extract(df, i):
    df = df
    i = i
    tyd = df.iloc[i].values[0]
    solar_power = df.iloc[i].values[1]
    diesel_gen = df.iloc[i].values[2] 
    battery_power = df.iloc[i].values[3]
    wind_power = df.iloc[i].values[4]
    return tyd, solar_power, diesel_gen, battery_power, wind_power

def main():
    client = iothub_client_init()
    df = pd.read_excel('data\Microgrid Data.xlsx')
    
    try:
        iothub_client_telemetry(client,df)
    except KeyboardInterrupt:
        print("IoTHubClient sample stopped by user")
    finally:
        # Upon application exit, shut down the client
        print("Shutting down IoTHubClient")
        client.shutdown()

    # Run Sample
    try:
        run_telemetry_sample(client)
    except KeyboardInterrupt:
        print("IoTHubClient sample stopped by user")
    finally:
        # Upon application exit, shut down the client
        print("Shutting down IoTHubClient")
        client.shutdown()

if __name__ == '__main__': 
    main()
    