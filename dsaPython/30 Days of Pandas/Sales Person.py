import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    red_com_ids = company[company["name"] == "RED"]["com_id"]
    red_orders = orders[orders["com_id"].isin(red_com_ids)]
    red_sales_ids = red_orders["sales_id"].unique()
    result_df = sales_person[~sales_person["sales_id"].isin(red_sales_ids)][["name"]]

    return result_df
    