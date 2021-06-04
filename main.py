import time
from datetime import datetime
import requests
import json

from tokenKey import token

now = datetime.now()
hour = now.hour

activeHoursFromTo = [0, 23] #From, to
activeHours = []

for i in range(activeHoursFromTo[0], activeHoursFromTo[1]):
    activeHours.append(i)

used = []

def log(logTxt: str):
    with open("commits.log", "a") as f:
        f.write(logTxt+"\n")

def getEvents():
    req = requests.get("https://api.github.com/orgs/microsoft/events", headers={"Authorization":"token "+token})
    events = json.loads(req.text)
    filteredEvents = []
    for event in events:
        if event["type"] == "PushEvent":
            filteredEvents.append(event)
    return filteredEvents

def update():
    events = getEvents()
    if len(events) > 0:
        for event in events:
            if event["id"] in used:
                pass
            else:
                login = event["actor"]["login"]
                repo = event["repo"]["name"]
                time_at = event["created_at"]
                log(f"{time_at}: {login} > {repo}")
                print(login+" pushed to "+repo)
                used.append(event["id"])
    time.sleep(5)
    update()
try:
    update()
except Exception:
    update()