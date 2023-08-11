import requests

config = {
    "rss": None
}

def req(js0n: dict=None, r=None):
    if js0n != None and isinstance(js0n, dict) and len(js0n) > 0:
        dummy = {
            "r": None,
            "method": None,
            "url": None,
            "params": None,
            "data": None,
            "headers": None,
            "aftermethod": None
        }
        if "r" in js0n and js0n["r"] != None:
            dummy["r"] = js0n["r"]
        else:
            if r != None:
                dummy["r"] = r
        if "method" in js0n and js0n["method"] != None:
            dummy["method"] = js0n["method"]
        if "url" in js0n and js0n["url"] != None:
            dummy["url"] = js0n["url"]
        if "params" in js0n and js0n["params"] != None:
            dummy["params"] = js0n["params"]
        if "data" in js0n and js0n["data"] != None:
            dummy["data"] = js0n["data"]
        if "headers" in js0n and js0n["headers"] != None:
            dummy["headers"] = js0n["headers"]
        if "aftermethod" in js0n and js0n["aftermethod"] != None:
            dummy["aftermethod"] = str(js0n["aftermethod"]).lower()
        if dummy["r"] != None and dummy["method"] != None and dummy["url"] != None and dummy["aftermethod"] != None:
            try:
                re = dummy["r"].request(
                    method=dummy["method"],
                    url=dummy["url"],
                    params=dummy["params"],
                    data=dummy["data"],
                    headers=dummy["headers"]
                )
            except Exception:
                re = None
            if re != None:
                out = None
                if dummy["aftermethod"] == "text":
                    out = re.text
                if dummy["aftermethod"] == "json":
                    out = re.json()
                if dummy["aftermethod"] == "content":
                    out = re.content
                if dummy["aftermethod"] == "re":
                    out = re
                return out

class Efood:
    def __init__(self):
        with requests.Session() as rss:
            self.rss = rss
        headers_config = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42",
        }  
        for header in headers_config:
            self.rss.headers[header] = headers_config[header]
        config["rss"] = self.rss
    class User:
        def __init__(self):
            self.rss = config["rss"]
        def register(self, email :str=None, password :str=None, firstName :str=None, lastName :str=None):
            if email != None and isinstance(email, str) and password != None and isinstance(password, str) and firstName != None and isinstance(firstName, str) and lastName != None and isinstance(lastName, str):
                data0 = req(
                    js0n={
                        "method": "post",
                        "url": "https://www.e-food.gr/api/auth/email/register",
                        "data": {
                            "email": email,
                            "password": password,
                            "firstName": firstName,
                            "lastName": lastName
                        },
                        "aftermethod": "json"
                    },
                    r=self.rss
                )
                return data0
        def login(self, email :str=None, password :str=None):
            if email != None and isinstance(email, str) and password != None and isinstance(password, str):
                data0 = req(
                    js0n={
                        "method": "post",
                        "url": "https://www.e-food.gr/api/auth/email/login",
                        "data": {
                            "email": email,
                            "password": password
                        },
                        "aftermethod": "json"
                    },
                    r=self.rss
                )
                if data0 != None and isinstance(data0, dict):
                    if "data" in data0 and data0["data"] != None and isinstance(data0["data"], dict):
                        if "session_id" in data0["data"] and data0["data"]["session_id"] != None and isinstance(data0["data"]["session_id"], str):
                            self.rss.headers["X-Core-Session-Id"] = data0["data"]["session_id"]
                        if "user" in data0["data"] and data0["data"]["user"] != None and isinstance(data0["data"]["user"], dict):
                            return data0["data"]["user"]
        def logout(self):
            if "X-Core-Session-Id" in self.rss.headers and self.rss.headers["X-Core-Session-Id"] != None:
                data0 = req(
                    js0n={
                        "method": "get",
                        "url": "https://api.e-food.gr/api/v1/user/logout",
                        "aftermethod": "json"
                    },
                    r=self.rss
                )
                if data0 != None and isinstance(data0, dict):
                    if "status" in data0 and data0["status"] != None and isinstance(data0["status"], str):
                        return data0["status"] == "ok"
        def reset_password(self, email :str=None):
            if email != None and isinstance(email, str):
                data0 = req(
                    js0n={
                        "method": "post",
                        "url": "https://api.e-food.gr/api/v1/user/reset_password",
                        "data": {
                            "email": email
                        },
                        "aftermethod": "json"
                    },
                    r=self.rss
                )
                if data0 != None and isinstance(data0, dict):
                    if "status" in data0 and data0["status"] != None and isinstance(data0["status"], str):
                        return data0["status"] == "ok"
        def password_token(self, token :str=None, new_password :str=None):
            if token != None and isinstance(token, str) and new_password != None and isinstance(new_password, str):
                data0 = req(
                    js0n={
                        "method": "post",
                        "url": "https://api.e-food.gr/api/v1/user/password/token",
                        "data": {
                            "token": token,
                            "new_password": new_password
                        },
                        "aftermethod": "json"
                    },
                    r=self.rss
                )
                if data0 != None and isinstance(data0, dict):
                    if "status" in data0 and data0["status"] != None and isinstance(data0["status"], str):
                        return data0["status"] == "ok"
        def account(self):
            if "X-Core-Session-Id" in self.rss.headers and self.rss.headers["X-Core-Session-Id"] != None:
                data0 = req(
                    js0n={
                        "method": "get",
                        "url": "https://api.e-food.gr/api/v1/user/account",
                        "aftermethod": "json"
                    },
                    r=self.rss
                )
                if data0 != None and isinstance(data0, dict):
                    if "data" in data0 and data0["data"] != None and isinstance(data0["data"], dict):
                        return data0["data"]
        def address(self, address_id :int=None):
            if "X-Core-Session-Id" in self.rss.headers and self.rss.headers["X-Core-Session-Id"] != None:
                data0 = req(
                    js0n={
                        "method": "get",
                        "url": f"https://api.e-food.gr/api/v1/user/clients/address{f'/{address_id}' if address_id != None and isinstance(address_id, int) else ''}",
                        "aftermethod": "json"
                    },
                    r=self.rss
                )
                if data0 != None and isinstance(data0, dict):
                    if "data" in data0 and data0["data"] != None and (isinstance(data0["data"], dict) or isinstance(data0["data"], list)):
                        return data0["data"][0] if isinstance(data0["data"], list) and len(data0["data"]) == 1 else data0["data"]
    class Restaurant:
        def __init__(self):
            self.rss = config["rss"]
        def all(self, latitude :float=None, longitude: float=None):
            if latitude != None and isinstance(latitude, float) and longitude != None and isinstance(longitude, float):
                data0 = req(
                    js0n={
                        "method": "get",
                        "url": "https://api.e-food.gr/api/v1/restaurants",
                        "params": {
                            "latitude": latitude,
                            "longitude": longitude,
                            "filters": {},
                            "mode": "filter",
                            "version": "3"
                        },
                        "aftermethod": "json"
                    },
                    r=self.rss
                )
                if data0 != None and isinstance(data0, dict):
                    if "data" in data0 and data0["data"] != None and isinstance(data0["data"], dict):
                        data1 = data0["data"]
                        if "restaurants" in data1 and data1["restaurants"] != None and isinstance(data1["restaurants"], list) and len(data1["restaurants"]) > 0:
                            return data0["data"]["restaurants"]
        def restaurant(self, shop_id :int=None):
            if shop_id != None and isinstance(shop_id, int):
                data0 = req(js0n={
                        "method": "get",
                        "url": f"https://api.e-food.gr/api/v1/restaurants/{shop_id}",
                        "aftermethod": "json"
                    },
                    r=self.rss
                )
                if data0 != None and isinstance(data0, dict):
                    if "data" in data0 and data0["data"] != None and isinstance(data0["data"], dict):
                        if "menu" in data0["data"] and data0["data"]["menu"] != None and isinstance(data0["data"]["menu"], dict):
                            return data0["data"]["menu"]
        def unique(self, shop_id :int=None):
            if shop_id != None and isinstance(shop_id, int):
                data0 = req(js0n={
                        "method": "get",
                        "url": "https://api.e-food.gr/v2/order/restaurant/unique",
                        "params": {
                            "restaurant_id": shop_id
                        },
                        "aftermethod": "json"
                    },
                    r=self.rss
                )
                if data0 != None and isinstance(data0, dict):
                    if "data" in data0 and data0["data"] != None and isinstance(data0["data"], list) and len(data0["data"]) > 0:
                        return data0["data"]
    class Shops:
        def __init__(self):
            self.rss = config["rss"]
        def ratings(self, shop_id :int=None, limit :int=20, offset :int=0):
            if shop_id != None and isinstance(shop_id, int) and limit != None and isinstance(limit, int) and offset != None and isinstance(offset, int):
                data0 = req(
                    js0n={
                        "method": "get",
                        "url": f"https://api.e-food.gr/v3/shops/ratings",
                        "params": {
                            "shop_id": shop_id,
                            "limit": limit,
                            "offset": offset
                        },
                        "aftermethod": "json"
                    },
                    r=self.rss
                )
                if data0 != None and isinstance(data0, dict):
                    if "data" in data0 and data0["data"] != None and isinstance(data0["data"], dict):
                        return data0["data"]
        def catalog(self, shop_id :int=None):
            if shop_id != None and isinstance(shop_id, int):
                data0 = req(
                    js0n={
                        "method": "get",
                        "url": f"https://api.e-food.gr/v3/shops/catalog",
                        "params": {
                            "shop_id": shop_id
                        },
                        "aftermethod": "json"
                    },
                    r=self.rss
                )
                if data0 != None and isinstance(data0, dict):
                    if "data" in data0 and data0["data"] != None and isinstance(data0["data"], dict):
                        if "menu" in data0["data"] and data0["data"]["menu"] != None and isinstance(data0["data"]["menu"], dict):
                            return data0["data"]["menu"]
        def chains(self, shop_id :int=None):
            if shop_id != None and isinstance(shop_id, int):
                data0 = req(
                    js0n={
                        "method": "get",
                        "url": f"https://api.e-food.gr/v3/shops/chains",
                        "params": {
                            "shop_id": shop_id
                        },
                        "aftermethod": "json"
                    },
                    r=self.rss
                )
                if data0 != None and isinstance(data0, dict):
                    if "data" in data0 and data0["data"] != None and isinstance(data0["data"], dict):
                        return data0["data"]
        def info(self, shop_id :int=None):
            if shop_id != None and isinstance(shop_id, int):
                data0 = req(
                    js0n={
                        "method": "get",
                        "url": f"https://api.e-food.gr/v3/shops/info",
                        "params": {
                            "shop_id": shop_id
                        },
                        "aftermethod": "json"
                    },
                    r=self.rss
                )
                if data0 != None and isinstance(data0, dict):
                    if "data" in data0 and data0["data"] != None and isinstance(data0["data"], dict):
                        return data0["data"]
    def homepage(self):
        data0 = req(
            js0n={
                "method": "get",
                "url": f"https://www.e-food.gr/api/homepage",
                "aftermethod": "json"
            },
            r=self.rss
        )
        if data0 != None and isinstance(data0, dict):
            if "data" in data0 and data0["data"] != None and isinstance(data0["data"], dict):
                return data0["data"]
    def search(self, latitude :float=None, longitude :float=None, terms :str=None):
        if latitude != None and isinstance(latitude, float) and longitude != None and isinstance(longitude, float) and terms != None and isinstance(terms, str):
            data0 = req(
                js0n={
                    "method": "get",
                    "url": f"https://api.e-food.gr/v2/disco/search",
                    "params": {
                        "lat": latitude,
                        "lon": longitude,
                        "terms": terms
                    },
                    "aftermethod": "json"
                },
                r=self.rss
            )
            if data0 != None and isinstance(data0, dict):
                if "data" in data0 and data0["data"] != None and isinstance(data0["data"], dict):
                    return data0["data"]