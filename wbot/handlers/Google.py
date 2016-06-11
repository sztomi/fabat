# -*- coding: utf8 -*-
import os
import pprint

from googleapiclient.discovery import build

from wbot.handlers.HandlerBase import HandlerBase


class Google(HandlerBase):
    _GOOGLE_CSE_KEY = os.environ['GOOGLE_CSE_KEY']
    _GOOGLE_CSE_CX = os.environ['GOOGLE_CSE_CX']

    def __init__(self):
        self._api = build('customsearch', 'v1', developerKey=self._GOOGLE_CSE_KEY)

    def execute(self, param):
        if not param or len(param) == 0:
            return "_Baszó kölyközöl engem?_"
        res = self._api.cse().list(
            q=param,
            num=1,
            cx=self._GOOGLE_CSE_CX
        ).execute()
        pprint.pprint(res)
        return ''.join([i['link'] + "\n"
                        for i in res['items']])

    @property
    def help_text(self):
        return "Seach Google and get the first two results."
