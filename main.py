import discord
from pyowm import OWM
import random as rd
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils import weather
from discord.ext import commands
owm = OWM('501fc5a4f679c097c996da39b2cef9d1')
mgr = owm.weather_manager()
obziv = ['ЕБЛАН','СУКА',"УЕБАН", "ТВАРЬ","УЕБА","МУДАК","ПИЗДОГЛАЗ","ЕБЛОЗВОН","ГОНДОПЛЯС","ХУЙЛО","ГАНДОН","ХУЕБЕС","УЕБИЩЕ"]
obziv1 = ["ТУПОЙ","КОНЧЕННЫЙ","ОТСТАЛЫЙ","ЕБУЧИЙ","ДЕФЕКТИВНЫЙ","СОЦИАЛЬНО-НЕАДАПТИРОВАННЫЙ","СЛАДЕНЬКИЙ","СУЧИЙ"]
client = commands.Bot(command_prefix = '..')
@client.event
async def on_ready():
	game = discord.Game("Я живой!")
	await client.change_presence(status=discord.Status.idle, activity=game)
	print('Bot start')
@client.command(pass_context = True)
async def weather(ctx, arg):
	print('Command "weather"')
	try:
		observation = mgr.weather_at_place(arg)
		w = observation.weather
		temperature = w.temperature('celsius')['temp']
		humidity = w.humidity
		rain = w.rain
		clouds = w.clouds
		status = w.status
		if status == "Clouds":
			status = '☁Облачно\n'    # CLOUD
		elif status == "Rain":
			status = '🌧Дождь\n'    # RAIN
		elif status == "Snow":
			status = '❄️Снегопад\n'   # SNOW
		elif status == "Thunderstorm":
			status = '⚡Гроза\n'   # THUNDER
		else:
			status = ''# NORMAL
		await ctx.send('Прогноз погоды в "'+arg+'"\n'+status+'🌡Температура: '+str(temperature)+'\n💧Влажность: '+str(humidity)+'\n☁️Облачность:'+str(clouds))
	except:
		await ctx.send('Чел, я не ебу че это за город, поэтому давай по нормальному пиши')
@client.command(pass_context = True)
async def nah(ctx, arg):
	temp = rd.randint(0,len(obziv)-1)
	temp1 = rd.randint(0,len(obziv1)-1)
	await ctx.send('ПОШЕЛ НАХУЙ '+arg+" "+obziv[temp]+" "+obziv1[temp1])
@client.command(pass_context = True)
async def nahcmds(ctx):
	await ctx.send("Существительные: "+str(obziv)+"\nПрилагательные: "+str(obziv1))
@client.command()
async def helps(ctx):
	helpsf = open('help.txt','r',encoding = "utf-8")
	helps = helpsf.read()
	helpsf.close()
	await ctx.send(helps)
@client.command()
async def test(ctx):
	try:
		jopa = discord.MessageReference('34')
		await ctx.send(jopa)
	except Exception as e:
		await ctx.send(e)
		return

token = input("Enter a token: ")
client.run(token)
