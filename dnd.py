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

 
  
def Rub_Postac(author):
  global rasa
  global klasa
  global subklasa
  global Statystyki
  global opis
  global personality
  if author == 512712313623674910:
    subklasa = 'Samurai'
    rasa = 'Tabaxi'
    klasa = 'Fighter'
  else:
    Losuj_Rasa()
    Losuj_Klasa()
    Losuj_Opis()
  Stats()
  Personality()
  final = "**Rasa:** " + rasa + "\n" + "**Klasa:** " + klasa + '\n' + "**Subklasa:** " + subklasa + '\n' + str(Statystyki) + '\n' + '**Sex:** '+ random.choice(["Mele", "Femele"]) + '\n'+ '**Personality:** ' + twofourpersonality + '\n**Description:** ' + opis
  return final


# print("Gotowe")
# Rub_Postac()

