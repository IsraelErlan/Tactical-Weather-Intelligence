import pandas as pd
import numpy as np


class WeatherData:

    def __init__(self, weather_list: list[dict]):
        self.df = pd.DataFrame(weather_list)

    @classmethod
    def create_and_run(cls, weather_list):
        instance = cls(weather_list)
        return instance.run_all()

    def run_all(self):
        self.delete_duplicates()
        self.remove_null_values()
        self.add_col_temperature_category()
        self.add_col_wind_status()
        return self.to_json()

    def delete_duplicates(self):
        self.df = self.df.drop_duplicates()

    def remove_null_values(self):
        self.df = self.df.dropna()

    def add_col_temperature_category(self):
        self.df['temperature_category'] = pd.cut(self.df['temperature'],
                                                 bins=[-np.inf, 18, 25, np.inf],
                                                 labels=['cold', 'moderate', 'hot'])

    def add_col_wind_status(self):
        self.df['wind_status'] = pd.cut(self.df['wind_speed'],
                                        bins=[-np.inf, 10, np.inf],
                                        labels=['calm', 'windy'])

    def to_json(self):
        data = self.df.to_dict(orient='records')
        return data
