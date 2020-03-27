import requests
import json


resp = requests.get("https://planzajec.eaiib.agh.edu.pl/view/timetable/645/events?start=2020-03-02&end=2020-03-07&_=1585327741228")


print(json.dumps(resp.json(), indent=2))


