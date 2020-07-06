from google_api.create_form import create_service, execute_request
from timetable_api.EventJsonMapper import databaseToModel
from timetable_api.eventsDAO import get_all_events, set_student_events, user_exists


def get_answers():
    service = create_service()
    request = {"function": "get_answers", "devMode": "false"}
    response = execute_request(service, request)
    return response['response'].get('result', {})


def assign_courses():
    answers = get_answers()
    # print(answers)
    db_events = get_all_events()
    events = []
    for event in db_events:
        events.append(databaseToModel(event))
    # print(events)
    for answer in answers:
        student_id = answer['Numer indeksu']
        if student_id == "" or not user_exists(student_id):
            continue
        student_events = []
        for course in answer.keys():
            if course is not 'Imię i Nazwisko':
                for event in events:
                    if event.title == course and event.group == answer[course]:
                        student_events.append(event)
        set_student_events(student_id, student_events, True)


if __name__ == '__main__':
    assign_courses()
