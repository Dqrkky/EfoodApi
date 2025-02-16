import efoodgr
import json  # noqa: F401
import os

ee = efoodgr.Efood()

re = ee.Request()
use = ee.User()

headers_config = {
    "x-core-session-id": "<set-session-id>"
}
re.rss.headers.update(headers_config)
os.system("cls")
print(
    "Hello, " +
    re.request(
        use.account()
    ).json()["data"]["first_name_in_vocative"]
)

last_order = re.request(use.orders(limit=1)).json()["data"]["orders"][0]

tab = "    "
print(f'Last Order\n{tab}Items : {", ".join([order["name"] for order in last_order["products"]])}\n{tab}Place : {last_order["restaurant"]["name"]}\n{tab}Price : {last_order["price"]}€')