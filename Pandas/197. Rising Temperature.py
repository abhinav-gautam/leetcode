# https://leetcode.com/problems/rising-temperature/description/?envType=study-plan-v2&envId=top-sql-50

import pandas as pd

data = [
    [1, "2015-01-01", 10],
    [2, "2015-01-02", 25],
    [3, "2015-01-03", 20],
    [4, "2015-01-04", 30],
]
weather = pd.DataFrame(data, columns=["id", "recordDate", "temperature"]).astype(
    {"id": "Int64", "recordDate": "datetime64[ns]", "temperature": "Int64"}
)


def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by="recordDate", inplace=True)
    weather["date_diff"] = weather["recordDate"].diff().dt.days
    weather["temp_diff"] = weather["temperature"].diff()
    return pd.DataFrame(
        weather[(weather["date_diff"] == 1) & (weather["temp_diff"] > 0)]["id"]
    )


print(rising_temperature(weather))
