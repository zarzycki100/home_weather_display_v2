import sqlite3
import os
from dotenv import load_dotenv

from sqlite3 import Error

from Logger import Logger
from MeasurementValueObject import MeasurementValueObject


class SQLiteConnector:
    connection = None

    def __init__(self):
        try:
            load_dotenv()

            self.connection = sqlite3.connect(os.getenv('SQLITE_DATABASE'))
        except Error as e:
            Logger.debug(e)

    def save_history(self, measurement):
        try:
            sql = ' INSERT INTO history (temperature, humidity) VALUES(?,?) '
            cur = self.connection.cursor()
            cur.execute(sql, measurement)
            self.connection.commit()

            return cur.lastrowid
        except Error as e:
            Logger.debug(e)

    def read_last_history(self):
        try:
            sql = ' SELECT temperature, humidity FROM history ORDER BY created_at DESC limit 1 '
            cur = self.connection.cursor()
            data = cur.execute(sql).fetchone()

            return MeasurementValueObject(data)
        except Error as e:
            Logger.debug(e)

