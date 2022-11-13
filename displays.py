import settings


class ServerMessages:

    def help(self) -> str:
        return """
ℹ️ Бот для отслеживания онлайна на сервере @dreammita.
ℹ️ Мои команды:
/start, /help - открыть это меню
/status - проверить онлайн
ℹ️ Код: https://github.com/Sn3ppi/dreammita-status-bot"""

    def server_off(self, server_data: str) -> str:
        return f"""
🕑 <b>Последнее обновление</b>: {server_data["last_update"]}
ℹ️ <b>Состояние</b>: выключен ❌
🖥 <b>IP</b>: {settings.IPADDR}"""

    def server_on(self, server_data: str, players: str) -> str:
        return f"""
🕑 <b>Последнее обновление</b>: {server_data["last_update"]}
ℹ️ <b>Состояние</b>: включен ✅
🖥 <b>IP</b>: {settings.IPADDR}
📡 <b>PING</b>: {round(server_data["ping"], 1)} ms
📝 <b>Описание</b>: {server_data["motd"]}  
🕹 <b>Версия</b>: {server_data["version"]}
👥 <b>Текущий онлайн</b>: {server_data["player_count"]}/{server_data["player_max"]}
👥<b>Игроки</b>:
{players}"""

    def no_players(self) -> str:
        return "На сервере сейчас никого нет."

    def players(self, server_data: str) -> str:
        return "\n".join(player for player in server_data["players"])


class Errors:

    def many_clicks(self, count: int) -> str:
        return f"Подозрительная активность! Попробуйте через {count} с."

    def server(self, error: str) -> str:
        return f"Возникла ошибка при получении данных: {error}"
