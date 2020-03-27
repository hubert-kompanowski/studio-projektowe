import requests
import json
import datetime

class TimetableEvent:
    def __init__(self, name, start):
        self.name = name
        self.start = start
    def __str__(self):
        return self.name+" "+str(self.start)

resp = requests.get("https://planzajec.eaiib.agh.edu.pl/view/timetable/645/events?start=2020-03-02&end=2020-03-07&_=1585327741228")
dataArray = resp.json()

currentElement = dataArray[0]
event = TimetableEvent(currentElement.get('title'), currentElement.get('start'))
print(event)
