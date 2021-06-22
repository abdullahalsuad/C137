import discord
import os
import requests
import json
import random
import pandas as pd
from keep_alive import keep_alive

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def jokes():
    data = requests.get(f)
    tt = json.loads(data.text)
    return tt

f = r"https://official-joke-api.appspot.com/random_joke"



#all words arry

slang_words = ["fuck", "motherfucker", "bitch", "son of a bitch","Bastard","Idiot"]

welcome_words = ["Hello","HELLO","hello","Hi","HI","hi","HEY","Hey","hey"]

sadStatus = ["c/SadStatus"]

#welcome words area 
welcomearr = []
welcomdf = pd.read_csv("welcomeword.csv")
for i in range(4):
	welcomearr.append(welcomdf['WELCOME'][i])

#slang words area
slangarr = []
slangdf = pd.read_csv("slangword.csv")
for i in range(3):
  slangarr.append(slangdf['SLANG'][i])

#sad Status area
sadStatusarr = []
sadStatusdf = pd.read_csv("sadstatus.csv")
for i in range(30):
  sadStatusarr.append(sadStatusdf['SADSTATUS'][i])


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game("c/help"))
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return 
   
  msg = message.content 

#inspire area 
  if message.content.startswith('c/inspire'):
    quote = get_quote()
    await message.channel.send(quote)
#jokes area
  if message.content.startswith('c/jokes'):
    j = jokes()
    s = j['setup'] 
    p = j['punchline'] 
    await message.channel.send(f'Setup: {s}')
    await message.channel.send(f'Punchline: {p}')

#help area
  if message.content.startswith('c/help'):
    helpmsg = open("help.txt", "r")
    helpdata = helpmsg.read()
    await message.channel.send(helpdata)  

#info area
  if message.content.startswith('c/info'):
    infomsg = open("info.txt", "r")
    info = infomsg.read()
    await message.channel.send(info)     
  
#welcome words area
  if any(word in msg for word in welcome_words):
     await message.channel.send(random.choice(welcomearr))

#slang_words words area
  if any(word in msg for word in slang_words):
    await message.channel.send(random.choice(slangarr))

#sad_status  area
  if any(word in msg for word in sadStatus):
    await message.channel.send(random.choice(sadStatusarr))

keep_alive()
client.run(os.getenv('TOKEN'))