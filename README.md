# Optimal-Scheduling

An IoT solution to send microgrid data to and from ThingsSpeak
https://thingspeak.com/channels/1833675

We then use the data we obtain from the ThingsSpeak to calculate the minimum amount of power that we can use to satisfy the load. As well as the power sources that will be used.   

## Creating virtual env
python3 -m venv env

## Activate virtual env
.\env\Scripts\activate

## In your enviroment install the dependecies 
pip install -r requirements.txt

## Send data to and from ThingsSpeak to perform Optimal scheduling based on the load required 
First change URL and insert your own API key
...then run: *main.py* 

## Send commands to Arduino
First run the *receieveDataFromPython.ino* Arduino code in the receieveDataFromPython folder
Then make sure the serial monitor in the Arduino IDE is closed
Finally run *python arduinoCommands.py* to send commands to the Arudino
