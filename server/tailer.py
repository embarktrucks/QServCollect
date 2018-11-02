#!/usr/bin/env python
import sys
import os
import re
from slackclient import SlackClient

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

game = os.environ["GAME"]

class Server(object):
    def __init__(self):
        self.players = 0
        self.color = '#ffffff'
        self.game = 'none'

    def send(self, message, attachments = None):
        sc.api_call(
            "chat.postMessage",
            channel="lan-party",
            text=message,
            attachments=attachments,
        )

    def player_change(self, message):
        message = '%s (%d player(s) in game.)' % (message, self.players)
        attachments = {
            "fallback": message,
            "color": self.color,
            "title": self.title or self.game,
            "text": message,
        }
        self.send(message='', attachments=[attachments])

    def connected(self, message):
        """ Return True if the message is a connection message. """
        return False

    def disconnected(self, message):
        """ Return True if the message is a disconnection message. """
        return False

    def handle(self, message):
        if self.connected(message):
            self.players += 1
            self.player_change("Player joined the game!")
            return

        if self.disconnected(message):
            self.players -= 1
            self.player_change("Player left the game!")
            return

class Sauerbraten(Server):
    def __init__(self):
        super(Sauerbraten, self).__init__()
        self.color = '#aa4a00'
        self.game = 'sour'
        self.title = 'Sauerbraten'

    def connected(self, message):
        return 'connected from' in message

    def disconnected(self, message):
        return 'Leave' in message

class Tron(Server):
    def __init__(self):
        super(Tron, self).__init__()
        self.color = '#00f2ff'
        self.game = 'tron'
        self.title = 'Tron'

    def connected(self, message):
        return 'Received login' in message

    def disconnected(self, message):
        return 'received logout' in message

class TeeWorlds(Server):
    def __init__(self):
        super(TeeWorlds, self).__init__()
        self.color = '#b1b700'
        self.game = 'tee'
        self.title = 'TeeWorlds'

    def connected(self, message):
        name = re.search('\'(\w+)\'', message)
        return 'entered and joined the game' in message

    def disconnected(self, message):
        return 'has left the game' in message

handlers = [
        TeeWorlds(),
        Sauerbraten(),
        Tron()
        ]

handler = next(x for x in handlers if x.game == game)

while True:
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        break

    if not line:
        break

    handler.handle(line)

    sys.stdout.write(line)
