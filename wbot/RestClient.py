# -*- coding: utf8 -*-
import json
from urllib.parse import urljoin

import requests


class RestClient(object):
    """
    Universal REST client.
    """

    class _callProxy(object):
        def __init__(self, base_url, name):
            self.url = urljoin(base_url, name)

        def __call__(self, *args, **kwargs):
            result = requests.post(self.url, data=kwargs)
            return json.loads(result.text)

    def __init__(self, base_url, *functions):
        """
        Initializes a RestClient.
        :param base_url: The base url to make calls to. No trailing / required
        """
        self.base_url = base_url
        self.proxies = {}
        for f in functions:
            self.proxies[f] = RestClient._callProxy(self.base_url, f)

    def __getattr__(self, item):
        if item in self.proxies:
            return self.proxies[item]
        return self.__dict__[item]
