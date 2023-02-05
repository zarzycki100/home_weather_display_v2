from DHTSensorReader import DHTSensorReader
from SQLiteConnector import SQLiteConnector

dht_sensor_reader = DHTSensorReader()
measurement = dht_sensor_reader.measure_temperature_and_humidity()

sqlite = SQLiteConnector('/home/pi/home/pi/Dexter/GrovePi/Projects/000_AZ_Projects/home_weather_display_v2/hwd_sqlite_database')
sqlite.save_history((measurement.temperature, measurement.humidity))
