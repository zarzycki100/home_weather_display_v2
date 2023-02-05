from grovepi import *
from math import isnan

from MeasurementValueObject import MeasurementValueObject


class DHTSensorReader:
    dht_sensor_port = None
    dht_sensor_type = None

    def __init__(self):
        self.dht_sensor_port = 7  # connect the DHt sensor to port 7
        self.dht_sensor_type = 0  # use 0 for the blue-colored sensor and 1 for the white-colored sensor

    def measure_temperature_and_humidity(self):

        measurement = dht(self.dht_sensor_port, self.dht_sensor_type)

        if isnan(measurement[0]) is True or isnan(measurement[1]) is True:
            self.measure_temperature_and_humidity()

        print("temp =", measurement[0], "\thumidity =", measurement[1], "%")

        return MeasurementValueObject(measurement)
