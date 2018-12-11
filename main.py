# python3.6
# coding: utf-8

'''Простой бот на discord.py 1.0.0a с использованием discord.ext.commands и cogs.

Автор: AkiraSumato-01 / Рам#6692
'''

## -> Импортируем необходимые библиотеки.
import discord
from discord.ext import commands

# -> Токен бота:
# Чтобы его получить, создайте приложение на
# https://discordapp.com/developers/applications/me
# и во вкладке "Bot" создайте бота и нажмите кнопку "Copy"
# чтобы скопировать этот самый токен.
TOKEN = 'your_bot_token_here'

## -> Префикс для команд:
## Используется для доступа к командам бота.
## Например, чтобы выполнить команду "test",
## вводим "ex?test", т.к. префикс: "ex?".
DEFAULT_PREFIX = 'ex?'

## -> Подключаемые расширения (модули):
## Каждый модуль хранит в себе набор функций (зачастую, команд).
modules = ['modules.example']

## Здесь просто указывается, что префиксом будет упоминание
## или значение переменной "PREFIX"
prefix = commands.when_mentioned_or(DEFAULT_PREFIX)


## -> Главный класс.
class YourBotName(commands.Bot):
    '''Главный класс бота.'''
    def __init__(self, token, prefix, modules):
        '''Инициализация'''
        commands.Bot.__init__(self, command_prefix=prefix)
        self.modules = modules
        self.load()
        self.run(token, bot=True, reconnect=True)
    
    def load(self):
        '''Загружаем подключаемые расширения (модули)'''
        ## -> Удаление дефолтной команды "help":
        ## дефолтная команда автоматически добавляется,
        ## но если вы делаете свой справочник,
        # расскомментируйте строку ниже
        # self.remove_command('help')

        ## -> Загружаем расширения:
        ## функция 'commands.Bot().load_extension(extension)'
        ## загружает расширение. Если не удалось, выдает исключение.
        for module in self.modules:
            try:
                self.load_extension(module)
            except Exception as e:
                print(f'<!> Не удалось загрузить модуль {module}.\n{type(e).__name__}: {e}', file=sys.stderr)
            else:
                print(f'<!> Модуль {module} успешно загружен.')

    async def on_connect(self):
        ## При подключении к Discord, бот поменяет статус на "I'm loading :з"
        await self.change_presence(activity=discord.Game(name='I\'m loading :з'), status=discord.Status.idle)
    
    async def on_ready(self):
        print(f'<?> Подключение к {self.user} успешно.')
        ## По окончанию загрузки, бот поменяет статус на "Discord API"
        await self.change_presence(activity=discord.Game(name='Discord API'))


if __name__ == '__main__':
    ## -> Запускаем бота.
    YourBotName(TOKEN, prefix, modules)