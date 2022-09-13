import random, json, requests
import description

rasa = 'Human'
klasa = 'Standart'
subklasa = 'none'
Statystyki = {'Strength': 0, 'Dexterity': 0, 'Constitution': 0, 'Intelligence': 0, 'Wisdom': 0, 'Charisma': 0}
atrybuty = list(Statystyki.keys())
opis = "none"



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


    
  
  

def Losuj_Rasa(author):
  global Statystyki, atrybuty
  rr = open("json/newrases.json")
  race_result = json.load(rr)
  race_list = []
  for row in race_result['results']:
    name = row['name']
    race_list.append(name)

  #race_list.append(new_races) #Dla nowych ras, ale raczej będzie rozwijanie jsona, bo wszystko na nim działa.
  global rasa
  if str(author)=='512712313623674910':
    rasa = 'Tabaxi'
  else:
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
      



def Losuj_Klasa(author):
  cr = open("json/clases.json")
  class_ressult = json.load(cr)
  class_list = []
  for row in class_ressult['results']:
    name = row['name']
    class_list.append(name)
    
  global klasa
  if str(author)=='512712313623674910':
    klasa = 'Fighter'
  else:
    klasa = random.choice(class_list)
  subclass_list = []
  for row in class_ressult['results']:
    if row['name']==klasa:
      for nextrow in row['archetype']:
        name =nextrow['name']
        subclass_list.append(name)
    
  global subklasa
  if str(author)=='512712313623674910':
    subklasa = 'Samurai'
  else:
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
  

 
  
def Rub_Postac(author):
  Stats()
  Losuj_Rasa(author)
  Losuj_Klasa(author)
  Losuj_Opis()
  final = "Rasa: " + rasa + "\n" + "Klasa: " + klasa + '\n' + "Subklasa: " + subklasa + '\n' + str(Statystyki) + '\n' + opis
  return final


# print("Gotowe")
# Rub_Postac()

