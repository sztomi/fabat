# -*- coding: utf8 -*-
"""
Dispatches user queries.
"""


class Dispatcher(object):
    _handlers = {}

    HELP_QUERY = ['help', 'halp', '?', '???', '/?', '--help']

    def get_response(self, query):
        """
        Tries to parse a query and execute a handler if it exists.
        :param query: The query to parse. The first word is assumed to
        be the command, the rest is the parameter(s).
        :return: The result of the command or error_text.
        """
        cmd, params = query.split(' ', 1)
        if cmd in self.HELP_QUERY:
            return self.get_help()
        elif cmd in self._handlers:
            return self._handlers[cmd].execute(params)
        else:
            return self.error_text

    def register_handler(self, handler_class):
        """
        Registers a handler.
        :param handler_class: The class of the handler.
        :return:
        """
        self._handlers.append(handler_class.__name__, handler_class)

    @property
    def error_text(self):
        return "Csillagseggű székely gyerek!"

    def get_help(self):
        """
        Calls the police.
        :return: The concatenated help strings from all handlers.
        """
        return ''.join([handler.help_text
                        for _, handler in self._handlers])
