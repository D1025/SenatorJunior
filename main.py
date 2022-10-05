import os
import hikari
import lightbulb
import time
import dnd
import d10roll
import findathing
import rolemanagement
import random

TOKEN = os.environ['TOKEN']
bot = lightbulb.BotApp(token=TOKEN)

colors_list = [0x0099FF, 0xDC143C, 0xFF1493, 0xFF6347, 0xFFD700, 0xBA55D3, 0x4B0082, 0x7FFF00, 0x2E8B57, 0x800000, 0xD2691E]

#####################################################


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print("Bot has started!")


#####################################################


### /dnd DND CHARACTER MAKER
@bot.command
@lightbulb.option('intelligence',
                  "Do you want turn off intelligence stats?",
                  type=str,
                  required=False,
                  choices=["Turn off", "Autistic"],
                  default="No")
@lightbulb.command('dnd', 'Makes random character for dnd 5e')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    character = dnd.Rub_Postac(ctx.author.id, ctx.options.intelligence)
    p_author = "".join(['Character made by ',str(ctx.author)])
    print(p_author)
    #embed = hikari.Embed(title="Example embed", description="An example hikari embed")
    embed = hikari.Embed(title="DND 5e CHARACTER", description = character, color = random.choice(colors_list))
    #embed.set_thumbnail("Arts/Logos/DnD.png")
    #embed.set_thumbnail("https://i.pinimg.com/originals/48/cb/53/48cb5349f515f6e59edc2a4de294f439.png")
    try:
      embed.set_thumbnail(dnd.ArtClass())
    except:
      embed.set_thumbnail("Arts/Logos/DnD.png")
    embed.set_footer(p_author)
    await ctx.respond(embed)


#####################################################


### FIND PERSONALLITY
@bot.command
@lightbulb.option("personality",
                  "what a personality?",
                  type=str,
                  required=True,
                  choices=[
                      "Abrasiveness", "Absent-Minded", "Aggression", "Brawler",
                      "Cautious", "Detached", "Dishonesty", "Distinctive",
                      "Easygoing", "Farsighted", "Focused", "Hard Of Hearing",
                      "Hardy", "Honest", "Illiterate", "Inattentive", "Polite",
                      "Quick", "Relentless", "Slow", "Specialized",
                      "Suspicious", "Uncivilized"
                  ])
@lightbulb.command('find', 'Find personality description')
@lightbulb.implements(lightbulb.SlashCommand)
async def find(ctx):
    await ctx.respond(findathing.FindPersonality(ctx.options.personality))


#####################################################


### /roll dice:5 + optional EXALTED STANDARD ROLL
@bot.command
@lightbulb.option("desc", "description", type=str, required=False, default="")
@lightbulb.option("auto",
                  "automatic successes",
                  type=int,
                  required=False,
                  default=0)
@lightbulb.option("dice", "How much you want to roll", type=int)
@lightbulb.command('roll', 'Exalted roller')
@lightbulb.implements(lightbulb.SlashCommand)
async def roll(ctx):
    await ctx.respond(
        d10roll.DiseRoll(ctx.options.dice, ctx.options.auto, ctx.options.desc))


#####################################################


### DAMAGE ROLLER FOR EXALTED
@bot.command
@lightbulb.option("damage",
                  "Damage type",
                  type=str,
                  required=False,
                  default="Lethal",
                  choices=["Bashing", "Lethal", "Aggravated"])
@lightbulb.option("dice", "How much you want to roll", type=int)
@lightbulb.command('damage', 'Exalted damage roller')
@lightbulb.implements(lightbulb.SlashCommand)
async def damage(ctx):
    await ctx.respond(d10roll.DamageRoll(ctx.options.dice, ctx.options.damage))


#####################################################


### GIVE ROLE TO SOMEBODY
@bot.command
@lightbulb.option("code", "Secred Passcode to discord role", type=str)
@lightbulb.command('giverole', 'Add your own role')
@lightbulb.implements(lightbulb.SlashCommand)
async def giverole(ctx):
    trole = rolemanagement.GiveRole(ctx.guild_id, ctx.options.code)
    if trole != "False":
      try:
        await bot.rest.add_role_to_member(user=ctx.author,guild=ctx.guild_id, role=trole)
        await ctx.respond("Done, look at your fancy role!")
      except:
        await ctx.respond("Hey, you problably have already that role!")
    else:
        await ctx.respond("Sorry, got a problem.")
    time.sleep(3)
    await ctx.delete_last_response()


#####################################################
### ADDING ROLES

@bot.command
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.ADMINISTRATOR))
@lightbulb.option("id", "Role ID", type=str)
@lightbulb.option("code", "Secred code for getting role", type=str)
@lightbulb.command('adminaddrole', 'Add secred code for role!')
@lightbulb.implements(lightbulb.SlashCommand)
async def systemrole(ctx):
  rolemanagement.AddGiveRole(ctx.guild_id, ctx.options.code, ctx.options.id)
  await ctx.respond("Added")
  
  


#####################################################

time.sleep(3)

try:
    bot.run(
        status=hikari.Status.ONLINE,
        activity=hikari.Activity(
            name="Make a dnd Character!",
            type=hikari.ActivityType.WATCHING,
        ),
    )
except:
    os.system("kill 1")

# DO_NOT_DISTURB IDLE ONLINE

# PROGRAMING
# Make a dnd Character!
