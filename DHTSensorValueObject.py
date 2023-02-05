from dataclasses import dataclass


@dataclass(frozen=True)
class DHTSensorValueObject:
    temperature: float
    humidity: float
