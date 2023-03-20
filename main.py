from sense_hat import SenseHat
from time import sleep
import datetime as dt
import os

## Code designed to get data from astrPi's sense hat

# Definition of our data storage
dir_path = "/home/pi"
fileName = "data.csv"
file = open(dir_path + "/" + fileName, "w")

# Pointing sense hat with a local reference and cleaning sense hat
sensor = SenseHat()
sensor.clear()

# Salute message
sensor.show.message("Hello from Escoles Betlem")


# Definition of timeMarks and intervals
initTime = dt.datetime.now()
sensor.show_message("Settings enviroment")
duration = 160
interval = 0.2

# Definement of csv format
csv_titles = ["Date and Time", "Temperature C", "Pressure", "Humidity"]
file.writelines(csv_titles)
iteration = 0

# Writing code block
while dt.datetime.now() < (initTime + dt.timedelta(minutes=duration)):

    # Feedback messages
    if (iteration % 500) == 0:
        sensor.show_message("Measuring...")
    
    # Taking values from sensors
    temp = sensor.get_temperature()
    press  =sensor.get_pressure()
    humit = sensor.get_humidity()
    measure_time = dt.datetime.now()
    accel = sensor.get_accelerometer_raw()

    # Writing new line in the file
    measures_string = ["\n","," + str(measure_time) + ",", str(temp) + ",", str(press) + ",", str(humit) + ",", str(accel + ",","\n")]
    file.writelines(measures_string)

    # Iteration counter and sleeping
    iteration =+ 1
    sleep(interval)

# Closing file
file.close()

# Showing final message
sensor.show_message("Good Bye ISS. Wish you have a nice fly")