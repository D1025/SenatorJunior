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
  await ctx.respond(character)
  print('Done')


time.sleep(3)


bot.run(status=hikari.Status.ONLINE,activity=hikari.Activity(name="Make a dnd Character!",type=hikari.ActivityType.WATCHING,),)

# DO_NOT_DISTURB IDLE ONLINE
