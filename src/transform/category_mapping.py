import pandas as pd


CATEGORY_MAPPING = {
    "446": "Health and Personal Care Stores",
    "44611": "Pharmacies and Drug Stores",
}


def map_retail_categories(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter Census MRTS data for beauty-related retail categories
    and add readable category names.
    """

    df = df.copy()

    # Keep beauty-related retail categories
    df = df[df["category_code"].isin(CATEGORY_MAPPING)]

    # Keep monthly sales only
    df = df[df["data_type_code"] == "SM"]

    # Keep seasonally adjusted data
    df = df[df["seasonally_adj"] == "yes"]

    # Add readable category names
    df["category_name"] = df["category_code"].map(CATEGORY_MAPPING)

    return df