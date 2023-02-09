
import discord 
import random
import json
import os
import sys 
import asyncio
import time
from discord import *
from discord.ext import commands
from discord import Embed
from asyncio import sleep
from discord.ext.commands import Bot
from turtle import clear



file = open('config.json','r')
config = json.load(file)
intents = discord.Intents.all()
bot = commands.Bot(config['prefix'],intents=intents)


@bot.remove_command( 'help' )
@bot.command() #pass_cotext = True
async def help(ctx, arg = None): # Украшения для команды help
    await ctx.message.delete()
    if arg == None:
        emb = discord.Embed(title= '     Выберите категорию команд: ', color= discord.Colour.dark_gold())
        emb.add_field(name = ('v.help basic'), value='Основные команды ', inline= False)
        emb.add_field(name=('v.help mod'), value= 'Показывает все модераторские команды', inline= False )
        emb.add_field(name=('v.help more'), value= 'Показывает разные команды.', inline= False)
        emb.set_thumbnail(url = "https://i.ytimg.com/vi/FpBikhF6SqI/maxresdefault.jpg")
    elif arg == 'basic':
        emb = discord.Embed(title= '   Основные команды    ', color= discord.Colour.dark_gold())
        emb.add_field( name = ('v.info') , value= 'Информация о Vilonka bot', inline= False)
    elif arg == 'mod':
        emb = discord.Embed(title= '     Команды для модераторов: ', color= discord.Colour.dark_gold())
        emb.add_field( name = ('v.ban') , value= 'Банит пользователя на сервере', inline= False)
        emb.add_field( name = ('v.unban') , value= 'Банит пользователя на сервере', inline= False)
        emb.add_field( name = ('v.kick'), value= 'Кикает человека с сервера', inline= False)
        emb.add_field( name = ('v.clear'), value= 'Удаление сообщений', inline= False)
    elif arg == 'more':
        emb = discord.Embed(title= '     Разные команды ', color= discord.Colour.dark_gold())
        emb.add_field( name = ('v.орел_решка'), value= 'Подбрасывает монетку', inline= False )
        emb.add_field( name = ('v.say' ), value= 'Бот отправляет сообщение что написал пользователь' , inline= False)
    else:
        member = ctx.author # Пишет в лс пользователю что он получил достижение 
        embed = discord.Embed(title="Вы допустили ошибку.", colour=0xFFFFFF, description="Провельте правильно ли написана команда хелп") #Поля не должны быть пустыми.
        await ctx.channel.send(embed=embed)
        await member.send("Ты получил достижение ｓｅｃｒｅｔ    ｉｎ    ｈｅｌｐ ;Ｄ , что бы получить достижение напиши мне в лс и скинь док-ва.")
        # # await ctx.send('секретка, кто нашел тому роль ')
        # await ctx.send('секретка, кто нашел тому роль ', ephemeral = True)
    await ctx.send( embed = emb )


@bot.command(name= 'say') # бот отправляет тоже самое сообщение что написал пользователь и удаляет сообщение пользователя
@commands.has_permissions(administrator=True)
async def say(ctx, *, arg):
    await ctx.message.delete() #Удаляем сообщение автора команды
    await ctx.send(arg) 


@bot.event # показывает что бот онлайн + в его статусе на скольких он серверах 
async def on_ready():
    print('Bot online')
    print(f'name bot = {bot.user.name}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f" я нахожусь на {len(bot.guilds)} серверах."))


@bot.command(name='info') #описание бота 
async def info(ctx):
    emb = discord.Embed(title= '                       Информация обо мне                                        ', color= discord.Colour.dark_gold())
    emb.add_field(name=('                        Привет! Меня зовут Вилонка.                                     '), inline= False,
                  value='И у меня пока что не так много команд, но в будующем их станет намного больше! Так-же у моего создателя есть свой дискорд сервер.\
                     Он выкладывает на нем мои новые команды, а так же может сделать вам приватную команду :D. Мы тебя ждем на нашем сервере!\
                        Discord:https://discord.gg/EzvpNEqCeG  ')
    # emb.add_field(value='   И у меня пока что не так много команд, но в будующем их станет намного больше!       ', inline= False)
    # emb.add_field(value='                 Так-же у моего создателя есть свой дискорд сервер.                     ', inline= False)
    # emb.add_field(value='Он выкладывает на нем мои новые команды, а так же может сделать вам приватную команду :D', inline= False)
    # emb.add_field(value='                           Присоединяйся мы тебя ждем!                                  ', inline= False)
    # emb.add_field(value='                      Discord:https://discord.gg/EzvpNEqCeG                             ', inline= False)
    await ctx.send(embed = emb)


#               ТЕГ В ДИСКОРДЕ СПЕЦИЛЬАОГО ЧЕЛОВЕК <@А СЮДА ЕГО ID>


@bot.command(name='орел_решка') #орел или решка
async def орел_решка(ctx):
    choice = random.randint(0, 100) # случайное число от 0 до 100
    if choice <= 49:
        await ctx.send(f'{ ctx.author.mention } Выпал Орел!')
    elif 50<=choice<99:
        await ctx.send(f'{ ctx.author.mention } Выпала решка!')
    elif 99<=choice:
       await ctx.send(f'{ ctx.author.mention } Ну надоели со своим орлом и решкой 💀')


@bot.command(name='kick') # кикает с сервера (надо доделать)
@commands.has_permissions( administrator=True )
async def kick(ctx, member: discord.Member, *, reason=None):
                await member.kick()
                await ctx.send(f'Пользователь { member.mention } был кикнут с сервера. Причина:  { reason }. Давайте все ему скажем покаааааааааа.')



# @bot.command(name='ban') # кикает с сервера (надо доделать)
# @commands.has_permissions(administrator=True)
# async def ban( ctx, member: discord.Member, *, reason=None ):
#     if administrator == True:
#         await member.ban()
#         await ctx.send(f'Пользователь { member.mention } был забанен на сервере. Причина:  {reason}. Давайте все ему скажем покаааааааааа.')
#     else:
#         await ctx.send(f'{ctx.author.mention } Вы феменистка и у вас нет прав прав а а ')



@bot.command(name='clear') # удаляет сообщения в чате 
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=20): #число 20 - это число удалённых сообщений, если число не указано
    await ctx.channel.purge(limit=amount)

# async def clear_error(ctx, error):
#     if isinstance(error, commands.MissingPermissions):
#         await ctx.send( f'{ctx.author.mention } Вы феменистка и у вас нет прав прав а а ')




bot.run(config['token'])