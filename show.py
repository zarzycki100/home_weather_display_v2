from time import sleep

from LCDScreenService import LCDScreenService
from SQLiteConnector import SQLiteConnector

sqlite = SQLiteConnector('/home/pi/home/pi/Dexter/GrovePi/Projects/000_AZ_Projects/home_weather_display_v2/hwd_sqlite_database')
measurement = sqlite.read_last_history()

lcd_screen_service = LCDScreenService()
lcd_screen_service.show_measurement(measurement)
lcd_screen_service.clear()
lcd_screen_service.show_outside_measurement()

