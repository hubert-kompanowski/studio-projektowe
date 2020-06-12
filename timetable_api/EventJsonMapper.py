from server.database_operations import execute_query, create_database_connection
from timetable_api.TimetableEvent import TimetableEvent
from timetable_api.eventsDAO import get_all_events


def databaseToModel(element):
    return TimetableEvent(element[1], element[2], element[3], element[4], element[5], element[6], element[7],
                          element[8], element[0])


def modelToJson(event: TimetableEvent):
    startDate = "2020-03-0{}T{}".format(event.day + 1, event.start)
    endDate = "2020-03-0{}T{}".format(event.day + 1, event.end)
    title = "{}, Sala: {}, Prowadzący: {}, Grupa: {}, {}".format(event.title, event.room, event.teacher, event.group,
                                                                 event.info)
    jsonEvent = "{" + "startDate: '{}', endDate: '{}', title: '{}'".format(startDate, endDate, title) + "}"
    return jsonEvent

def databaseArrayToJson(events):
    result = "["
    for i in range(len(events)):
        result += modelToJson(databaseToModel(events[i]))
        result += ", "
    result += "]"
    return result


# res = get_all_events()[49]
# print(res)
# print(databaseToModel(res))
# print(modelToJson(databaseToModel(res)))
# print(databaseArrayToJson(get_all_events()))
