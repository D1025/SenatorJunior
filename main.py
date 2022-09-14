import os
import hikari
import lightbulb
import time
import dnd

TOKEN = os.environ['TOKEN']
bot = lightbulb.BotApp(token=TOKEN)


@bot.listen(hikari.StartedEvent)
async def on_started(event):
  print("Bot has started!")


@bot.command
@lightbulb.command('dnd', 'Makes random character for dnd 5e')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
  character = dnd.Rub_Postac(ctx.author.id)
  print('Character made by '+ str(ctx.author))
  await ctx.respond(character)
  


time.sleep(3)

try:
  bot.run(status=hikari.Status.ONLINE,activity=hikari.Activity(name="Make a dnd Character!",type=hikari.ActivityType.WATCHING,),)
except:
  os.system("kill 1")

# DO_NOT_DISTURB IDLE ONLINE
