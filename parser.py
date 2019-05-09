import json

with open("C:/Users/Platon Candell/Documents/Italy/data/congress/93/bills/s/s1/data.json") as f:
  data = json.load(f)

print(data["actions"][0]["acted_at"]) 