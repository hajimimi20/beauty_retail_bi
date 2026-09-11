import os

import pandas as pd
import pymysql
from dotenv import load_dotenv


load_dotenv()


def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        charset="utf8mb4",
    )


def load_retail_sales(df: pd.DataFrame) -> None:
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        INSERT INTO retail_sales (
            category_code,
            category_name,
            sales_month,
            sales_value,
            seasonally_adjusted
        )
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            category_name = VALUES(category_name),
            sales_value = VALUES(sales_value)
    """

    try:
        for _, row in df.iterrows():
            cursor.execute(
                sql,
                (
                    row["category_code"],
                    row["category_name"],
                    row["sales_month"],
                    row["sales_value"],
                    row["seasonally_adjusted"],
                ),
            )

        connection.commit()

        print(f"Loaded {len(df)} records into MariaDB.")

    finally:
        cursor.close()
        connection.close()