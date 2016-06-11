# -*- coding: utf8 -*-
import os
import random

import flickrapi

from wbot.handlers.HandlerBase import HandlerBase


class Flickr(HandlerBase):
    def __init__(self):
        _FLICKR_KEY = os.environ['FLICKR_KEY']
        _FLICKR_SECRET = os.environ['FLICKR_SECRET']
        self._flickr = flickrapi.FlickrAPI(_FLICKR_KEY,
                                           _FLICKR_SECRET, format='parsed-json')

    def execute(self, param):
        search_tags = param.replace(' ;', ',')
        result = random.choice(
            self._flickr.photos.search(
                tags=search_tags,
                extras='url_m')['photos']['photo'])
        return result['url_m']

    @property
    def help_text(self):
        return "Gets a random picture from flickr that contains the given tags"
