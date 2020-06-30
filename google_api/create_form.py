from googleapiclient import errors
from googleapiclient.discovery import build
from oauth2client import file as oauth_file, client, tools

SCRIPT_ID = 'MAtUnKvmALzI7I-2ZXFKOowN-YzWt5ix_'


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
    request = {"function": "create_form"}
    execute_request(service, request)


def add_questions():
    service = create_service()
    request = {"function": "add_questions",
               "parameters": [[["WTM", "1a", "1b", "2a", "2b"], ["kompi", "1a", "1b"]]]}
    execute_request(service, request)


if __name__ == '__main__':
    clear_form()
    add_questions()
