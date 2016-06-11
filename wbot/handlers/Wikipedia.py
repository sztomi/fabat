# -*- coding: utf8 -*-
import wikipedia

from wbot.handlers.HandlerBase import HandlerBase


class Wikipedia(HandlerBase):
    def execute(self, param):
        return wikipedia.summary(param, sentences=3)

    @property
    def help_text(self):
        return "Gets a wikipedia summary."
