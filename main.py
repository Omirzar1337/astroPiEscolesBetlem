from sense_hat import SenseHat
from time import sleep
import datetime as dt
import os

dir_path = "/home/pi"
sensor = SenseHat()
sensor.clear()

sensor.show.message("Hello from Escoles Betlem")

fileName = "dades.csv"
file = open(dir_path+"/"+fileName, "w")

initTime = dt.datetime.now()
sensor.show_message("Settings enviroment")
#total duration of the data gathering process
duration = 160
#time interval between each sensor mesure
interval = 0.2

csv_titles = ["Date and Time", "Temperature C", "Pressure", "Humidity"]
file.writelines(csv_titles)
iteration = 0
while dt.datetime.now() < (initTime + dt.timedelta(minutes=duration)):

    #messages for knowing if it is working
    if (iteration % 500) == 0:
        sensor.show_message("Measuring...")
    
    #Taking values form sensors
    temp = sensor.get_temperature()
    press  =sensor.get_pressure()
    humit = sensor.get_humidity()
    measure_time = dt.datetime.now()
    accel = sensor.get_accelerometer_raw()

    measures_string = ["\n","," + str(measure_time) + ",", str(temp) + ",", str(press) + ",", str(humit) + ",", str(accel + ",","\n")]

    file.writelines(measures_string)
    iteration = iteration + 1
    sleep(interval)

file.close()

sensor.show_message("Good Bye ISS. Wish you have a nice fly")