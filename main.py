from DHTSensorReader import DHTSensorReader
from Logger import Logger
from SQLiteConnector import SQLiteConnector

dht_sensor_reader = DHTSensorReader()
measurement = dht_sensor_reader.measure_temperature_and_humidity()

sqlite = SQLiteConnector()
sqlite.save_history((measurement.temperature, measurement.humidity))