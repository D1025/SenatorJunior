import random



def DiseRoll(dicenummber, auto, description):
  number = -1
  Rolled = ""
  sukcesses = auto
  for roll in range(0,dicenummber):
    number = random.randint(1,10)
    if number ==10:
      Rolled += "__**"+str(number)+"**__"
      sukcesses+=2
    elif number >=7:
      Rolled += "**"+str(number)+"**"
      sukcesses+=1
    else:
      Rolled += str(number)
    if roll!=dicenummber-1:
      Rolled +=", "
  if auto>0:
    if description=="":
      finalroll = "You rolled ["+ str(dicenummber)+"]: " + Rolled + "for a total of **" + str(sukcesses) + "** successes with " +str(auto) + " autosuccesses"
    else:
      finalroll = "You rolled [" + str(dicenummber)+"]: " + Rolled + " for a total of **" + str(sukcesses) + "** successes with " +str(auto) + " autosuccesses for " + description
  else:
    if description=="":
      finalroll = "You rolled [" + str(dicenummber)+"]: " + Rolled + " for a total of **" + str(sukcesses) + "** successes"
    else:
      finalroll = "You rolled [" + str(dicenummber)+"]: " + Rolled + " for a total of **" + str(sukcesses) + "** successes for " + description
  tab_finalroll = [finalroll, "".join([str(sukcesses), " SUCCESSES"])]
  #return finalroll
  return tab_finalroll


def DamageRoll(dicenummber, damagetype):
  number = -1
  Rolled = ""
  sukcesses = 0
  for roll in range(0,dicenummber):
    number = random.randint(1,10)
    if number >=7:
      Rolled += "**"+str(number)+"**"
      sukcesses+=1
    else:
      Rolled += str(number)
    if roll!=dicenummber-1:
      Rolled +=", "
  finalroll = "You rolled [" + str(dicenummber)+"]: " + Rolled + " for a total of **" + str(sukcesses) + "** levels of " + damagetype + " damage"
  return finalroll