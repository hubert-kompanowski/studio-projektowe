from googleapiclient import errors
from googleapiclient.discovery import build
from oauth2client import file as oauth_file, client, tools
from server.database_operations import execute_query, create_database_connection
from timetable_api.TimetableEvent import TimetableEvent
from timetable_api.eventsDAO import get_all_events, set_student_events
from timetable_api.EventJsonMapper import databaseToModel

SCRIPT_ID = 'MAtUnKvmALzI7I-2ZXFKOowN-YzWt5ix_'

def get_courses_for_form():
    cnx = create_database_connection()
    resp = execute_query("SELECT * FROM events WHERE study_group NOT LIKE '0' ORDER BY title, study_group;", cnx)
    cnx.close()
    courses = []
    prev_title = ""
    course = []
    for i in range(len(resp)):
        event = databaseToModel(resp[i])

        if event.title != prev_title:
            if course:
                courses.append(course.copy())
            course = [event.title]
        prev_title = event.title
        course.append(event.group)
    return courses

def execute_request(service, request):
    try:
        # Make the API request.
        response = service.scripts().run(body=request,
                                         scriptId=SCRIPT_ID).execute()

        if 'error' in response:
            # The API executed, but the script returned an error.

            # Extract the first (and only) set of error details. The values of
            # this object are the script's 'errorMessage' and 'errorType', and
            # an list of stack trace elements.
            error = response['error']['details'][0]
            print("Script error message: {0}".format(error['errorMessage']))

            if 'scriptStackTraceElements' in error:
                # There may not be a stacktrace if the script didn't start
                # executing.
                print("Script error stacktrace:")
                for trace in error['scriptStackTraceElements']:
                    print("\t{0}: {1}".format(trace['function'],
                                              trace['lineNumber']))
        else:
            # The structure of the result depends upon what the Apps Script
            # function returns. Here, the function returns an Apps Script Object
            # with String keys and values, and so the result is treated as a
            # Python dictionary (folderSet).
            print("done")
            return response

    except errors.HttpError as e:
        # The API encountered a problem before the script started executing.
        print(e.content)


def create_service():
    # Setup the Apps Script API
    SCOPES = 'https://www.googleapis.com/auth/forms'

    store = oauth_file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    return build('script', 'v1', credentials=creds)


def clear_form():
    service = create_service()
    request = {"function": "create_form", "devMode": "false"}
    execute_request(service, request)


def add_questions():
    service = create_service()
    request = {"function": "add_questions",
               "parameters": [get_courses_for_form()], "devMode": "false"}
    execute_request(service, request)


if __name__ == '__main__':
    clear_form()
    add_questions()
