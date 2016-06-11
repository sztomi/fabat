# -*- coding: utf8 -*-
import os

from wbot import RestClient
from wbot.handlers.HandlerBase import HandlerBase


class Cleverbot(HandlerBase):
    _CLEVERBOT_API_USER = os.environ['CLEVERBOT_API_USER']
    _CLEVERBOT_API_KEY = os.environ['CLEVERBOT_API_KEY']
    _URL = r'https://cleverbot.io/1.0/'

    def __init__(self):
        self._api = RestClient(self._URL, 'create', 'ask')
        self._nick = self._api.create(
            user=self._CLEVERBOT_API_USER,
            key=self._CLEVERBOT_API_KEY)['nick']

    def execute(self, param):
        response = self._api.ask(
            user=self._CLEVERBOT_API_USER,
            key=self._CLEVERBOT_API_KEY,
            nick=self._nick,
            text=param)['response']
        return response

    @property
    def help_text(self):
        return "Talks to cleverbot"
