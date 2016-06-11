# -*- coding: utf8 -*-
from abc import ABCMeta, abstractmethod, abstractproperty


class HandlerBase(metaclass=ABCMeta):
    """
    The base class for all handlers.
    """

    def __init__(self):
        pass

    @abstractmethod
    def execute(self, param):
        # type: (str) -> str
        """
        Executes the handler.
        :param param: The parameter passed to the handler
        (i.e. the rest of the query)
        :return: String response of the handler.
        """
        pass

    @abstractproperty
    def help_text(self):
        # type: () -> str
        """
        :return: The help text for this handler.
        """
        pass
