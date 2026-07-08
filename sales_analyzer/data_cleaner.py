import pandas as pd

class DataCleaner:

    def __init__(self, dataframe):
        self.df = dataframe

    def clean_data(self):

        self.df.drop_duplicates(inplace=True)

        # Numeric columns
        numeric_cols = ["Quantity", "Price", "Discount"]

        for col in numeric_cols:
            if col in self.df.columns:
                self.df[col] = pd.to_numeric(self.df[col], errors="coerce")
                self.df[col] = self.df[col].fillna(self.df[col].mean())

        # Text columns
        for col in self.df.columns:
            if self.df[col].dtype == "object":
                self.df[col] = self.df[col].fillna("Unknown")

        return self.df

    def convert_date(self):
        if "Date" in self.df.columns:
            self.df["Date"] = pd.to_datetime(self.df["Date"])

        return self.df