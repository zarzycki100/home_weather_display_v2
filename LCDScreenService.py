from time import sleep

from grove_rgb_lcd import *


class LCDScreenService:
    def __init__(self):
        setRGB(0, 255, 0)

    def show_measurement(self, measurement):
        try:
            t = str(measurement.temperature)
            h = str(measurement.humidity)

            setText_norefresh("Temp:" + t + "C\n" + "Humidity :" + h + "%")

            sleep(20)
        except (IOError, TypeError) as e:
            print(str(e))
            setText("")

    def clear(self):
        setText("")

        sleep(20)

    def show_outside_measurement(self):
        setText("outside \n weather!")

        sleep(20)


