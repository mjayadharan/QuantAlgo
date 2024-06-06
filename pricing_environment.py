import time
import pandas as pd

class PricingEnvironment:
    def __init__(self, name):
        self.name = name
        self.assets = {}

    def load_data_from_excel(self, file_names):
        for file_name in file_names:
            try:
                data = pd.read_excel(file_name + '.xlsx')
                asset_name = file_name.split('_')[0]
                # Convert 'Timestamp' column to datetime if not already
                if isinstance(data['Timestamp'].iloc[0], str):
                    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
                self.assets[asset_name] = data.set_index('Timestamp')['Open'].to_dict()
                print(f"Loaded data for asset '{asset_name}' from {file_name}.xlsx")
            except Exception as e:
                print(f"Error loading data from {file_name}.xlsx: {e}")

    def load_data_from_csv(self, file_names):
        for file_name in file_names:
            try:
                data = pd.read_csv(file_name + '.csv')
                asset_name = file_name.split('_')[0]
                # Convert 'Timestamp' column to datetime if not already
                if isinstance(data['Timestamp'].iloc[0], str):
                    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
                self.assets[asset_name] = data.set_index('Timestamp')['Open'].to_dict()
                print(f"Loaded data for asset '{asset_name}' from {file_name}.csv")
            except Exception as e:
                print(f"Error loading data from {file_name}.csv: {e}")

    def get_open_price_for_timestamp(self, timestamp):
        # Convert input timestamp to the format used in the loaded CSV files
        timestamp = pd.to_datetime(timestamp)
        open_prices = {}
        for asset, prices in self.assets.items():
            if timestamp in prices:
                open_prices[asset] = prices[timestamp]
            else:
                print(f"No data found for asset '{asset}' at timestamp '{timestamp}'")
        return open_prices
