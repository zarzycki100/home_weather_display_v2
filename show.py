from LCDScreenService import LCDScreenService
from SQLiteConnector import SQLiteConnector

sqlite = SQLiteConnector()
measurement = sqlite.read_last_history()

lcd_screen_service = LCDScreenService()
lcd_screen_service.show_measurement(measurement)
lcd_screen_service.clear()
lcd_screen_service.show_outside_measurement()

