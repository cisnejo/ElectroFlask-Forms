from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools


def testing():
    SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
    DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))

    store = file.Storage('token.json')
    # Documentation says to have "creds = None", but you can use "store.get()" to have your
    # Google Account remmeber you based on the "token.json" file that gets genertated
    creds = store.get()
    if not creds or creds.invalid:
        # Per Google API Doumentation, your Cliend_ID and Secret should be saved as "credentials.json"
        # You need to either change 'client_secrets.json' to credientials or save the credentials.json file as 'client_secrets.json'
        flow = client.flow_from_clientsecrets('client_secrets.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = discovery.build('forms', 'v1', http=creds.authorize(
        Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

    #  Prints the responses of your specified form:
    form_id = '14oTx7VoIwe9NP3msdkdDNpAq8F6QH1cCJNPBPpsO7J8'
    form_data = service.forms().get(formId=form_id).execute()

    response_data = service.forms().responses().list(formId=form_id).execute()
    print(response_data)
    return ([response_data])


testing()
