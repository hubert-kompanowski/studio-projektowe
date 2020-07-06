from timetable_api.TimetableEvent import TimetableEvent
import json
from datetime import datetime, timedelta


def databaseToModel(element):
    return TimetableEvent(element[1], element[2], element[3], element[4],
                          element[5], element[6], element[7],
                          element[8], element[0])


def modelToJson(event: TimetableEvent):
    week_day = datetime.today().weekday()
    week_day = week_day if week_day < 6 else -1
    monday = datetime.today() - timedelta(days=week_day)


    start_date = (monday + timedelta(days=event.day - 1)).strftime(
        '%Y-%m-%dT') + str(event.start)
    end_date = (monday + timedelta(days=event.day - 1)).strftime(
        '%Y-%m-%dT') + str(event.end)

    title = "{}, Sala: {}, Prowadzący: {}, Grupa: {}, {}".format(event.title,
                                                                 event.room,
                                                                 event.teacher,
                                                                 event.group,
                                                                 event.info)
    json_event = {
        "startDate": start_date,
        "endDate": end_date,
        "title": title
    }
    return json.dumps(json_event)


def databaseArrayToJson(events):
    result = {"data": []}
    for i in range(len(events)):
        result["data"].append(
            json.loads(modelToJson(databaseToModel(events[i]))))

    return json.dumps(result)

# res = get_all_events()[49]
# print(res)
# print(databaseToModel(res))
# print(modelToJson(databaseToModel(res)))
# print(databaseArrayToJson(get_all_events()))
