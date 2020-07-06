from json import dumps
from server.database_operations import execute_query, create_database_connection
from timetable_api.EventJsonMapper import databaseToModel


def getCoursesList():
    weekdays = ["pon.", "wt.", "sr.", "czw.", "pt."]
    cnx = create_database_connection()
    resp = execute_query("SELECT * FROM events WHERE study_group NOT LIKE '0' ORDER BY title;", cnx)
    # print(resp)
    cnx.close()
    # json_dict = {}
    courses = []
    # events_list = []
    # for i in range (len(resp)):
    #     # events_list.append(databaseToModel(resp[i]))
    #     event = databaseToModel(resp[i])
    #     if not event.title in json_dict:
    #         json_dict[event.title] = []
    #     single_event_dict = {}
    #     single_event_dict["id"] = event.idx
    #     single_event_dict["info"] = weekdays[event.day-1] + ", " + str(event.start) + "-" + str(event.end) + ", " + event.teacher
    #     json_dict[event.title].append(single_event_dict)
    # return dumps({"courses": json_dict}, ensure_ascii=False)
    course_title = ""

    course = {"name": ""}
    for i in range(len(resp)):
        event = databaseToModel(resp[i])
        # print(course)

        if event.title != course["name"]:
            if course["name"] != "":
                courses.append(course.copy())
            course["events"] = []
            course["name"] = event.title

        single_event_dict = {"id": event.idx, "info": "gr. "+ event.group +", "+weekdays[event.day - 1] + " " + str(event.start) + "-" + str(
            event.end) + ", " + event.teacher}

        course["events"].append(single_event_dict)
        # print(courses)
    return dumps({"courses": courses}, ensure_ascii=False)

# print(getCoursesList())
