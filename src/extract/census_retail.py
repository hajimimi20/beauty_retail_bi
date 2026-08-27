import os

import pandas as pd
import requests
from dotenv import load_dotenv


load_dotenv()

BASE_URL = "https://api.census.gov/data/timeseries/eits/mrts"
API_KEY = os.getenv("CENSUS_API_KEY")


def get_retail_sales(year: int = 2025) -> pd.DataFrame:
    params = {
        "get": (
            "data_type_code,"
            "time_slot_id,"
            "seasonally_adj,"
            "category_code,"
            "cell_value,"
            "error_data"
        ),
        "time": str(year),
        "key": API_KEY,
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    columns = data[0]
    rows = data[1:]

    return pd.DataFrame(rows, columns=columns)


if __name__ == "__main__":
    df = get_retail_sales()

    print("Total records:", len(df))
    print(df.head())