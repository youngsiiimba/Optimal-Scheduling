# Optimal-Scheduling

## Creating virtual env
python3 -m venv env

## Activate virtual env
.\env\Scripts\activate

## In your enviroment install the dependecies 
pip install requirements.txt

## Send data to ThingsSpeak 
First change URL and insert your own API key
...then run:
python data2thingsspeak.py

## Send commands to Arduino
First run arduino code in the *receieveDataFromPython.ino* receieveDataFromPython folder
Then make sure the serial monitor in the Arduino IDE is closed
Finally run *python arduinoCommands.py* to send commands to the Arudino
