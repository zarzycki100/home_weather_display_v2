class MeasurementValueObject:
    temperature = None
    humidity = None

    def __init__(self, dht_sensor_measurement):
        self.temperature = dht_sensor_measurement[0]
        self.humidity = dht_sensor_measurement[1]
