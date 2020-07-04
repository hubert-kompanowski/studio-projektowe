from timetable_api.TimetableEvent import TimetableEvent
import json


def databaseToModel(element):
    return TimetableEvent(element[1], element[2], element[3], element[4],
                          element[5], element[6], element[7],
                          element[8], element[0])


def modelToJson(event: TimetableEvent):
    startDate = "2020-06-{}T{}".format(event.day + 25, event.start)
    endDate = "2020-06-{}T{}".format(event.day + 25, event.end)
    title = "{}, Sala: {}, Prowadzący: {}, Grupa: {}, {}".format(event.title,
                                                                 event.room,
                                                                 event.teacher,
                                                                 event.group,
                                                                 event.info)
    jsonEvent = {
        "startDate": startDate,
        "endDate": endDate,
        "title": title
    }
    return json.dumps(jsonEvent)


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
