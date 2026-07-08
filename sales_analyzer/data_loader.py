import pandas as pd
import os


class DataLoader:

    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):

        if not os.path.exists(self.filepath):
            raise FileNotFoundError("File not found.")

        if self.filepath.endswith(".csv"):
            df = pd.read_csv(self.filepath)

        elif self.filepath.endswith(".xlsx"):
            df = pd.read_excel(self.filepath)

        else:
            raise ValueError("Unsupported file format.")

        return df