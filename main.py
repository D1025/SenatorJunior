import os
import hikari
import lightbulb
import time
import dnd
import d10roll
import findathing

TOKEN = os.environ['TOKEN']
bot = lightbulb.BotApp(token=TOKEN)


@bot.listen(hikari.StartedEvent)
async def on_started(event):
  print("Bot has started!")

### /dnd DND CHARACTER MAKER
@bot.command
@lightbulb.command('dnd', 'Makes random character for dnd 5e')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
  character = dnd.Rub_Postac(ctx.author.id)
  print('Character made by '+ str(ctx.author))
  await ctx.respond(character)

@bot.command
@lightbulb.option("personality","what a personality?", type=str, required=True, choices=["Abrasiveness", "Absent-Minded", "Aggression", "Brawler", "Cautious", "Detached", "Dishonesty", "Distinctive", "Easygoing", "Farsighted", "Focused", "Hard Of Hearing", "Hardy", "Honest", "Illiterate", "Inattentive", "Polite", "Quick", "Relentless", "Slow", "Specialized", "Suspicious", "Uncivilized"])
@lightbulb.command('find', 'Find personality description')
@lightbulb.implements(lightbulb.SlashCommand)
async def find(ctx):
  await ctx.respond(findathing.FindPersonality(ctx.options.personality))
  
### /roll dice:5 + optional EXALTED STANDARD ROLL
@bot.command
@lightbulb.option("desc","description", type=str, required=False, default="")
@lightbulb.option("auto","automatic successes", type=int, required=False, default=0)
@lightbulb.option("dice","How much you want to roll", type=int)
@lightbulb.command('roll', 'Exalted roller')
@lightbulb.implements(lightbulb.SlashCommand)
async def roll(ctx):
  await ctx.respond(d10roll.DiseRoll(ctx.options.dice, ctx.options.auto, ctx.options.desc)) 

### DAMAGE ROLLER FOR EXALTED
@bot.command
@lightbulb.option("damage","Damage type", type=str, required=False, default="Lethal", choices=["Bashing", "Lethal", "Aggravated"])
@lightbulb.option("dice","How much you want to roll", type=int)
@lightbulb.command('damage', 'Exalted damage roller')
@lightbulb.implements(lightbulb.SlashCommand)
async def damage(ctx):
  await ctx.respond(d10roll.DamageRoll(ctx.options.dice, ctx.options.damage)) 


time.sleep(3)

try:
  bot.run(status=hikari.Status.ONLINE,activity=hikari.Activity(name="Make a dnd Character!",type=hikari.ActivityType.WATCHING,),)
except:
  os.system("kill 1")

# DO_NOT_DISTURB IDLE ONLINE
