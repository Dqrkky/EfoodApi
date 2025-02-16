import requests
import json
import shared

class Efood:
    def __init__(self):
        with requests.Session() as rss:
            self.rss = rss
        self.shared = shared.Shared(
            rss=self.rss
        )
        headers_config = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "el",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "sec-ch-ua": "'Not A(Brand';v='8', 'Chromium';v='132', 'Google Chrome';v='132'",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "'Windows'",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "User-Agent": f"eFoodBot/1.0 (Python; Requests {requests.__version__}) https://github.com/Dqrkky/EfoodApi",
            "x-core-platform": "web",
            "x-core-version": "2.87.14"
        }
        self.rss.headers.update(headers_config)
        global config
        config = {
            "rss": self.rss,
            "shared": self.shared,
            "getaway": "https://api.e-food.gr"
        }
    class Request:
        def __init__(self):
            self.__dict__.update(config)
        def request(self, config :dict=None):
            if config != None and isinstance(config, dict):  # noqa: E711
                req = self.rss.request(
                    *self.shared.convert_json_to_values(
                        config=config
                    )
                )
                return req
    class User:
        def __init__(self):
            self.__dict__.update(config)
        def components(self, data :dict=None):
            if data != None and isinstance(data, dict):  # noqa: E711
                return {
                    "method": "post",
                    "url": f"{self.getaway}/v3/data/components",
                    "data": json.dumps(
                        obj=data
                    )
                }
        def orders(self, limit :int=5, offset :int=0):
            if limit != None and isinstance(limit, int) and \
            offset != None and isinstance(offset, int):  # noqa: E711
                return {
                    "method": "get",
                    "url": "https://www.e-food.gr/api/user/orders/history",
                    "params": {
                        "limit": limit,
                        "offset": offset,
                        "mode": "extended"
                    }
                }
        def register(self, email :str=None, password :str=None, firstName :str=None, lastName :str=None):
            if email != None and isinstance(email, str) and \
            password != None and isinstance(password, str) and \
            firstName != None and isinstance(firstName, str) and \
            lastName != None and isinstance(lastName, str):  # noqa: E711
                return {
                    "method": "post",
                    "url": f"{self.getaway}/api/auth/email/register",
                    "data": json.dumps(
                        obj={
                            "email": email,
                            "password": password,
                            "firstName": firstName,
                            "lastName": lastName
                        }
                    )
                }
        def login(self, email :str=None, password :str=None):
            if email != None and isinstance(email, str) and \
            password != None and isinstance(password, str):  # noqa: E711
                return {
                    "method": "post",
                    "url": "https://www.e-food.gr/api/auth/email/login",
                    "data": json.dumps(
                        obj={
                            "email": email,
                            "password": password
                        }
                    )
                }
        def logout(self):
            if "X-Core-Session-Id" in self.rss.headers and self.rss.headers["X-Core-Session-Id"] != None:  # noqa: E711
                return {
                    "method": "get",
                    "url": f"{self.getaway}/api/v1/user/logout"
                }
        def reset_password(self, email :str=None):
            if email != None and isinstance(email, str):  # noqa: E711
                return {
                    "method": "post",
                    "url": f"{self.getaway}/api/v1/user/reset_password",
                    "data": json.dumps(
                        obj={
                            "email": email
                        }
                    )
                }
        def password_token(self, token :str=None, new_password :str=None):
            if token != None and isinstance(token, str) and \
            new_password != None and isinstance(new_password, str):  # noqa: E711
                return {
                    "method": "post",
                    "url": f"{self.getaway}/api/v1/user/password/token",
                    "data": json.dumps(
                        obj={
                            "token": token,
                            "new_password": new_password
                        }
                    )
                }
        def account(self):
            if "X-Core-Session-Id" in self.rss.headers and self.rss.headers["X-Core-Session-Id"] != None:  # noqa: E711
                return {
                    "method": "get",
                    "url": f"{self.getaway}/api/v1/user/account"
                }
        def address(self, address_id :int=None):
            if "X-Core-Session-Id" in self.rss.headers and self.rss.headers["X-Core-Session-Id"] != None:  # noqa: E711
                return {
                    "method": "get",
                    "url": f"{self.getaway}/api/v1/user/clients/address{f'/{address_id}' if address_id != None and isinstance(address_id, int) else ''}"  # noqa: E711
                }
    class Restaurant:
        def __init__(self):
            self.__setattr__.__dict__.update(config)
        def all(self, latitude :float=None, longitude: float=None):
            if latitude != None and isinstance(latitude, float) and \
            longitude != None and isinstance(longitude, float):  # noqa: E711
                return {
                    "method": "get",
                    "url": f"{self.getaway}/api/v1/restaurants",
                    "params": {
                        "latitude": latitude,
                        "longitude": longitude,
                        "filters": {},
                        "mode": "filter",
                        "version": "3"
                    }
                }
        def restaurant(self, shop_id :int=None):
            if shop_id != None and isinstance(shop_id, int):  # noqa: E711
                return {
                    "method": "get",
                    "url": f"{self.getaway}/api/v1/restaurants/{shop_id}"
                }
        def unique(self, shop_id :int=None):
            if shop_id != None and isinstance(shop_id, int):  # noqa: E711
                return {
                    "method": "get",
                    "url": f"{self.getaway}/v2/order/restaurant/unique",
                    "params": {
                        "restaurant_id": shop_id
                    }
                }
    class Shops:
        def __init__(self):
            self.__setattr__.__dict__.update(config)
        def ratings(self, shop_id :int=None, limit :int=20, offset :int=0):
            if shop_id != None and isinstance(shop_id, int) and \
            limit != None and isinstance(limit, int) and \
            offset != None and isinstance(offset, int):  # noqa: E711
                return {
                    "method": "get",
                    "url": f"{self.getaway}/v3/shops/ratings",
                    "params": {
                        "shop_id": shop_id,
                        "limit": limit,
                        "offset": offset
                    }
                }
        def catalog(self, shop_id :int=None):
            if shop_id != None and isinstance(shop_id, int):  # noqa: E711
                return {
                    "method": "get",
                    "url": f"{self.getaway}/v3/shops/catalog",
                    "params": {
                        "shop_id": shop_id
                    }
                }
        def chains(self, shop_id :int=None):
            if shop_id != None and isinstance(shop_id, int):  # noqa: E711
                return {
                    "method": "get",
                    "url": f"{self.getaway}/v3/shops/chains",
                    "params": {
                        "shop_id": shop_id
                    }
                }
        def info(self, shop_id :int=None):
            if shop_id != None and isinstance(shop_id, int):  # noqa: E711
                return {
                    "method": "get",
                    "url": f"{self.getaway}/v3/shops/info",
                    "params": {
                        "shop_id": shop_id
                    }
                }
    def homepage(self):
        return {
            "method": "get",
            "url": f"{self.getaway}/api/homepage"
        }
    def search(self, latitude :float=None, longitude :float=None, terms :str=None):
        if latitude != None and isinstance(latitude, float) and \
        longitude != None and isinstance(longitude, float) and \
        terms != None and isinstance(terms, str):  # noqa: E711
            return {
                "method": "get",
                "url": f"{self.getaway}/v2/disco/search",
                "params": {
                    "lat": latitude,
                    "lon": longitude,
                    "terms": terms
                }
            }