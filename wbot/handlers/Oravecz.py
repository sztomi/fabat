# -*- coding: utf8 -*-
import random
import re

from wbot.handlers.HandlerBase import HandlerBase


class Oravecz(HandlerBase):
    """
    Jól csak a szívével lát az ember.
    """

    def __init__(self):
        super().__init__()
        word_lists = {'fonev': Oravecz.load("assets/data/fonev.txt"),
                      'fonevbol': Oravecz.load("assets/data/fonevbol.txt"),
                      'foneve': Oravecz.load("assets/data/foneve.txt"),
                      'fonevvel': Oravecz.load("assets/data/fonevvel.txt"),
                      'ige_alanyi_e3': Oravecz.load("assets/data/ige_alanyi_e3.txt"),
                      'ige_targyas_e3': Oravecz.load("assets/data/ige_targyas_e3.txt"),
                      'jelzo': Oravecz.load("assets/data/jelzo.txt"),
                      'legjelzo': Oravecz.load("assets/data/legjelzo.txt"),
                      'ige_felszolito_e2': Oravecz.load("assets/data/ige_felszolito_e2.txt"),
                      'ige_felszolito_e3': Oravecz.load("assets/data/ige_felszolito_e3.txt"),
                      'fonevi_igenev': Oravecz.load("assets/data/fonevi_igenev.txt"),
                      'szerkezet': Oravecz.load("assets/data/szerkezet.txt")}
        self.word_lists = word_lists

    @staticmethod
    def load(file_name):
        return [line.strip() for line in open(file_name, "r")]

    def execute(self, param):
        return self.generate()

    @property
    def help_text(self):
        return self.generate()

    def generate(self):
        skeleton = random.choice(self.word_lists["szerkezet"]).split(' ')
        result = ""

        for word in skeleton:
            rgx = re.compile(r"\{(.+?)\}")
            match = re.search(rgx, word)
            if match and len(match.groups()) == 1:
                result += re.sub(rgx, random.choice(self.word_lists[match.group(1)]), word, count=1)
            else:
                result += word
            result += ' '

        return result[0].upper() + result[1:]
