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
        cmd, *params = query.split(' ', 1)
        cmd = cmd.lower()
        if cmd in self.HELP_QUERY:
            return self.get_help()
        elif cmd in self._handlers:
            return self._handlers[cmd].execute(params[0] if len(params) > 0 else '')
        else:
            return self.error_text

    def register_handler(self, handler_class):
        """
        Registers a handler.
        :param handler_class: The class of the handler.
        :return:
        """
        self._handlers[handler_class.__name__.lower()] = handler_class()

    @property
    def error_text(self):
        return "Csillagseggű székely gyerek!"

    def get_help(self):
        """
        Calls the police.
        :return: The concatenated help strings from all handlers.
        """
        return ''.join(['*{}*: '.format(name) + handler.help_text + "\n"
                        for name, handler
                        in iter(sorted(self._handlers.items()))])
