import sqlite3
from pathlib import Path

import pandas as pd


conn = sqlite3.connect(Path(__file__).with_name("data.sqlite"))

try:
    df_first_five = pd.read_sql(
        "SELECT employeeNumber, lastName FROM employees", conn
    )
    df_five_reverse = pd.read_sql(
        "SELECT lastName, employeeNumber FROM employees", conn
    )
    df_alias = pd.read_sql(
        "SELECT lastName, employeeNumber AS ID FROM employees", conn
    )
    df_executive = pd.read_sql(
        """
        SELECT CASE
            WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing') THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
        FROM employees
        """,
        conn,
    )
    df_name_length = pd.read_sql(
        "SELECT LENGTH(lastName) AS name_length FROM employees", conn
    )
    df_short_title = pd.read_sql(
        "SELECT SUBSTR(jobTitle, 1, 2) AS short_title FROM employees", conn
    )
    sum_total_price = pd.read_sql(
        "SELECT ROUND(priceEach * quantityOrdered) AS total_price FROM orderDetails",
        conn,
    ).sum()
    df_day_month_year = pd.read_sql(
        """
        SELECT orderDate,
               STRFTIME('%d', orderDate) AS day,
               STRFTIME('%m', orderDate) AS month,
               STRFTIME('%Y', orderDate) AS year
        FROM orders
        """,
        conn,
    )
finally:
    conn.close()
