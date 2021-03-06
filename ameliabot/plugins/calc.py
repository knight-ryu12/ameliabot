"""
Overview
========
This plugin uses wolfram alpha to compute mathematical expressions.

Commands
========

Command: @calc expression
Description: Computes the expression using wolfram alpha.

Example
=======

<\tau> @calc integrate x^2
<\amelia>  integral x^2  dx = x^3/3+constant

"""

import wolframalpha

from untwisted.plugins.irc import send_msg
from untwisted.network import xmap
from ameliabot.cmd import regcmd
from ameliabot.tools import send_lines

class Calculate(object):
    def __init__(self, server, appid):
        self.client = wolframalpha.Client(appid)
        xmap(server, 'CMSG', self.calculate)
    
    @regcmd('@calc (?P<exp>.+)$')
    def calculate(self, server, nick, user, host, target, msg, exp):
        req  = self.client.query(exp)
        data = ''
        for pod in req:
            if pod.text:
                data = '%s %s' % (data, pod.text)
        send_lines(server, target, data)
    
install = Calculate








