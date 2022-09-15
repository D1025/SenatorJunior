import random, json, requests
import description

rasa = 'Human'
klasa = 'Standart'
subklasa = 'none'
Statystyki = {'Strength': 0, 'Dexterity': 0, 'Constitution': 0, 'Intelligence': 0, 'Wisdom': 0, 'Charisma': 0}
atrybuty = list(Statystyki.keys())
opis = "none"
twofourpersonality = ""

def Personality():
  personality = []
  pr = open("json/personality.json")
  personality_result = json.load(pr)
  for row in personality_result['results']:
    name = row['name']
    personality.append(name)
  global twofourpersonality
  twofourpersonality = str(random.choice(personality))
  personality.remove(twofourpersonality)
  i = random.randint(1,2)
  for j in range(0,i):
    k = random.choice(personality)
    twofourpersonality += ", " + k
    personality.remove(k)



def Stats():
  global Statystyki
  global atrybuty
  # wartosci = list(Statystyki.values())
  # print(wartosci)

  for i in range(6):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    roll3 = random.randint(1,6)
    roll4 = random.randint(1,6)
    nums = [roll1,roll2,roll3,roll4]
    lowest = min(nums)
    score = roll1 + roll2 + roll3 + roll4 - lowest
    Statystyki[atrybuty[i]]=score
    # print(Statystyki[atrybuty[i]])

def IntStats():
  global klasa
  primary = "Dexterity"
  class_result = json.load(open("json/clases.json"))
  for row in class_result['results']:
    if row['name']==klasa:
      primary = row['primary']
  
  score_list = []
  for i in range(6):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    roll3 = random.randint(1,6)
    roll4 = random.randint(1,6)
    nums = [roll1,roll2,roll3,roll4]
    lowest = min(nums)
    score_list.append(roll1 + roll2 + roll3 + roll4 - lowest)

  Statystyki[primary]=max(score_list)
  score_list.remove(max(score_list))
  if primary != "Dexterity":
    Statystyki["Dexterity"]=max(score_list)
    score_list.remove(max(score_list))
    atrib = ["Strength", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    atrib.remove(primary)
    for i in range(4):
      k = random.choice(atrib)
      Statystyki[k]=score_list[0]
      score_list.pop(0)
      atrib.remove(k)
  else:
    atrib = ["Strength", "Constitution", "Intelligence", "Wisdom", "Charisma"]
    for i in range(5):
      k = random.choice(atrib)
      Statystyki[k]=score_list[0]
      score_list.pop(0)
      atrib.remove(k)
      
  
    
  
  

def Losuj_Rasa():
  global Statystyki, atrybuty
  rr = open("json/newrases.json")
  race_result = json.load(rr)
  race_list = []
  for row in race_result['results']:
    name = row['name']
    race_list.append(name)

  #race_list.append(new_races) #Dla nowych ras, ale raczej będzie rozwijanie jsona, bo wszystko na nim działa.
  global rasa
  rasa = random.choice(race_list)
  # rasa = 'Half-Elf'
  # print(Statystyki)
  for row in race_result['results']:
    if str(row['name'])==rasa:
      hated_i=[]
      # print(row['asi'])
      for att in row['asi']:
        for i in range(0,6):
          # print(atrybuty[i])
          # print(att['attributes'][0])
          if atrybuty[i]==att['attributes'][0]:
            Statystyki[atrybuty[i]]+=att['value']
            hated_i.append(i)
      for att in row['asi']:
        if att['attributes'][0]=='Other':
          att_dodaj = random.randint(0,5)
          try:
            hated_i.index(att_dodaj)
          except:
            Statystyki[atrybuty[att_dodaj]]+=att['value']
            hated_i.append(att_dodaj)
          att_dodaj = random.randint(0,5)

  # print(Statystyki)
      



def Losuj_Klasa():
  cr = open("json/clases.json")
  class_ressult = json.load(cr)
  class_list = []
  for row in class_ressult['results']:
    name = row['name']
    class_list.append(name)
    
  global klasa
  klasa = random.choice(class_list)
  subclass_list = []
  for row in class_ressult['results']:
    if row['name']==klasa:
      for nextrow in row['archetype']:
        name =nextrow['name']
        subclass_list.append(name)
    
  global subklasa
  subklasa = random.choice(subclass_list)
  
  

def Losuj_Opis():
  global opis
  opis = random.choice(description.hair_color)
  opis += " "
  opis += random.choice(description.hair_style)
  opis += ". "
  opis += random.choice(description.eye_type)
  opis += " "
  opis += random.choice(description.eye_color)
  opis += " eyes. "
  if random.randint(1,3) == 1:
    opis += random.choice(description.mark)
    opis += " "
    opis += random.choice(description.mark_where)
    opis += ". "
  if random.randint(1,3) == 1:
    opis += random.choice(description.tattoo)
    opis += " "
    opis += random.choice(description.tattoo_where)
    opis += " "

 
  
def Rub_Postac(author, Int):
  global rasa
  global klasa
  global subklasa
  global Statystyki
  global opis
  global personality
  Losuj_Klasa()
  if Int !="No":
    Stats()
  else:
    IntStats()
  Losuj_Rasa()
  Losuj_Opis()
  Personality()
  if author == 512712313623674910:
    subklasa = 'Samurai'
    rasa = 'Tabaxi'
    klasa = 'Fighter'

  final = "**Rasa:** " + rasa + "\n" + "**Klasa:** " + klasa + '\n' + "**Subklasa:** " + subklasa + '\n' + str(Statystyki) + '\n' + '**Sex:** '+ random.choice(["Mele", "Femele"]) + '\n'+ '**Personality:** ' + twofourpersonality + '\n**Description:** ' + opis
  return final


# print("Gotowe")
# Rub_Postac()

