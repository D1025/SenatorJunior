import json


def FindPersonality(personality):
  pr = open("json/personality.json")
  personality_result = json.load(pr)
  for row in personality_result['results']:
    name = row['name']
    if name == personality:
      now = row['decription']
  return now