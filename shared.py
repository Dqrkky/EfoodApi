#https://gist.githubusercontent.com/Dqrkky/8484b1f246c3bc6e106680d22ef4b85c/raw/shared.py
import urllib

class Shared:
    def __init__(self, rss=None):
        self.rss = rss if rss != None else None  # noqa: E711
    def get_request_headers_json(self):
        if hasattr(self, "rss") and self.rss != None:  # noqa: E711
            return {
                d1: d2 for d1, d2 in self.rss.headers.items()
            }
    def set_request_headers(self, name :str=None, value :str=None):
        if hasattr(self, "rss") and self.rss != None:  # noqa: E711
            if name != None and value != None:  # noqa: E711
                self.rss.headers[name] = value
                return self.get_request_headers_json()
    def remove_request_headers(self, name :str=None):
        if hasattr(self, "rss") and self.rss != None:  # noqa: E711
            if name != None and name in self.get_request_headers_json():  # noqa: E711
                return {
                    "name": name,
                    "value": self.rss.headers.pop(name)
                }
    def convert_json_to_values(self, config :dict=None):
        if config != None and isinstance(config, dict):  # noqa: E711
            return (
                config["method"] if "method" in config and config["method"] != None else None,  # noqa: E711
                config["url"] if "url" in config and config["url"] != None else None,  # noqa: E711
                config["params"] if "params" in config and config["params"] != None else None,  # noqa: E711
                config["data"] if "data" in config and config["data"] != None else None,  # noqa: E711
                config["headers"] if "headers" in config and config["headers"] != None else None,  # noqa: E711
                config["cookies"] if "cookies" in config and config["cookies"] != None else None,  # noqa: E711
                config["files"] if "files" in config and config["files"] != None else None,  # noqa: E711
                config["auth"] if "auth" in config and config["auth"] != None else None,  # noqa: E711
                config["timeout"] if "timeout" in config and config["timeout"] != None else None,  # noqa: E711
                config["allow_redirects"] if "allow_redirects" in config and config["allow_redirects"] != None and isinstance(config["allow_redirects"], bool) else True,  # noqa: E711
                config["proxies"] if "proxies" in config and config["proxies"] != None else None,  # noqa: E711
                config["hooks"] if "hooks" in config and config["hooks"] != None else None,  # noqa: E711
                config["stream"] if "stream" in config and config["stream"] != None and isinstance(config["stream"], bool) else False,  # noqa: E711
                config["verify"] if "verify" in config and config["verify"] != None else None,  # noqa: E711
                config["cert"] if "cert" in config and config["cert"] != None else None,  # noqa: E711
                config["json"] if "json" in config and config["json"] != None else None,  # noqa: E711
            )
    def dtsup(self, config :dict=None):
        if config != None and isinstance(config, dict):  # noqa: E711
            return urllib.parse.urlencode(query=config)
    def construct(self, url :str=None, params :dict=None):
        if url != None and isinstance(url, str) and params != None and isinstance(params, dict):  # noqa: E711
            return f'{url}?{self.dtsup(config=params)}'