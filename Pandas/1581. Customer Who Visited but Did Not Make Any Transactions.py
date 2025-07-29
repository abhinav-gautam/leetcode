# https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan-v2&envId=top-sql-50
import pandas as pd

data = [[1, 23], [2, 9], [4, 30], [5, 54], [6, 96], [7, 54], [8, 54]]
visits = pd.DataFrame(data, columns=["visit_id", "customer_id"]).astype(
    {"visit_id": "Int64", "customer_id": "Int64"}
)
data = [[2, 5, 310], [3, 5, 300], [9, 5, 200], [12, 1, 910], [13, 2, 970]]
transactions = pd.DataFrame(
    data, columns=["transaction_id", "visit_id", "amount"]
).astype({"transaction_id": "Int64", "visit_id": "Int64", "amount": "Int64"})


def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merge_df = pd.merge(visits, transactions, on="visit_id", how="left")
    no_txns = merge_df[merge_df["transaction_id"].isna()]
    grouped_no_txns = (
        no_txns.groupby("customer_id").size().reset_index(name="count_no_trans")
    )
    sorted_grouped = grouped_no_txns.sort_values(by="count_no_trans")
    return sorted_grouped


print(find_customers(visits, transactions))
