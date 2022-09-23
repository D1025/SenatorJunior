def GiveRole(guild, code):
  try:
    f = open("".join(["management/role/",str(guild), ".txt"]), "r")
  except:
    return "False"
  for line in f:
    l = line.strip()
    li = list(l.split(" "))
    if str(li[0]) == str(code):
      f.close()
      return li[1]
  f.close()
  return "False"



def AddGiveRole(guild, code, idrole):
  f = open("".join(["management/role/",str(guild), ".txt"]), "a")
  f.write(" ".join([code, idrole]))
  f.write("\n")
  f.close()

