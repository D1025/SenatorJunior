import random, json, requests
import description
from dndpaiting import Paint

rasa = 'Human'
klasa = 'Standart'
subklasa = 'none'
Statystyki = {
    'Strength': 0,
    'Dexterity': 0,
    'Constitution': 0,
    'Intelligence': 0,
    'Wisdom': 0,
    'Charisma': 0
}
atrybuty = list(Statystyki.keys())
opis = "none"
twofourpersonality = ""
rasa_art = ""
klasy_art = {'Artificer':"https://www.dndbeyond.com/avatars/13916/408/637411847943829485.jpeg",'Barbarian':"https://www.dndbeyond.com/avatars/10/0/636336416778392507.jpeg", 'Bard': "https://www.dndbeyond.com/avatars/10/1/636336416923635770.jpeg", 'Cleric':"https://www.dndbeyond.com/avatars/10/2/636336417054144618.jpeg", 'Druid':"https://www.dndbeyond.com/avatars/10/3/636336417152216156.jpeg", 'Fighter': "https://www.dndbeyond.com/avatars/10/4/636336417268495752.jpeg", 'Monk':"https://www.dndbeyond.com/avatars/10/5/636336417372349522.jpeg", 'Paladin': "https://www.dndbeyond.com/avatars/10/6/636336417477714942.jpeg", 'Ranger':"https://www.dndbeyond.com/avatars/10/7/636336417569697438.jpeg", 'Rogue':"https://www.dndbeyond.com/avatars/10/8/636336417681318097.jpeg", 'Sorcerer':"https://www.dndbeyond.com/avatars/10/9/636336417773983369.jpeg", 'Warlock': "https://www.dndbeyond.com/avatars/10/12/636336422983071263.jpeg", 'Wizard':"https://www.dndbeyond.com/avatars/10/11/636336418370446635.jpeg"}



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
    i = random.randint(1, 2)
    for j in range(0, i):
        k = random.choice(personality)
        twofourpersonality += ", " + k
        personality.remove(k)


def Stats():
    global Statystyki
    global atrybuty
    # wartosci = list(Statystyki.values())
    # print(wartosci)

    for i in range(6):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll3 = random.randint(1, 6)
        roll4 = random.randint(1, 6)
        nums = [roll1, roll2, roll3, roll4]
        lowest = min(nums)
        score = roll1 + roll2 + roll3 + roll4 - lowest
        Statystyki[atrybuty[i]] = score
        # print(Statystyki[atrybuty[i]])


def AutisticStats():
    global Statystyki
    global atrybuty

    for i in range(6):
        Statystyki[atrybuty[i]] = random.randint(1, 18)


def IntStats():
    global klasa
    primary = "Dexterity"
    class_result = json.load(open("json/clases.json"))
    for row in class_result['results']:
        if row['name'] == klasa:
            primary = row['primary']

    score_list = []
    for i in range(6):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        roll3 = random.randint(1, 6)
        roll4 = random.randint(1, 6)
        nums = [roll1, roll2, roll3, roll4]
        lowest = min(nums)
        score_list.append(roll1 + roll2 + roll3 + roll4 - lowest)

    Statystyki[primary] = max(score_list)
    score_list.remove(max(score_list))
    if primary != "Dexterity":
        Statystyki["Dexterity"] = max(score_list)
        score_list.remove(max(score_list))
        atrib = [
            "Strength", "Constitution", "Intelligence", "Wisdom", "Charisma"
        ]
        atrib.remove(primary)
        for i in range(4):
            k = random.choice(atrib)
            Statystyki[k] = score_list[0]
            score_list.pop(0)
            atrib.remove(k)
    else:
        atrib = [
            "Strength", "Constitution", "Intelligence", "Wisdom", "Charisma"
        ]
        for i in range(5):
            k = random.choice(atrib)
            Statystyki[k] = score_list[0]
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
    global rasa_art 
    rasa_art = ""
    rasa = random.choice(race_list)
    # rasa = 'Half-Elf'
    # print(Statystyki)
    for row in race_result['results']:
        if str(row['name']) == rasa:
            rasa_art = row['url']
            hated_i = []
            # print(row['asi'])
            for att in row['asi']:
                for i in range(0, 6):
                    # print(atrybuty[i])
                    # print(att['attributes'][0])
                    if atrybuty[i] == att['attributes'][0]:
                        Statystyki[atrybuty[i]] += att['value']
                        hated_i.append(i)
            for att in row['asi']:
                if att['attributes'][0] == 'Other':
                    att_dodaj = random.randint(0, 5)
                    try:
                        hated_i.index(att_dodaj)
                    except:
                        Statystyki[atrybuty[att_dodaj]] += att['value']
                        hated_i.append(att_dodaj)
                    att_dodaj = random.randint(0, 5)

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
        if row['name'] == klasa:
            for nextrow in row['archetype']:
                name = nextrow['name']
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
    if random.randint(1, 3) == 1:
        opis += random.choice(description.mark)
        opis += " "
        opis += random.choice(description.mark_where)
        opis += ". "
    if random.randint(1, 3) == 1:
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
    if Int == "Autistic":
        AutisticStats()
    elif Int != "No":
        Stats()
    else:
        IntStats()
    Losuj_Rasa()
    Losuj_Opis()
    Personality()
    Paint(Statystyki)
    if author == 1234:  #512712313623674910
        subklasa = 'Samurai'
        rasa = 'Tabaxi'
        klasa = 'Fighter'

    if random.randint(
            1, 64
    ) == 32 or author == 329328856831885312 or author == 306811011720019980 or author == 298525408025116672:
        sex = "Femboy XD"
    else:
        sex = random.choice(["Melee", "Femelee"])

    final = "**Rasa:** " + rasa + "\n" + "**Klasa:** " + klasa + '\n' + "**Subklasa:** " + subklasa + '\n' + str(
        Statystyki
    ) + '\n' + '**Sex:** ' + sex + '\n' + '**Personality:** ' + twofourpersonality + '\n**Description:** ' + opis
    return final


def ArtRace():
  global rasa_art
  return rasa_art

def ArtClass():
  global klasa
  global klasy_art
  return klasy_art[klasa]



  

# print("Gotowe")
# Rub_Postac()
