# imports
import os
import discord
from discord.ext.commands import Bot
from keepAlive import keep_alive
import functions as f
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO

#on startup
keep_alive()
my_secret = os.environ['token']
client = Bot(command_prefix="!")

# ready
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

#only use client.command
@client.command()
async def ping(ctx):
    await ctx.reply("pong!")

#join class
@client.command()
async def joinclass(ctx, classcode, classnum, classsec):
    guild = ctx.guild
    #makes role
    name = classcode.upper() + " " + classnum + " " + classsec
    if discord.utils.get(guild.channels, name= name) == False:
      await guild.create_role(name= name)

@client.command()
async def avatar(ctx, a):
  print(a)
  disallowed_characters = "<!@>"
  for character in disallowed_characters:
	  a = a.replace(character, "")
  user = await ctx.guild.query_members(user_ids=[int(a)])
  user = user[0]
  await ctx.send(user.avatar_url)

@client.command()
async def addclass(ctx, a, b, c): #ADD IF STATEMENT TO CHECK IF CLASS IS LEGIT
  f.add_classes_to_profile(user_id=ctx.author.id, user_name=ctx.author.name, classname=a, classnum=b, classsec=c, master_user_list='userInfo.txt')
  try:
    await ctx.send(a.upper(), " was added successfully!")
  except:
    await ctx.send("Oops! That failed!")

@client.command()
async def removeclass(ctx, a, b, c):
  try:
    f.remove_classes_from_profile(user_id=ctx.author.id, user_name=ctx.author.name, classname=a.upper(), classnum=b, classsec=c, master_user_list='userInfo.txt')
    await ctx.send(a.upper(), " was removed successfully!")
  except:
    await ctx.send("Oops! That failed!")

@client.command()
async def checkclass(ctx, a):
  if f.check_if_legit_name(name=a.upper()):
    await ctx.send("That class is legit!")
  else:
    await ctx.send("Uh oh! Check your class name of errors because that class doesnt exist!")

@client.command()
async def profile(ctx, a=None):

  if a == None:
    user = ctx.author
  else:
    disallowed_characters = "<!@>"
    for character in disallowed_characters:
	    a = a.replace(character, "")
    user = await ctx.guild.query_members(user_ids=[int(a)])
    user = user[0]

  print(ctx.author)
  img = Image.open("honeycomb.jpg")
  draw = ImageDraw.Draw(img)
  fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 75)
  fnt2 = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 100)

  asset = user.avatar_url_as(size = 128)
  data = BytesIO(await asset.read())
  
  #pfp
  pfp = Image.open(data)
  pfp = pfp.resize((750,750))
  img.paste(pfp, (50,50))
  

  #card formatting
  name = user #text is username
  classN = "Classes:"


  leftclassadj = 850
  rightclassadj = 1425
  topclassadj = 225
  vertclassmult = 160
  description = "Description: "
  draw.text((leftclassadj, 50), name, (0,0,0), font=fnt2)
  draw.text((leftclassadj, 125), "______________________", (0,0,0), font=fnt)

  #for i in 
  draw.text((leftclassadj, topclassadj), classN, (0,0,0), font=fnt)
  
  #draw.text((leftclassadj, topclassadj+vertclassmult*2), class5, (0,0,0), font=fnt)
  #draw.text((rightclassadj, topclassadj+vertclassmult*2), class6, (0,0,0), font=fnt)
  draw.text((50, 850), description, (0, 0, 0), font=fnt2)
  img.save('sample-out.jpg')
  await ctx.send(file=discord.File('sample-out.jpg'))


client.run(my_secret)