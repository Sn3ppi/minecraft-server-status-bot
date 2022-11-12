import json
import datetime

import time
from mcstatus import JavaServer

import displays
import settings


server_messages = displays.ServerMessages()
error_messages = displays.Errors()


server_data = {}
server_data["online"] = False


def get_server_data(): #постоянное получение информации о сервере
    global server_data
    while True:
        server_data["last_update"] = datetime.datetime.now().strftime("%a %d %b %Y %H:%M:%S")
        try:
            server = JavaServer.lookup(settings.IPADDR)
            ping_res = server.ping()
            server_data["ping"] = ping_res
            status_res = server.status(tries=1)
            server_data["version"] = status_res.version.name
            server_data["protocol"] = status_res.version.protocol
            server_data["motd"] = status_res.description
            server_data["player_count"] = status_res.players.online
            server_data["player_max"] = status_res.players.max
            server_data["players"] = []
            if status_res.players.sample is not None:
                server_data["players"] = [player.name for player in status_res.players.sample]
            server_data["online"] = True
        except Exception as e:
            print(error_messages.server(e))
        json.dumps(server_data, indent=4)
        time.sleep(1)


def get_players_list(): #парсинг информации об игроках
    return server_messages.players(server_data) if server_data["player_count"] > 0 else server_messages.no_players()


def parse_data(): #парсинг ВСЕЙ информации 
    return server_messages.server_on(server_data, get_players_list()) if server_data["online"] else server_messages.server_off(server_data)