# python3.6
# coding: utf-8

## -> Опять же, импорт нужных библиотек.
import discord
from discord.ext import commands

## -> А вот сам класс.
class ExampleCommands(object):
    '''Стандартные команды.
    `help ExampleCommands` для списка команд этого модуля;
    `help команда` для справки по указаанной команде.'''

    def __init__(self, bot):
        '''Инициализация модуля.'''
        self.bot = bot
    
    ## -> Команда "test":
    ## Отправляет сообщение, написанное после
    ## команды в чат от имени бота.
    @commands.command(name='test')
    async def test_command(self, ctx, *, message):
        '''Тестовая команда.
        Синтаксис:
        `test Hello World`,
        бот напишет в чат "Hello World"
        '''

        await ctx.send(message)


    ## -> Команда "test_owner":
    ## Так же у нее есть алиасы "test-owner" и "for-bot-owner".
    @commands.command(name='test_owner', aliases=['test-owner', 'for-bot-owner'])
    @commands.is_owner() # <-- Проверка на владельца бота.
    async def test_owner_command(self, ctx):
        '''Если команду ввел владелец бота, бот отправит в чат "Вы - мой господин!".
        Аргументы не требуются.
        '''

        await ctx.send('Вы - мой господин!')
    

    ## -> Команда "test_nsfw":
    ## Будет выполнена только если канал помечен, как "NSFW".
    @commands.command(name='test_nsfw')
    @commands.is_nsfw() # <-- Проверка на NSFW-канал.
    async def test_nsfw_command(self, ctx):
        '''Если команда отправлена в NSFW-канал, бот добавит реакцию ✅ к сообщению.
        '''

        await ctx.message.add_reaction('✅')
    

    ## -> Команда "myname":
    ## Бот отправит в чат ваш ник, ID, упоминание и полный ник (с тегом)
    @commands.command(name='myname')
    async def myname_command(self, ctx):

        await ctx.send(f'Ваш ник: {ctx.author.name}\n'
                       f'Ваш ID: {ctx.author.id}\n'
                       f'Упоминание: {ctx.author.mention}\n'
                       f'Полный ник: {ctx.author}\n')
    

    ## -> Команда "restart":
    ## Всего лишь полный перезапуск бота.
    @commands.command(name='restart')
    @commands.is_owner()
    async def restart_cmd(self, ctx):
        '''Перезагрузка бота.'''
        import os, sys

        await ctx.send('Перезагружаюсь...')
        os.execl(sys.executable, sys.executable, * sys.argv)


## -> Функция загрузки.
## В каждом подключаемом расширении должна быть функция "setup",
## которая вызывается, когда бот загружает данное расширение.
def setup(bot):
    bot.add_cog(ExampleCommands(bot))